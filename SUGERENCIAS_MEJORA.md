# 📋 Sugerencias de Mejora - Sistema de Ventas KivyMD

## 🔍 Análisis del Estado Actual

El proyecto cuenta con una arquitectura sólida que incluye:
- ✅ 14 pantallas funcionales (login, dashboard + 12 módulos)
- ✅ 10 repositorios especializados (93 métodos distribuidos)
- ✅ Tests automatizados (92 tests pasando)
- ✅ Facturación electrónica DIAN (validación NIT, CUFE, XML UBL 2.1)
- ✅ Sincronización offline mejorada (backoff exponencial, circuit breaker, métricas)
- ✅ Autenticación segura (PBKDF2, 2FA TOTP, lockout por intentos)
- ✅ Control de permisos por roles (5 roles definidos)

---

## 🎯 Sugerencias de Mejora Prioritarias

### 1. **Refactorización del Repository Monolítico** ⭐⭐⭐

**Problema:** `data/repository.py` tiene 1560 líneas y la nueva arquitectura en `data/repositories/` no está siendo utilizada por las pantallas existentes.

**Solución Propuesta:**

```python
# main.py - Reemplazar:
from data.repository import repo

# Por:
from data.repositories import (
    UserRepository,
    ProductRepository,
    SaleRepository,
    InventoryRepository,
    CajaRepository
)

# Crear instancia única global o usar inyección de dependencias
class SalesApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.user_repo = UserRepository()
        self.product_repo = ProductRepository()
        self.sale_repo = SaleRepository()
        # ... etc
```

**Beneficios:**
- Mejor cohesión y separación de responsabilidades
- Más fácil de testear individualmente
- Permite evolución independiente por dominio

**Esfuerzo:** Alto (requiere actualizar 14 pantallas)
**Impacto:** Muy Alto

---

### 2. **Agregar Service Layer** ⭐⭐⭐

**Problema:** La lógica de negocio está dispersa entre repositorios y pantallas.

**Solución Propuesta:**

```python
# services/
# ├── __init__.py
# ├── auth_service.py
# ├── sales_service.py
# ├── inventory_service.py
# └── sync_service.py

# services/sales_service.py
class SalesService:
    def __init__(self, sale_repo, inventory_repo, dian_service):
        self.sale_repo = sale_repo
        self.inventory_repo = inventory_repo
        self.dian_service = dian_service
    
    def create_sale(self, cart_items, client, payment_method, user):
        """
        Orquesta creación de venta:
        1. Validar stock disponible
        2. Calcular totales e impuestos
        3. Aplicar promociones
        4. Crear venta
        5. Descontar inventario
        6. Generar documento DIAN (si aplica)
        7. Registrar en bitácora
        """
        # Lógica de negocio centralizada
        pass
```

**Beneficios:**
- Lógica de negocio en un solo lugar
- Fácil de testear con mocks
- Reutilizable desde múltiples pantallas
- Sigue principio Single Responsibility

**Esfuerzo:** Medio-Alto
**Impacto:** Muy Alto

---

### 3. **Mejorar Manejo de Errores Global** ⭐⭐

**Problema:** Los errores se manejan con prints y try/except dispersos.

**Solución Propuesta:**

```python
# utils/error_handler.py
import logging
from functools import wraps

logger = logging.getLogger(__name__)

def handle_errors(default_return=None):
    """Decorator para manejo consistente de errores"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except BusinessValidationError as e:
                logger.warning(f"Error de validación: {e}")
                show_snackbar(str(e), level="warning")
                return default_return
            except DatabaseError as e:
                logger.error(f"Error de BD: {e}", exc_info=True)
                show_snackbar("Error de base de datos", level="error")
                return default_return
            except Exception as e:
                logger.critical(f"Error inesperado: {e}", exc_info=True)
                show_snackbar("Error interno del sistema", level="error")
                return default_return
        return wrapper
    return decorator

# Uso en pantallas:
@handle_errors(default_return=[])
def load_products(self):
    return self.product_repo.list_products()
```

**Beneficios:**
- Manejo consistente de errores
- Logging estructurado
- Mejor experiencia de usuario
- Debugging más fácil

