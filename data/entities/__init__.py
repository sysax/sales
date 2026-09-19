"""
Entidades de Dominio (DTOs) para el Sistema de Ventas

Estas clases representan los objetos de negocio principales del sistema,
proporcionando type safety, validación y métodos utilitarios.

Usan dataclasses para reducir boilerplate y mantener inmutabilidad donde sea apropiado.
"""
from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any
from datetime import datetime
from enum import Enum
import json


# ============================================================================
# ENUMS DE DOMINIO
# ============================================================================

class UserRole(str, Enum):
    """Roles de usuario en el sistema"""
    ADMIN = "admin"
    VENDEDOR = "vendedor"
    CAJERO = "cajero"
    ALMACEN = "almacen"


class DocumentType(str, Enum):
    """Tipos de documento de cliente/proveedor"""
    NIT = "NIT"
    CEDULA = "Cédula"
    PASAPORTE = "Pasaporte"
    RUT = "RUT"


class RegimenTributario(str, Enum):
    """Regímenes tributarios Colombia DIAN"""
    ORDINARIO = "Ordinario"
    SIMPLIFICADO = "Simplificado"
    NO_RESPONSABLE = "No responsable de IVA"


class PaymentMethod(str, Enum):
    """Métodos de pago"""
    EFECTIVO = "Efectivo"
    TARJETA_CREDITO = "Tarjeta Crédito"
    TARJETA_DEBITO = "Tarjeta Débito"
    TRANSFERENCIA = "Transferencia"
    CHEQUE = "Cheque"


class SaleStatus(str, Enum):
    """Estados de una venta"""
    BORRADOR = "Borrador"
    COMPLETADA = "Completada"
    ANULADA = "Anulada"
    PENDIENTE_PAGO = "Pendiente Pago"
    PARCIAL = "Parcial"


class DianStatus(str, Enum):
    """Estados de sincronización DIAN"""
    SINCRONIZADO = "Sincronizado"
    PENDIENTE = "Pendiente"
    ERROR = "Error"
    RECHAZADO = "Rechazado"


class MovementType(str, Enum):
    """Tipos de movimiento de inventario"""
    ENTRADA = "Entrada"
    SALIDA = "Salida"
    AJUSTE = "Ajuste"
    DEVOLUCION = "Devolución"
    MERMA = "Merma"


# ============================================================================
# ENTIDADES PRINCIPALES
# ============================================================================

@dataclass
class User:
    """Entidad de Usuario del sistema"""
    username: str
    role: UserRole
    active: bool = True
    failed_attempts: int = 0
    locked_until: Optional[datetime] = None
    created_at: Optional[datetime] = None
    last_login: Optional[datetime] = None
    totp_enabled: bool = False
    # Campos computados (no se persisten directamente)
    is_locked: bool = False
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'User':
        """Crear instancia desde diccionario (ej. row de DB)"""
        locked_until = None
        if data.get('locked_until'):
            locked_until = datetime.fromisoformat(data['locked_until'])
        
        created_at = None
        if data.get('created_at'):
            created_at = datetime.fromisoformat(data['created_at'])
            
        last_login = None
        if data.get('last_login'):
            last_login = datetime.fromisoformat(data['last_login'])
        
        return cls(
            username=data['username'],
            role=UserRole(data.get('role', 'vendedor')),
            active=bool(data.get('active', True)),
            failed_attempts=data.get('failed_attempts', 0),
            locked_until=locked_until,
            created_at=created_at,
            last_login=last_login,
            totp_enabled=bool(data.get('totp_enabled', False)),
            is_locked=cls._check_is_locked(locked_until)
        )
    
    @staticmethod
    def _check_is_locked(locked_until: Optional[datetime]) -> bool:
        """Verifica si el usuario está bloqueado actualmente"""
        if locked_until is None:
            return False
        return datetime.now() < locked_until
    
    def to_dict(self) -> Dict[str, Any]:
        """Convertir a diccionario para persistencia"""
        return {
            'username': self.username,
            'role': self.role.value,
            'active': 1 if self.active else 0,
            'failed_attempts': self.failed_attempts,
            'locked_until': self.locked_until.isoformat() if self.locked_until else None,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'last_login': self.last_login.isoformat() if self.last_login else None,
            'totp_enabled': 1 if self.totp_enabled else 0,
        }
    
    def can_login(self) -> bool:
        """Verifica si el usuario puede iniciar sesión"""
        if not self.active:
            return False
        if self.is_locked:
            return False
        return True
    
    def record_failed_attempt(self, max_attempts: int = 5, lock_minutes: int = 30) -> bool:
        """
        Registra intento fallido de login.
        Retorna True si el usuario fue bloqueado.
        """
        self.failed_attempts += 1
        if self.failed_attempts >= max_attempts:
            from datetime import timedelta
            self.locked_until = datetime.now() + timedelta(minutes=lock_minutes)
            self.is_locked = True
            return True
        self.is_locked = self._check_is_locked(self.locked_until)
        return False
    
    def reset_failed_attempts(self):
        """Reseta intentos fallidos después de login exitoso"""
        self.failed_attempts = 0
        self.locked_until = None
        self.is_locked = False
        self.last_login = datetime.now()


