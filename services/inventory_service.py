"""
Inventory Service - Colombia
Orquesta la lógica de negocio para gestión de inventario
"""
import logging
from datetime import datetime
from typing import List, Dict, Optional, Any

from data.repositories import InventoryRepository, ProductRepository
from utils.error_handler import (
    handle_errors, 
    BusinessValidationError, 
    DatabaseError
)
from utils.event_bus import publish_event, INVENTORY_UPDATED

logger = logging.getLogger(__name__)


class InventoryService:
    """
    Servicio de Inventario - Centraliza toda la lógica de negocio relacionada con inventario
    
    Responsabilidades:
    1. Registrar movimientos de entrada/salida
    2. Validar stock antes de operaciones
    3. Generar alertas de stock bajo
    4. Realizar ajustes de inventario
    5. Calcular valorización de inventario
    """
    
    def __init__(
        self,
        inventory_repo: InventoryRepository = None,
        product_repo: ProductRepository = None
    ):
        self.inventory_repo = inventory_repo or InventoryRepository()
        self.product_repo = product_repo or ProductRepository()
    
    @handle_errors(default_return=None)
    def register_purchase(
        self,
        product_id: int,
        quantity: int,
        cost_price: float,
        supplier_name: str,
        invoice_number: Optional[str] = None,
        notes: Optional[str] = None
    ) -> Optional[Dict]:
        """
        Registrar entrada de inventario por compra
        
        Args:
            product_id: ID del producto
            quantity: Cantidad a ingresar
            cost_price: Precio de costo unitario
            supplier_name: Nombre del proveedor
            invoice_number: Número de factura (opcional)
            notes: Notas adicionales
        
        Returns:
            Movimiento registrado o None si falla
        """
        logger.info(f"Registrando compra: producto {product_id}, cantidad {quantity}")
        
        # Validar cantidad positiva
        if quantity <= 0:
            raise BusinessValidationError("La cantidad debe ser mayor a 0")
        
        # Obtener producto
        product = self.product_repo.get_product(product_id)
        if not product:
            raise BusinessValidationError(f"Producto {product_id} no existe")
        
        # Registrar movimiento
        movement_id = self.inventory_repo.register_movement(
            product_id=product_id,
            quantity=quantity,
            movement_type='purchase',
            reference_id=invoice_number,
            notes=notes or f"Compra de {quantity} unidades a ${cost_price}"
        )
        
        # Actualizar precio de costo promedio
        current_stock = product['stock']
        current_cost = product.get('price_buy', 0)
        new_stock = current_stock + quantity
        
        if new_stock > 0:
            new_cost = ((current_stock * current_cost) + (quantity * cost_price)) / new_stock
            
            # Actualizar producto con nuevo stock y costo
            self.product_repo.update_product(product_id, {
                'stock': new_stock,
                'price_buy': new_cost
            })
        
        # Publicar evento
        publish_event(
            INVENTORY_UPDATED,
            product_id=product_id,
            quantity_change=quantity,
            movement_type='purchase'
        )
        
        logger.info(f"Compra registrada. Nuevo stock: {new_stock}")
        
        return {
            'movement_id': movement_id,
            'product_id': product_id,
            'quantity': quantity,
            'new_stock': new_stock,
            'new_cost': new_cost
        }
    
    @handle_errors(default_return=None)
    def register_adjustment(
        self,
        product_id: int,
        quantity: int,
        reason: str,
        user_id: int = None,
        notes: Optional[str] = None
    ) -> Optional[Dict]:
        """
        Registrar ajuste de inventario (positivo o negativo)
        
        Args:
            product_id: ID del producto
            quantity: Cantidad a ajustar (positivo=add, negativo=remove)
            reason: Razón del ajuste
            user_id: Usuario que realiza el ajuste
            notes: Notas adicionales
        
        Returns:
            Movimiento registrado o None si falla
        """
        logger.info(f"Registrando ajuste: producto {product_id}, cantidad {quantity}")
        
        # Validar cantidad
        if quantity == 0:
            raise BusinessValidationError("La cantidad debe ser diferente de 0")
        
        # Obtener producto
        product = self.product_repo.get_product(product_id)
        if not product:
            raise BusinessValidationError(f"Producto {product_id} no existe")
        
        # Validar que no quede stock negativo
        new_stock = product['stock'] + quantity
        if new_stock < 0:
            raise BusinessValidationError(
                f"No se puede ajustar. Stock actual: {product['stock']}, "
                f"Ajuste: {quantity}. Resultaría en stock negativo."
            )
        
        # Registrar movimiento
        movement_id = self.inventory_repo.register_movement(
            product_id=product_id,
            quantity=quantity,
            movement_type='adjustment',
            reference_id=None,
            notes=notes or f"Ajuste: {reason}"
        )
        
        # Actualizar stock
        self.product_repo.update_product(product_id, {'stock': new_stock})
        
        # Publicar evento
        publish_event(
            INVENTORY_UPDATED,
            product_id=product_id,
            quantity_change=quantity,
            movement_type='adjustment'
        )
        
        logger.info(f"Ajuste registrado. Nuevo stock: {new_stock}")
        
        return {
            'movement_id': movement_id,
            'product_id': product_id,
            'quantity': quantity,
            'new_stock': new_stock,
            'reason': reason
        }
    
    @handle_errors(default_return=[])
    def get_low_stock_products(self, threshold_multiplier: float = 1.0) -> List[Dict]:
        """
        Obtener productos con stock bajo
        
        Args:
            threshold_multiplier: Multiplicador del stock mínimo (default: 1.0)
        
        Returns:
            Lista de productos con stock bajo
        """
        products = self.product_repo.list_products()
        low_stock = []
        
        for product in products:
            stock_min = product.get('stock_min', 0)
            threshold = stock_min * threshold_multiplier
            
            if product['stock'] < threshold:
                low_stock.append({
                    **product,
                    'stock_status': 'low',
                    'threshold': threshold,
                    'shortage': threshold - product['stock']
                })
        
        return low_stock
    
    @handle_errors(default_return={'total_value': 0, 'products_count': 0})
    def get_inventory_valuation(self) -> Dict:
        """
        Calcular valorización total del inventario
        
        Returns:
            Diccionario con valor total y detalles
        """
        products = self.product_repo.list_products()
        
        total_value = 0
        valuation_details = []
        
        for product in products:
            stock = product.get('stock', 0)
            cost = product.get('price_buy', 0)
            value = stock * cost
            
            if value > 0:
                valuation_details.append({
                    'product_id': product['id'],
                    'name': product['name'],
                    'sku': product['sku'],
                    'stock': stock,
                    'cost': cost,
                    'value': value
                })
                total_value += value
        
        return {
            'total_value': total_value,
            'products_count': len(valuation_details),
            'details': valuation_details
        }
    
    @handle_errors(default_return=[])
    def get_movements_by_product(
        self, 
        product_id: int, 
        start_date: Optional[str] = None,
        end_date: Optional[str] = None
    ) -> List[Dict]:
        """
        Obtener movimientos de un producto
        
        Args:
            product_id: ID del producto
            start_date: Fecha inicio (opcional)
            end_date: Fecha fin (opcional)
        
        Returns:
            Lista de movimientos
        """
        return self.inventory_repo.get_movements_by_product(
            product_id, 
            start_date, 
            end_date
        )