**Esfuerzo:** Bajo
**Impacto:** Alto

---

### 4. **Implementar Event Bus / Pub-Sub** ⭐⭐

**Problema:** Las pantallas necesitan actualizarse mutuamente (ej: venta actualiza inventario).

**Solución Propuesta:**

```python
# utils/event_bus.py
from blinker import signal

# Señales disponibles
sale_created = signal('sale-created')
inventory_updated = signal('inventory-updated')
user_logged_in = signal('user-logged-in')
sync_completed = signal('sync-completed')

# Publicar evento
sale_created.send(self, sale_id=123, total=50000)

# Suscribirse en pantalla de inventario
sale_created.connect(self.on_sale_created, weak=False)

def on_sale_created(self, sender, sale_id, total):
    self.refresh_inventory()
```

**Alternativa sin dependencias externas:**

```python
# utils/event_bus.py
from collections import defaultdict

class EventBus:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.listeners = defaultdict(list)
        return cls._instance
    
    def subscribe(self, event_type, callback):
        self.listeners[event_type].append(callback)
    
    def publish(self, event_type, **data):
        for callback in self.listeners.get(event_type, []):
            try:
                callback(**data)
            except Exception as e:
                logging.error(f"Error en listener {event_type}: {e}")

# Uso
bus = EventBus()
bus.subscribe('inventory_updated', self.refresh_ui)
bus.publish('inventory_updated', product_id=123)
```

**Beneficios:**
- Desacoplamiento total entre componentes
- Fácil agregar nuevos listeners
- Múltiples reacciones a un mismo evento

**Esfuerzo:** Medio
**Impacto:** Alto

---

### 5. **Agregar DTOs / Entidades de Dominio** ⭐⭐

**Problema:** Se usan diccionarios y rows de DB directamente, lo que es propenso a errores.

**Solución Propuesta:**

```python
# models/product.py
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, List

@dataclass
class Product:
    id: int
    sku: str
    name: str
    price: float
    price_buy: float
    stock: int
    stock_min: int
    stock_max: int
    barcode: Optional[str] = None
    category: Optional[str] = None
    kit_items: List[dict] = field(default_factory=list)
    created_at: Optional[datetime] = None
    
    @property
    def is_low_stock(self) -> bool:
        return self.stock < self.stock_min
    
    @property
    def is_available(self) -> bool:
        return self.stock > 0
    
    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'sku': self.sku,
            # ... etc
        }
    
    @classmethod
    def from_row(cls, row: dict) -> 'Product':
        return cls(
            id=row['id'],
            sku=row['sku'],
            name=row['name'],
            # ... etc
        )

# models/sale.py
@dataclass
class SaleItem:
    product_id: int
    product_name: str
    quantity: int
    unit_price: float
    subtotal: float
    discount: float = 0.0
    tax: float = 0.0

@dataclass  
class Sale:
    id: int
    folio: str
    client_name: str
    items: List[SaleItem]
    subtotal: float
    tax: float
    total: float
    payment_method: str
    status: str
    created_at: datetime
    cufe: Optional[str] = None
    
    @property
    def item_count(self) -> int:
        return sum(item.quantity for item in self.items)
```

**Beneficios:**
- Type safety
- autocomplete en IDEs
- Validación en constructor
- Métodos de dominio encapsulados

**Esfuerzo:** Medio-Alto
**Impacto:** Medio-Alto

---

### 6. **Mejorar Testing de Repositorios Especializados** ⭐⭐

**Problema:** Solo hay tests para el repository monolítico, no para los nuevos repositorios.

**Solución Propuesta:**