@dataclass
class Product:
    """Entidad de Producto"""
    id: int
    sku: str
    name: str
    price: float
    stock: int
    barcode: Optional[str] = None
    description: Optional[str] = None
    category: Optional[str] = None
    subcategory: Optional[str] = None
    brand: Optional[str] = None
    supplier: Optional[str] = None
    price_buy: float = 0.0
    price_wholesale: float = 0.0
    tax: str = "19%"  # IVA Colombia
    unit: str = "unidad"
    stock_min: int = 0
    stock_max: int = 0
    location: Optional[str] = None
    status: str = "activo"
    image: Optional[str] = None
    lote: Optional[str] = None
    vencimiento: Optional[str] = None
    is_kit: bool = False
    kit_items: List[Dict[str, Any]] = field(default_factory=list)
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Product':
        """Crear instancia desde diccionario"""
        kit_json = data.get('kit_json', '[]')
        kit_items = json.loads(kit_json) if isinstance(kit_json, str) else kit_json
        
        return cls(
            id=data['id'],
            sku=data['sku'],
            name=data['name'],
            price=data['price'],
            stock=data['stock'],
            barcode=data.get('barcode'),
            description=data.get('description'),
            category=data.get('cat'),
            subcategory=data.get('subcat'),
            brand=data.get('brand'),
            supplier=data.get('supplier'),
            price_buy=data.get('price_buy', 0.0),
            price_wholesale=data.get('price_wholesale', 0.0),
            tax=data.get('tax', '19%'),
            unit=data.get('unit', 'unidad'),
            stock_min=data.get('stock_min', 0),
            stock_max=data.get('stock_max', 0),
            location=data.get('location'),
            status=data.get('status', 'activo'),
            image=data.get('image'),
            lote=data.get('lote'),
            vencimiento=data.get('vencimiento'),
            is_kit=bool(data.get('is_kit', False)),
            kit_items=kit_items
        )
    
    def to_dict(self) -> Dict[str, Any]:
        """Convertir a diccionario para persistencia"""
        return {
            'id': self.id,
            'sku': self.sku,
            'name': self.name,
            'price': self.price,
            'stock': self.stock,
            'barcode': self.barcode,
            'description': self.description,
            'cat': self.category,
            'subcat': self.subcategory,
            'brand': self.brand,
            'supplier': self.supplier,
            'price_buy': self.price_buy,
            'price_wholesale': self.price_wholesale,
            'tax': self.tax,
            'unit': self.unit,
            'stock_min': self.stock_min,
            'stock_max': self.stock_max,
            'location': self.location,
            'status': self.status,
            'image': self.image,
            'lote': self.lote,
            'vencimiento': self.vencimiento,
            'is_kit': 1 if self.is_kit else 0,
            'kit_json': json.dumps(self.kit_items),
        }
    
    @property
    def needs_reorder(self) -> bool:
        """Verifica si el producto necesita reordenarse"""
        return self.stock <= self.stock_min
    
    @property
    def is_expired(self) -> bool:
        """Verifica si el producto está vencido"""
        if not self.vencimiento:
            return False
        venc_date = datetime.strptime(self.vencimiento, '%Y-%m-%d')
        return datetime.now() > venc_date
    
    def get_tax_rate(self) -> float:
        """Obtiene la tasa de impuesto como decimal (ej. 0.19 para 19%)"""
        if self.tax == "Exento":
            return 0.0
        try:
            return float(self.tax.replace('%', '')) / 100.0
        except ValueError:
            return 0.19  # Default 19% IVA Colombia


