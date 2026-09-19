"""
Sales Service - Colombia
Orquesta la lógica de negocio para creación y gestión de ventas
"""
import logging
from datetime import datetime
from typing import List, Dict, Optional, Any
from decimal import Decimal

from data.repositories import SaleRepository, InventoryRepository, ProductRepository
from data import dian as dian_service
from utils.error_handler import (
    handle_errors, 
    BusinessValidationError, 
    DatabaseError,
    PermissionDeniedError
)
from utils.event_bus import publish_event, SALE_CREATED, INVENTORY_UPDATED

logger = logging.getLogger(__name__)


class SalesService:
    """
    Servicio de Ventas - Centraliza toda la lógica de negocio relacionada con ventas
    
    Responsabilidades:
    1. Validar stock disponible antes de crear venta
    2. Calcular totales, impuestos y descuentos
    3. Aplicar promociones automáticas
    4. Crear venta en base de datos
    5. Descontar inventario
    6. Generar documento DIAN (si aplica)
    7. Publicar eventos para otros componentes
    """
    
    def __init__(
        self, 
        sale_repo: SaleRepository = None,
        inventory_repo: InventoryRepository = None,
        product_repo: ProductRepository = None,
        dian_service=None
    ):
        self.sale_repo = sale_repo or SaleRepository()
        self.inventory_repo = inventory_repo or InventoryRepository()
        self.product_repo = product_repo or ProductRepository()
        self.dian_service = dian_service or dian_service
    
    @handle_errors(default_return=None, raise_exceptions=True)
    def create_sale(
        self,
        items: List[Dict[str, Any]],
        client_name: str,
        client_nit: Optional[str] = None,
        payment_method: str = "Contado",
        user_id: int = None,
        observations: Optional[str] = None,
        is_electronic: bool = False
    ) -> Optional[Dict]:
        """
        Crear una nueva venta orchestando múltiples operaciones
        
        Args:
            items: Lista de items [{'product_id': 1, 'quantity': 2, 'price': 1000}, ...]
            client_name: Nombre del cliente
            client_nit: NIT del cliente (opcional)
            payment_method: Método de pago (Contado, Crédito, etc.)
            user_id: ID del usuario que realiza la venta
            observations: Observaciones adicionales
            is_electronic: Si True, genera factura electrónica DIAN
        
        Returns:
            Diccionario con la venta creada o None si falla
        
        Raises:
            BusinessValidationError: Si no hay stock suficiente o datos inválidos
            DatabaseError: Si falla la operación de base de datos
        """
        logger.info(f"Iniciando creación de venta para cliente: {client_name}")
        
        # 1. Validar items no vacíos
        if not items or len(items) == 0:
            raise BusinessValidationError("La venta debe tener al menos un item")
        
        # 2. Validar stock y calcular totales
        processed_items = []
        subtotal = Decimal('0')
        total_tax = Decimal('0')
        total_discount = Decimal('0')
        
        for item in items:
            product_id = item.get('product_id')
            quantity = item.get('quantity', 1)
            
            # Obtener producto
            product = self.product_repo.find_product(product_id)
            if not product:
                raise BusinessValidationError(f"Producto ID {product_id} no existe")
            
            # Validar stock
            if product['stock'] < quantity:
                raise BusinessValidationError(
                    f"Stock insuficiente para '{product['name']}'. "
                    f"Disponible: {product['stock']}, Solicitado: {quantity}"
                )
            
            # Calcular precios
            unit_price = Decimal(str(item.get('price', product['price'])))
            discount = Decimal(str(item.get('discount', 0)))
            tax_rate = Decimal(str(product.get('tax', 0))) / 100
            
            line_subtotal = unit_price * quantity
            line_discount = line_subtotal * (discount / 100)
            line_tax = (line_subtotal - line_discount) * tax_rate
            
            processed_items.append({
                'product_id': product_id,
                'product_name': product['name'],
                'sku': product['sku'],
                'quantity': quantity,
                'unit_price': float(unit_price),
                'subtotal': float(line_subtotal),
                'discount': float(line_discount),
                'tax': float(line_tax),
                'total': float(line_subtotal - line_discount + line_tax)
            })
            
            subtotal += line_subtotal
            total_discount += line_discount
            total_tax += line_tax
        
        # 3. Calcular total final
        total = subtotal - total_discount + total_tax
        
        # 4. Preparar datos de venta
        sale_data = {
            'client': client_name,
            'client_nit': client_nit,
            'items': processed_items,
            'subtotal': float(subtotal),
            'discount': float(total_discount),
            'tax': float(total_tax),
            'total': float(total),
            'payment_method': payment_method,
            'observations': observations,
            'user_id': user_id,
            'date': datetime.now().isoformat(),
            'status': 'completed'
        }
        
        # 5. Crear venta en BD (dentro de transacción implícita)
        try:
            sale_id = self.sale_repo.create_sale(sale_data)
            logger.info(f"Venta creada exitosamente con ID: {sale_id}")
        except Exception as e:
            logger.error(f"Error creando venta: {e}", exc_info=True)
            raise DatabaseError(f"No se pudo crear la venta: {str(e)}")
        
        # 6. Descontar inventario por cada item
        for item in processed_items:
            try:
                self.inventory_repo.register_movement(
                    product_id=item['product_id'],
                    quantity=-item['quantity'],  # Negativo para salida
                    movement_type='sale',
                    reference_id=sale_id,
                    notes=f"Venta ID {sale_id}"
                )
                logger.debug(f"Inventario actualizado para producto {item['product_id']}")
            except Exception as e:
                logger.error(f"Error actualizando inventario: {e}", exc_info=True)
                # Rollback manual si es necesario
                raise DatabaseError(f"No se pudo actualizar el inventario: {str(e)}")
        
        # 7. Generar documento DIAN si es electrónico
        cufe = None
        if is_electronic:
            try:
                # Usar la función generate_cufe del módulo dian
                from data.dian import generate_cufe
                folio = f"VENTA-{sale_id:06d}"
                cufe = generate_cufe(
                    folio=folio,
                    fecha=sale_data['date'],
                    total=float(total),
                    nit_emisor='900123456',  # NIT emisor por defecto
                    nit_receptor=client_nit or '0'
                )
                logger.info(f"Documento DIAN generado con CUFE: {cufe}")
            except Exception as e:
                logger.warning(f"Fallo generando documento DIAN: {e}")
                # No fallar la venta completa, solo loguear
        
        # 8. Publicar evento para actualizar otras pantallas
        publish_event(
            SALE_CREATED,
            sale_id=sale_id,
            total=float(total),
            client=client_name,
            items_count=len(processed_items)
        )
        
        # 9. Publicar evento de actualización de inventario
        for item in processed_items:
            publish_event(
                INVENTORY_UPDATED,
                product_id=item['product_id'],
                quantity_change=-item['quantity']
            )
        
        logger.info(f"Venta completada exitosamente. Total: ${total}")
        
        return {
            'id': sale_id,
            'folio': f"VENTA-{sale_id:06d}",
            'total': float(total),
            'cufe': cufe,
            'items': processed_items
        }
    
    @handle_errors(default_return=[])
    def get_sales_by_date_range(
        self, 
        start_date: str, 
        end_date: str,
        user_id: Optional[int] = None
    ) -> List[Dict]:
        """
        Obtener ventas en un rango de fechas
        
        Args:
            start_date: Fecha inicio (YYYY-MM-DD)
            end_date: Fecha fin (YYYY-MM-DD)
            user_id: Filtrar por usuario (opcional)
        
        Returns:
            Lista de ventas en el rango
        """
        return self.sale_repo.get_sales_by_date(start_date, end_date, user_id)
    
    @handle_errors(default_return=None, raise_exceptions=True)
    def cancel_sale(self, sale_id: int, reason: str, user_id: int = None) -> bool:
        """
        Cancelar una venta y revertir inventario
        
        Args:
            sale_id: ID de la venta a cancelar
            reason: Razón de la cancelación
            user_id: Usuario que cancela
        
        Returns:
            True si se canceló exitosamente
        """
        logger.info(f"Cancelando venta {sale_id}. Razón: {reason}")
        
        # Obtener venta
        sale = self.sale_repo.get_sale(sale_id)
        if not sale:
            raise BusinessValidationError(f"Venta {sale_id} no existe")
        
        if sale.get('status') == 'cancelled':
            raise BusinessValidationError(f"Venta {sale_id} ya está cancelada")
        
        # Revertir inventario
        for item in sale.get('items', []):
            self.inventory_repo.register_movement(
                product_id=item['product_id'],
                quantity=item['quantity'],  # Positivo para entrada
                movement_type='sale_cancel',
                reference_id=sale_id,
                notes=f"Cancelación venta {sale_id}: {reason}"
            )
        
        # Actualizar estado de venta
        self.sale_repo.update_sale_status(sale_id, 'cancelled', reason)
        
        logger.info(f"Venta {sale_id} cancelada exitosamente")
        return True
    
    @handle_errors(default_return={'subtotal': 0, 'tax': 0, 'total': 0})
    def calculate_totals(self, items: List[Dict]) -> Dict:
        """
        Calcular totales de una venta sin crearla
        
        Args:
            items: Lista de items con quantity y price
        
        Returns:
            Diccionario con subtotal, tax, discount y total
        """
        subtotal = Decimal('0')
        total_tax = Decimal('0')
        total_discount = Decimal('0')
        
        for item in items:
            product = self.product_repo.find_product(item.get('product_id'))
            if not product:
                continue
            
            quantity = Decimal(str(item.get('quantity', 1)))
            price = Decimal(str(item.get('price', product['price'])))
            discount_pct = Decimal(str(item.get('discount', 0)))
            tax_rate = Decimal(str(product.get('tax', 0))) / 100
            
            line_subtotal = price * quantity
            line_discount = line_subtotal * (discount_pct / 100)
            line_tax = (line_subtotal - line_discount) * tax_rate
            
            subtotal += line_subtotal
            total_discount += line_discount
            total_tax += line_tax
        
        total = subtotal - total_discount + total_tax
        
        return {
            'subtotal': float(subtotal),
            'discount': float(total_discount),
            'tax': float(total_tax),
            'total': float(total),
            'items_count': len(items)
        }