```python
# tests/test_repositories/
# ├── __init__.py
# ├── test_user_repository.py
# ├── test_product_repository.py
# ├── test_sale_repository.py
# └── test_inventory_repository.py

# tests/test_repositories/test_user_repository.py
import pytest
from data.repositories import UserRepository

class TestUserRepository:
    @pytest.fixture
    def repo(self):
        return UserRepository()
    
    def test_list_users_returns_all(self, repo):
        users = repo.list_users()
        assert len(users) >= 5  # Admin + 4 usuarios seed
    
    def test_find_user_valid_credentials(self, repo):
        user = repo.find_user('admin', 'admin123')
        assert user is not None
        assert user['username'] == 'admin'
        assert 'password' not in user or user['password'] == '***'
    
    def test_find_user_invalid_password(self, repo):
        user = repo.find_user('admin', 'wrong')
        assert user is None
    
    def test_add_user_success(self, repo):
        repo.add_user('test_user', 'Test123!', 'Vendedor')
        users = repo.list_users()
        assert any(u['username'] == 'test_user' for u in users)
    
    def test_lockout_after_3_failures(self, repo):
        # Intentar 3 veces con password incorrecto
        for i in range(3):
            repo.find_user('admin', 'wrong')
        
        # Cuarto intento debería fallar aunque password sea correcto
        user = repo.find_user('admin', 'admin123')
        assert user is None  # Bloqueado
```

**Esfuerzo:** Medio
**Impacto:** Alto (mejora calidad del código)

---

### 7. **Agregar Migraciones de Base de Datos Formales** ⭐⭐

**Problema:** Las migraciones están hardcodeadas en `db.py` sin versionado.

**Solución Propuesta:**

```python
# data/migrations/
# ├── __init__.py
# ├── 001_initial_schema.sql
# ├── 002_add_user_security.sql
# ├── 003_add_dian_settings.sql
# └── 004_add_outbox_table.sql

# data/migration_manager.py
class MigrationManager:
    MIGRATIONS = [
        ('001_initial_schema', 'Crear tablas base'),
        ('002_add_user_security', 'Agregar columnas de seguridad usuarios'),
        ('003_add_dian_settings', 'Tabla configuración DIAN'),
        ('004_add_outbox_table', 'Tabla sincronización offline'),
    ]
    
    def get_current_version(self):
        conn = sqlite.get_conn()
        cur = conn.cursor()
        cur.execute("SELECT version FROM schema_migrations ORDER BY version DESC LIMIT 1")
        result = cur.fetchone()
        conn.close()
        return result[0] if result else '000'
    
    def migrate(self):
        current = self.get_current_version()
        pending = [m for m in self.MIGRATIONS if m[0] > current]
        
        for migration_id, description in pending:
            print(f"Ejecutando {migration_id}: {description}")
            sql_path = f"data/migrations/{migration_id}.sql"
            with open(sql_path) as f:
                sql = f.read()
            sqlite.execute_script(sql)
            
            # Registrar migración
            conn = sqlite.get_conn()
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO schema_migrations (version, applied_at) VALUES (?, ?)",
                (migration_id, datetime.now().isoformat())
            )
            conn.commit()
            conn.close()
```

**Beneficios:**
- Versionado claro de esquema
- Rollback posible
- Reproducible en diferentes ambientes
- Audit trail de cambios

**Esfuerzo:** Medio
**Impacto:** Medio

---

### 8. **Optimizar Consultas de Base de Datos** ⭐

**Problema:** Algunas consultas pueden ser ineficientes con grandes volúmenes de datos.

**Solución Propuesta:**

```python
# Agregar índices en db.py
CREATE INDEX IF NOT EXISTS idx_products_sku ON products(sku);
CREATE INDEX IF NOT EXISTS idx_products_barcode ON products(barcode);
CREATE INDEX IF NOT EXISTS idx_products_category ON products(category);
CREATE INDEX IF NOT EXISTS idx_sales_date ON sales(date);
CREATE INDEX IF NOT EXISTS idx_sales_client ON sales(client_name);
CREATE INDEX IF NOT EXISTS idx_outbox_status ON outbox(status, created_ts);
CREATE INDEX IF NOT EXISTS idx_users_username ON users(username);

# Usar EXPLAIN QUERY PLAN para analizar consultas lentas
cur.execute("EXPLAIN QUERY PLAN SELECT * FROM products WHERE stock < stock_min")
print(cur.fetchall())

# Paginación para listas grandes
def list_products_paginated(self, page=1, per_page=50):
    offset = (page - 1) * per_page
    cur.execute(
        "SELECT * FROM products ORDER BY id LIMIT ? OFFSET ?",
        (per_page, offset)
    )
    return cur.fetchall()
```