@dataclass
class Client:
    """Entidad de Cliente"""
    id: int
    name: str
    nit: Optional[str] = None
    razon_social: Optional[str] = None
    regimen: str = "Simplificado"
    responsabilidad: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    credit: float = 0.0
    credit_limit: float = 0.0
    discount: int = 0  # Porcentaje
    balance: float = 0.0
    price_list: Optional[str] = None
    status: str = "activo"
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Client':
        """Crear instancia desde diccionario"""
        return cls(
            id=data['id'],
            name=data['name'],
            nit=data.get('nit'),
            razon_social=data.get('razon'),
            regimen=data.get('regimen', 'Simplificado'),
            responsabilidad=data.get('responsabilidad'),
            email=data.get('email'),
            phone=data.get('phone'),
            address=data.get('address'),
            city=data.get('city'),
            credit=data.get('credit', 0.0),
            credit_limit=data.get('credit_limit', 0.0),
            discount=data.get('discount', 0),
            balance=data.get('balance', 0.0),
            price_list=data.get('price_list'),
            status=data.get('status', 'activo')
        )
    
    def to_dict(self) -> Dict[str, Any]:
        """Convertir a diccionario para persistencia"""
        return {
            'id': self.id,
            'name': self.name,
            'nit': self.nit,
            'razon': self.razon_social,
            'regimen': self.regimen,
            'responsabilidad': self.responsabilidad,
            'email': self.email,
            'phone': self.phone,
            'address': self.address,
            'city': self.city,
            'credit': self.credit,
            'credit_limit': self.credit_limit,
            'discount': self.discount,
            'balance': self.balance,
            'price_list': self.price_list,
            'status': self.status,
        }
    
    @property
    def has_credit_available(self) -> bool:
        """Verifica si el cliente tiene crédito disponible"""
        return (self.balance + self.credit) < self.credit_limit
    
    @property
    def available_credit(self) -> float:
        """Calcula crédito disponible"""
        return max(0.0, self.credit_limit - self.balance - self.credit)


@dataclass
class SaleItem:
    """Entidad de Ítem de Venta"""
    product_id: int
    product_name: str
    qty: int
    unit_price: float
    subtotal: float
    tax_rate: float = 0.19
    discount: float = 0.0
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'SaleItem':
        """Crear instancia desde diccionario"""
        return cls(
            product_id=data['product_id'],
            product_name=data.get('product_name', ''),
            qty=data['qty'],
            unit_price=data.get('unit_price', data['subtotal'] / data['qty'] if data['qty'] > 0 else 0),
            subtotal=data['subtotal'],
            tax_rate=data.get('tax_rate', 0.19),
            discount=data.get('discount', 0.0)
        )
    
    def to_dict(self) -> Dict[str, Any]:
        """Convertir a diccionario para persistencia"""
        return {
            'product_id': self.product_id,
            'product_name': self.product_name,
            'qty': self.qty,
            'unit_price': self.unit_price,
            'subtotal': self.subtotal,
            'tax_rate': self.tax_rate,
            'discount': self.discount,
        }
    
    @property
    def total_tax(self) -> float:
        """Calcula el impuesto del ítem"""
        return self.subtotal * self.tax_rate
    
    @property
    def total_with_tax(self) -> float:
        """Calcula total con impuesto"""
        return self.subtotal + self.total_tax - self.discount