**Esfuerzo:** Bajo
**Impacto:** Alto (performance)

---

### 9. **Agregar Caché para Consultas Frecuentes** ⭐

**Problema:** Consultas repetitivas a DB impactan performance.

**Solución Propuesta:**

```python
# utils/cache.py
from functools import wraps
from time import time
from threading import Lock

class SimpleCache:
    def __init__(self, ttl_seconds=300):
        self._cache = {}
        self._timestamps = {}
        self._lock = Lock()
        self.ttl = ttl_seconds
    
    def get(self, key):
        with self._lock:
            if key in self._cache:
                if time() - self._timestamps[key] < self.ttl:
                    return self._cache[key]
                else:
                    del self._cache[key]
                    del self._timestamps[key]
            return None
    
    def set(self, key, value):
        with self._lock:
            self._cache[key] = value
            self._timestamps[key] = time()
    
    def invalidate(self, key):
        with self._lock:
            if key in self._cache:
                del self._cache[key]
                del self._timestamps[key]
    
    def clear(self):
        with self._lock:
            self._cache.clear()
            self._timestamps.clear()

# Decorador para cachear resultados
def cached(cache_instance, key_prefix=''):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            key = f"{key_prefix}:{func.__name__}:{str(args)}:{str(kwargs)}"
            result = cache_instance.get(key)
            if result is not None:
                return result
            
            result = func(*args, **kwargs)
            cache_instance.set(key, result)
            return result
        return wrapper
    return decorator

# Uso
cache = SimpleCache(ttl_seconds=60)

@cached(cache, key_prefix='products')
def list_products(self):
    # Consulta a DB
    pass
```

**Esfuerzo:** Bajo-Medio
**Impacto:** Medio-Alto (performance)

---

### 10. **Mejorar UI con Estados de Carga** ⭐

**Problema:** No hay feedback visual durante operaciones largas.

**Solución Propuesta:**

```python
# components/loading_overlay.py
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.spinner import MDSpinner
from kivymd.uix.label import MDLabel

class LoadingOverlay(MDBoxLayout):
    def __init__(self, text="Cargando...", **kwargs):
        super().__init__(orientation='vertical', 
                        md_bg_color=(0, 0, 0, 0.5),
                        **kwargs)
        
        spinner = MDSpinner(size_hint=(None, None), size=(dp(46), dp(46)))
        label = MDLabel(text=text, halign='center', theme_text_color='Custom')
        
        self.add_widget(spinner)
        self.add_widget(label)

# Uso en pantalla
def save_product(self):
    # Mostrar loading
    overlay = LoadingOverlay("Guardando producto...")
    self.parent.add_widget(overlay)
    
    # Ejecutar en background
    from threading import Thread
    def do_save():
        try:
            self.product_repo.save_product(data)
            Clock.schedule_once(lambda dt: self.show_success(), 0)
        except Exception as e:
            Clock.schedule_once(lambda dt: self.show_error(e), 0)
        finally:
            Clock.schedule_once(lambda dt: self.parent.remove_widget(overlay), 0)
    
    Thread(target=do_save).start()
```

**Esfuerzo:** Bajo
**Impacto:** Medio (UX)

---

### 11. **Agregar Logging Estructurado** ⭐

**Problema:** Se usa print() para debugging.

**Solución Propuesta:**

```python
# utils/logger.py
import logging
from datetime import datetime
from pathlib import Path

def setup_logger(name, level=logging.INFO):
    log_dir = Path('logs')
    log_dir.mkdir(exist_ok=True)
    
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    log_file = log_dir / f'{name}_{timestamp}.log'
    
    formatter = logging.Formatter(
        '%(asctime)s | %(levelname)-8s | %(name)s | %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # File handler
    file_handler = logging.FileHandler(log_file, encoding='utf-8')
    file_handler.setFormatter(formatter)
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger

# Uso
logger = setup_logger('sales_app')
logger.info('Aplicación iniciada')
logger.debug('Usuario autenticado: admin')
logger.warning('Stock bajo para producto PROD001')
logger.error('Error al conectar con servidor DIAN', exc_info=True)
```

**Esfuerzo:** Bajo
**Impacto:** Medio (mantenibilidad)

---

### 12. **Agregar Validación de Datos Centralizada** ⭐

**Problema:** Validaciones dispersas en múltiples lugares.

**Solución Propuesta:**

```python
# validators/__init__.py
from validators.product_validator import ProductValidator
from validators.sale_validator import SaleValidator
from validators.user_validator import UserValidator

# validators/product_validator.py
from dataclasses import dataclass
from typing import List, Tuple

@dataclass
class ValidationError:
    field: str
    message: str
    code: str

class ProductValidator:
    @staticmethod
    def validate_create(data: dict) -> List[ValidationError]:
        errors = []
        
        # SKU requerido
        if not data.get('sku'):
            errors.append(ValidationError('sku', 'SKU es requerido', 'REQUIRED'))
        elif len(data['sku']) < 3:
            errors.append(ValidationError('sku', 'SKU debe tener al menos 3 caracteres', 'TOO_SHORT'))
        
        # Nombre requerido
        if not data.get('name'):
            errors.append(ValidationError('name', 'Nombre es requerido', 'REQUIRED'))
        
        # Precio positivo
        price = data.get('price', 0)
        if price <= 0:
            errors.append(ValidationError('price', 'Precio debe ser mayor a 0', 'INVALID'))
        
        # Stock no negativo
        stock = data.get('stock', 0)
        if stock < 0:
            errors.append(ValidationError('stock', 'Stock no puede ser negativo', 'INVALID'))
        
        return errors
    
    @staticmethod
    def is_valid(errors: List[ValidationError]) -> bool:
        return len(errors) == 0

# Uso en pantalla
from validators import ProductValidator

def save_product(self):
    errors = ProductValidator.validate_create(self.product_data)
    
    if not ProductValidator.is_valid(errors):
        error_messages = '\n'.join([f"• {e.field}: {e.message}" for e in errors])
        self.show_dialog("Errores de validación", error_messages)
        return
    
    # Proceder a guardar
    self.product_repo.create(self.product_data)
```

**Esfuerzo:** Medio
**Impacto:** Alto (calidad de datos)

---

### 13. **Implementar Backup Automático** ⭐⭐

**Problema:** No hay mecanismo automático de backup de la base de datos.

**Solución Propuesta:**

```python
# utils/backup.py
import shutil
from datetime import datetime
from pathlib import Path

class BackupManager:
    def __init__(self, db_path='data/sistema_ventas.db', backup_dir='backups'):
        self.db_path = Path(db_path)
        self.backup_dir = Path(backup_dir)
        self.backup_dir.mkdir(exist_ok=True)
    
    def create_backup(self) -> Path:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_path = self.backup_dir / f'backup_{timestamp}.db'
        
        # Copiar archivo DB
        shutil.copy2(self.db_path, backup_path)
        
        # Comprimir (opcional)
        # import gzip
        # with open(backup_path, 'rb') as f_in, gzip.open(f'{backup_path}.gz', 'wb') as f_out:
        #     shutil.copyfileobj(f_in, f_out)
        
        print(f"Backup creado: {backup_path}")
        return backup_path
    
    def cleanup_old_backups(self, keep_days=30):
        """Eliminar backups mayores a N días"""
        from time import time
        
        cutoff = time() - (keep_days * 86400)
        
        for backup_file in self.backup_dir.glob('backup_*.db'):
            if backup_file.stat().st_mtime < cutoff:
                backup_file.unlink()
                print(f"Backup eliminado: {backup_file}")
    
    def restore_backup(self, backup_path: str):
        """Restaurar desde backup"""
        backup = Path(backup_path)
        if not backup.exists():
            raise FileNotFoundError(f"Backup no encontrado: {backup_path}")
        
        # Hacer backup del estado actual antes de restaurar
        self.create_backup()
        
        # Restaurar
        shutil.copy2(backup, self.db_path)
        print(f"Backup restaurado: {backup_path}")

# Programar backup diario
# En main.py o módulo separado
from apscheduler.schedulers.base import BaseScheduler
from apscheduler.triggers.cron import CronTrigger

scheduler = BaseScheduler()
backup_mgr = BackupManager()

@scheduler.scheduled_job(CronTrigger(hour=2, minute=0))  # 2 AM diario
def daily_backup():
    backup_mgr.create_backup()
    backup_mgr.cleanup_old_backups(keep_days=30)

scheduler.start()
```