@dataclass
class Sale:
    """Entidad de Venta/Factura"""
    id: str
    date: datetime
    client_id: int
    client_name: str
    vendedor: str
    items: List[SaleItem]
    subtotal: float
    tax: float
    discount: float = 0.0
    total: float = 0.0
    status: SaleStatus = SaleStatus.COMPLETADA
    doc_type: str = "Factura electrónica DIAN"
    payment_method: Optional[PaymentMethod] = None
    payments: List[Dict[str, Any]] = field(default_factory=list)
    paid: float = 0.0
    balance: float = 0.0
    due_date: Optional[datetime] = None
    dian_cufe: Optional[str] = None
    dian_status: DianStatus = DianStatus.SINCRONIZADO
    promo_code: Optional[str] = None
    notes: Optional[str] = None
    
    def __post_init__(self):
        """Calcular totales después de inicialización"""
        if self.total == 0.0 and self.items:
            self.total = sum(item.total_with_tax for item in self.items) - self.discount
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any], items: List[SaleItem] = None) -> 'Sale':
        """Crear instancia desde diccionario"""
        date = data['date']
        if isinstance(date, str):
            date = datetime.fromisoformat(date)
        
        due_date = None
        if data.get('due'):
            due = data['due']
            if isinstance(due, str):
                due_date = datetime.fromisoformat(due)
        
        payments_json = data.get('payments_json', '[]')
        payments = json.loads(payments_json) if isinstance(payments_json, str) else payments_json
        
        return cls(
            id=data['id'],
            date=date,
            client_id=data.get('client_id', 0),
            client_name=data['client'],
            vendedor=data.get('vendedor', ''),
            items=items or [],
            subtotal=data.get('subtotal', data['total']),
            tax=data.get('tax', 0.0),
            discount=data.get('discount', 0.0),
            total=data['total'],
            status=SaleStatus(data.get('status', 'Completada')),
            doc_type=data.get('doc_type', 'Factura electrónica DIAN'),
            payment_method=PaymentMethod(data['payment']) if data.get('payment') else None,
            payments=payments,
            paid=data.get('paid', 0.0),
            balance=data.get('balance', 0.0),
            due_date=due_date,
            dian_cufe=data.get('dian_cufe'),
            dian_status=DianStatus(data.get('dian_status', 'Sincronizado')),
            promo_code=data.get('promo'),
            notes=data.get('notes')
        )
    
    def to_dict(self) -> Dict[str, Any]:
        """Convertir a diccionario para persistencia"""
        return {
            'id': self.id,
            'date': self.date.isoformat(),
            'client': self.client_name,
            'client_id': self.client_id,
            'vendedor': self.vendedor,
            'total': self.total,
            'subtotal': self.subtotal,
            'tax': self.tax,
            'discount': self.discount,
            'status': self.status.value,
            'doc_type': self.doc_type,
            'payment': self.payment_method.value if self.payment_method else None,
            'payments_json': json.dumps(self.payments),
            'paid': self.paid,
            'balance': self.balance,
            'due': self.due_date.isoformat() if self.due_date else None,
            'estado': self.status.value,
            'dian_cufe': self.dian_cufe,
            'dian_status': self.dian_status.value,
            'promo': self.promo_code,
            'notes': self.notes,
        }
    
    @property
    def is_paid(self) -> bool:
        """Verifica si la venta está completamente pagada"""
        return self.balance <= 0.0
    
    @property
    def is_partial(self) -> bool:
        """Verifica si la venta tiene pago parcial"""
        return 0 < self.balance < self.total
    
    def add_payment(self, amount: float, method: str, user: str):
        """Agregar un pago a la venta"""
        payment = {
            'amount': amount,
            'method': method,
            'user': user,
            'date': datetime.now().isoformat()
        }
        self.payments.append(payment)
        self.paid += amount
        self.balance = max(0.0, self.total - self.paid)
        
        if self.balance == 0:
            self.status = SaleStatus.COMPLETADA
        elif self.paid > 0:
            self.status = SaleStatus.PARCIAL