**Esfuerzo:** Medio
**Impacto:** Muy Alto (seguridad de datos)

---

### 14. **Agregar Exportación a Excel/PDF Mejorada** ⭐

**Problema:** La exportación actual es básica.

**Solución Propuesta:**

```python
# utils/export.py
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, PatternFill
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

class ExcelExporter:
    @staticmethod
    def export_sales(sales_data, filename='ventas.xlsx'):
        wb = Workbook()
        ws = wb.active
        ws.title = "Ventas"
        
        # Headers con estilo
        headers = ['Folio', 'Fecha', 'Cliente', 'Total', 'Estado']
        for col, header in enumerate(headers, 1):
            cell = ws.cell(row=1, column=col, value=header)
            cell.font = Font(bold=True)
            cell.fill = PatternFill(start_color='4472C4', end_color='4472C4', fill_type='solid')
            cell.font = Font(color='FFFFFF', bold=True)
        
        # Datos
        for row_idx, sale in enumerate(sales_data, 2):
            ws.cell(row=row_idx, column=1, value=sale['folio'])
            ws.cell(row=row_idx, column=2, value=sale['date'])
            ws.cell(row=row_idx, column=3, value=sale['client'])
            ws.cell(row=row_idx, column=4, value=sale['total'])
            ws.cell(row=row_idx, column=5, value=sale['status'])
        
        # Auto-width columns
        for column in ws.columns:
            max_length = 0
            column_letter = column[0].column_letter
            for cell in column:
                try:
                    max_length = max(max_length, len(str(cell.value)))
                except:
                    pass
            ws.column_dimensions[column_letter].width = max_length + 2
        
        wb.save(filename)
        return filename

class PDFExporter:
    @staticmethod
    def export_report(data, filename='reporte.pdf'):
        doc = SimpleDocTemplate(filename, pagesize=letter)
        elements = []
        
        # Título
        from reportlab.platypus import Paragraph
        from reportlab.lib.styles import getSampleStyleSheet
        styles = getSampleStyleSheet()
        title = Paragraph("Reporte de Ventas", styles['Heading1'])
        elements.append(title)
        
        # Tabla
        table_data = [['Folio', 'Fecha', 'Cliente', 'Total']]
        for sale in data:
            table_data.append([
                sale['folio'],
                sale['date'],
                sale['client'],
                f"${sale['total']:,.2f}"
            ])
        
        table = Table(table_data)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), '#4472C4'),
            ('TEXTCOLOR', (0, 0), (-1, 0), '#FFFFFF'),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('GRID', (0, 0), (-1, -1), 1, '#000000'),
        ]))
        
        elements.append(table)
        doc.build(elements)
        return filename
```

**Esfuerzo:** Medio
**Impacto:** Medio (funcionalidad)

---

### 15. **Agregar Dashboard con Gráficos** ⭐⭐

**Problema:** El dashboard actual muestra tarjetas pero no gráficos visuales.

**Solución Propuesta:**

```python
# screens/dashboard.py - Agregar gráficos
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

class DashboardScreen(MDScreen):
    def build_chart(self, data):
        fig, ax = plt.subplots(figsize=(6, 4))
        
        # Gráfico de barras - Ventas por día
        days = [d['day'] for d in data]
        sales = [d['total'] for d in data]
        
        ax.bar(days, sales, color='#7FCEA0')
        ax.set_xlabel('Día')
        ax.set_ylabel('Ventas (COP)')
        ax.set_title('Ventas de la Semana')
        ax.tick_params(axis='x', rotation=45)
        
        plt.tight_layout()
        
        # Convertir a widget Kivy
        canvas = FigureCanvasKivyAgg(figure=fig)
        return canvas
    
    def load_dashboard(self):
        # Obtener datos
        sales_data = self.sale_repo.get_weekly_sales()
        
        # Crear gráfico
        chart_widget = self.build_chart(sales_data)
        
        # Agregar al layout
        self.ids.chart_container.add_widget(chart_widget)
```