@dataclass
class InventoryMovement:
    """Entidad de Movimiento de Inventario"""
    id: int
    timestamp: datetime
    sku: str
    product_name: str
    movement_type: MovementType
    qty: int
    before_qty: int
    after_qty: int
    reason: str
    user: str
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'InventoryMovement':
        """Crear instancia desde diccionario"""
        ts = data['ts']
        if isinstance(ts, str):
            ts = datetime.fromisoformat(ts)
        
        return cls(
            id=data['id'],
            timestamp=ts,
            sku=data['sku'],
            product_name=data['product'],
            movement_type=MovementType(data['type']),
            qty=data['qty'],
            before_qty=data['before_qty'],
            after_qty=data['after_qty'],
            reason=data['reason'],
            user=data['user']
        )
    
    def to_dict(self) -> Dict[str, Any]:
        """Convertir a diccionario para persistencia"""
        return {
            'id': self.id,
            'ts': self.timestamp.isoformat(),
            'sku': self.sku,
            'product': self.product_name,
            'type': self.movement_type.value,
            'qty': self.qty,
            'before_qty': self.before_qty,
            'after_qty': self.after_qty,
            'reason': self.reason,
            'user': self.user,
        }


@dataclass
class Supplier:
    """Entidad de Proveedor"""
    id: int
    name: str
    nit: Optional[str] = None
    contact: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    city: Optional[str] = None
    address: Optional[str] = None
    catalog: Optional[str] = None
    lead_time: Optional[str] = None
    payment_terms: Optional[str] = None
    balance: float = 0.0
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Supplier':
        """Crear instancia desde diccionario"""
        return cls(
            id=data['id'],
            name=data['name'],
            nit=data.get('nit'),
            contact=data.get('contact'),
            phone=data.get('phone'),
            email=data.get('email'),
            city=data.get('city'),
            address=data.get('address'),
            catalog=data.get('catalog'),
            lead_time=data.get('lead_time'),
            payment_terms=data.get('payment_terms'),
            balance=data.get('balance', 0.0)
        )
    
    def to_dict(self) -> Dict[str, Any]:
        """Convertir a diccionario para persistencia"""
        return {
            'id': self.id,
            'name': self.name,
            'nit': self.nit,
            'contact': self.contact,
            'phone': self.phone,
            'email': self.email,
            'city': self.city,
            'address': self.address,
            'catalog': self.catalog,
            'lead_time': self.lead_time,
            'payment_terms': self.payment_terms,
            'balance': self.balance,
        }


# ============================================================================
# OBJETOS DE VALOR (Value Objects)
# ============================================================================

@dataclass(frozen=True)
class Money:
    """Value Object para manejo de dinero con precisión"""
    amount: float
    currency: str = "COP"
    
    def __post_init__(self):
        # Redondear a 2 decimales para evitar errores de punto flotante
        object.__setattr__(self, 'amount', round(self.amount, 2))
    
    def __add__(self, other: 'Money') -> 'Money':
        if self.currency != other.currency:
            raise ValueError("Cannot add money with different currencies")
        return Money(self.amount + other.amount, self.currency)
    
    def __sub__(self, other: 'Money') -> 'Money':
        if self.currency != other.currency:
            raise ValueError("Cannot subtract money with different currencies")
        return Money(self.amount - other.amount, self.currency)
    
    def __mul__(self, factor: float) -> 'Money':
        return Money(self.amount * factor, self.currency)
    
    def apply_discount(self, percentage: float) -> 'Money':
        """Aplica un descuento porcentual"""
        if not 0 <= percentage <= 100:
            raise ValueError("Discount percentage must be between 0 and 100")
        return Money(self.amount * (1 - percentage / 100), self.currency)
    
    def apply_tax(self, rate: float) -> 'Money':
        """Aplica un impuesto"""
        return Money(self.amount * (1 + rate), self.currency)
    
    def to_string(self) -> str:
        """Formatea como string con símbolo de moneda"""
        symbols = {"COP": "$", "USD": "$", "EUR": "€"}
        symbol = symbols.get(self.currency, self.currency)
        return f"{symbol}{self.amount:,.2f}"


@dataclass(frozen=True)
class Address:
    """Value Object para direcciones"""
    street: str
    city: str
    state: Optional[str] = None
    postal_code: Optional[str] = None
    country: str = "Colombia"
    
    def to_full_address(self) -> str:
        """Retorna dirección completa formateada"""
        parts = [self.street, self.city]
        if self.state:
            parts.append(self.state)
        if self.postal_code:
            parts.append(self.postal_code)
        parts.append(self.country)
        return ", ".join(filter(None, parts))