**En KV:**
```kv
<DashboardScreen>:
    BoxLayout:
        orientation: 'vertical'
        
        ScrollView:
            GridLayout:
                cols: 1
                size_hint_y: None
                height: self.minimum_height
                
                # Tarjetas existentes
                BoxLayout:
                    id: cards_container
                    size_hint_y: None
                    height: dp(150)
                
                # Contenedor de gráficos
                BoxLayout:
                    id: chart_container
                    size_hint_y: None
                    height: dp(400)
                    orientation: 'vertical'
```

**Esfuerzo:** Medio
**Impacto:** Alto (visualización de datos)

---

## 📊 Resumen de Prioridades

| # | Mejora | Esfuerzo | Impacto | Prioridad |
|---|--------|----------|---------|-----------|
| 1 | Refactorizar Repository monolítico | Alto | Muy Alto | ⭐⭐⭐ |
| 2 | Agregar Service Layer | Medio-Alto | Muy Alto | ⭐⭐⭐ |
| 3 | Manejo de Errores Global | Bajo | Alto | ⭐⭐ |
| 4 | Event Bus / Pub-Sub | Medio | Alto | ⭐⭐ |
| 5 | DTOs / Entidades | Medio-Alto | Medio-Alto | ⭐⭐ |
| 6 | Tests de Repositorios | Medio | Alto | ⭐⭐ |
| 7 | Migraciones Formales | Medio | Medio | ⭐⭐ |
| 8 | Optimizar Consultas | Bajo | Alto | ⭐ |
| 9 | Caché | Bajo-Medio | Medio-Alto | ⭐ |
| 10 | Estados de Carga UI | Bajo | Medio | ⭐ |
| 11 | Logging Estructurado | Bajo | Medio | ⭐ |
| 12 | Validación Centralizada | Medio | Alto | ⭐ |
| 13 | Backup Automático | Medio | Muy Alto | ⭐⭐ |
| 14 | Exportación Mejorada | Medio | Medio | ⭐ |
| 15 | Dashboard con Gráficos | Medio | Alto | ⭐⭐ |

---

## 🚀 Roadmap Sugerido

### Fase 1 (Corto Plazo - 2-4 semanas)
- [x] Refactorizar `main.py` para usar nuevos repositorios
- [ ] Implementar manejo de errores global
- [ ] Agregar logging estructurado
- [ ] Optimizar consultas con índices

### Fase 2 (Mediano Plazo - 4-8 semanas)
- [ ] Crear Service Layer para ventas e inventario
- [ ] Implementar Event Bus
- [ ] Agregar tests para todos los repositorios
- [ ] Implementar backup automático

### Fase 3 (Largo Plazo - 8-12 semanas)
- [ ] Migrar todas las pantallas a nuevos repositorios
- [ ] Implementar DTOs/Entidades
- [ ] Agregar migraciones formales de DB
- [ ] Mejorar dashboard con gráficos

---

## 📝 Conclusión

El proyecto tiene una base sólida con buena arquitectura inicial. Las mejoras propuestas siguen mejores prácticas de desarrollo de software y están priorizadas por impacto/esfuerzo. Recomendaría comenzar con las mejoras de bajo esfuerzo y alto impacto (manejo de errores, logging, optimización de consultas) para luego abordar refactorizaciones más grandes.

**Puntos Fuertes Actuales:**
- ✅ Arquitectura de repositorios bien diseñada
- ✅ Tests existentes funcionando
- ✅ Documentación completa
- ✅ Características avanzadas (DIAN, offline sync)

**Áreas de Oportunidad:**
- 🔧 Consistencia en uso de nuevos repositorios
- 🔧 Centralización de lógica de negocio
- 🔧 Mejora en UX (loading states, feedback)
- 🔧 Seguridad de datos (backups)
