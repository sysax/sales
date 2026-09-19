# Guía de Testing - Sistema de Ventas KivyMD

## 📋 Resumen

Se ha implementado una suite de pruebas con **pytest** para el sistema de ventas con facturación DIAN.

### Archivos Creados

```
tests/
├── __init__.py           # Inicialización del paquete tests
├── test_db.py            # Tests para data/db.py (18 tests)
├── test_dian.py          # Tests para data/dian.py (17 tests)
├── test_repository.py    # Tests para data/repository.py (29 tests)
└── test_totp.py          # Tests para data/totp.py (28 tests)
```

**Total: 92 tests** ✅ Todos pasan

## 🚀 Ejecución de Tests

### Ejecutar todos los tests
```bash
cd /workspace
python -m pytest tests/ -v
```

### Ejecutar con reporte de cobertura
```bash
python -m pytest tests/ --cov=data --cov-report=term-missing
```

### Generar reporte HTML de cobertura
```bash
python -m pytest tests/ --cov=data --cov-report=html
# Abrir: htmlcov/index.html
```

### Ejecutar tests específicos
```bash
# Solo tests de db.py
python -m pytest tests/test_db.py -v

# Solo una clase específica
python -m pytest tests/test_db.py::TestHashPassword -v

# Solo un test específico
python -m pytest tests/test_db.py::TestHashPassword::test_hash_password_genera_salt_diferente -v
```

### Ejecutar tests que fallaron anteriormente
```bash
python -m pytest tests/ --lf
```

### Ejecutar en modo quiet (solo errores)
```bash
python -m pytest tests/ -q
```

## 📊 Cobertura Actual

| Módulo | Stmts | Cover | Missing |
|--------|-------|-------|---------|
| `data/__init__.py` | 0 | 100% | - |
| `data/db.py` | 130 | 98% | 273-274 |
| `data/dian.py` | 58 | 79% | Error handling |
| `data/totp.py` | 42 | 100% | - |
| `data/repository.py` | 1419 | 17% | Métodos no testeables sin UI |
| **TOTAL** | **1649** | **27%** | |

> **Nota:** La baja cobertura de `repository.py` se debe a que muchos métodos requieren interacción con la UI de KivyMD o están diseñados para usarse en contexto de la aplicación completa. Los tests cubren las funcionalidades críticas de autenticación y gestión de usuarios.

## 🧪 Categorías de Tests

### 1. `test_db.py` - Base de Datos (18 tests)
- **HashPassword**: Funciones de hash y verificación de contraseñas
- **DatabaseConnection**: Conexión SQLite
- **Counters**: Contadores de documentos (facturas, cotizaciones)
- **DatabaseInitialization**: Creación de tablas y seed data
- **UserMigration**: Migración de usuarios y passwords
- **ProductMigration**: Migración de productos

### 2. `test_dian.py` - Facturación DIAN (17 tests)
- **DIANSettings**: Configuración en tabla settings
- **DIANEnabled**: Habilitar/deshabilitar DIAN
- **DIANProvider**: Proveedor de facturación
- **GenerateCUFE**: Generación de CUFE simulado
- **AuditLogging**: Logging de cambios
- **Integration**: Flujo completo DIAN

### 3. `test_repository.py` - Repositorio (29 tests)
- **RolePermissions**: Permisos por rol
- **UserAuthentication**: Autenticación, lockout, intentos fallidos
- **UserManagement**: CRUD de usuarios
- **ListUsers**: Listado y filtrado
- **AuditLog**: Logging de auditoría

### 4. `test_totp.py` - 2FA TOTP (28 tests)
- **GenerateSecret**: Generación de secretos Base32
- **CurrentCode**: Generación de códigos TOTP
- **Verify**: Verificación con ventana de tiempo
- **ProvisioningURI**: URI para Google Authenticator
- **RecoveryCodes**: Códigos de recuperación
- **HashCode**: Hash de códigos

## 🔧 Configuración

### `pyproject.toml`
Configuración centralizada para pytest y coverage:
- Paths de tests
- Patrones de archivos/clases/funciones
- Exclusiones de cobertura

### Fixtures
Cada test usa fixtures para:
- Crear DB temporal en `/tmp`
- Seed data controlado
- Cleanup automático post-test

## 📈 Próximos Pasos Sugeridos

1. **Aumentar cobertura de repository.py**
   - Tests para métodos de productos
   - Tests para métodos de ventas
   - Tests para métodos de inventario

2. **Tests de integración**
   - Flujos completos de venta
   - Sync offline → online
   - Generación de reportes

3. **Tests de pantallas (KivyMD)**
   - Usar pytest-kivy o AppTestCase
   - Testear navegación entre screens
   - Testear validaciones de formularios

4. **CI/CD Integration**
   ```yaml
   # .github/workflows/tests.yml
   name: Tests
   on: [push, pull_request]
   jobs:
     test:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v2
         - run: pip install pytest pytest-cov
         - run: pytest tests/ --cov=data --cov-fail-under=30
   ```

5. **Pre-commit hooks**
   ```bash
   # .pre-commit-config.yaml
   repos:
     - repo: local
       hooks:
         - id: pytest
           name: pytest
           entry: pytest tests/ -q
           language: system
           pass_filenames: false
   ```

## ⚠️ Consideraciones Importantes

1. **DB Temporal**: Cada test crea su propia DB en el directorio `data/` con prefijo `test_`. Se elimina automáticamente después de cada test.

2. **Thread Safety**: SQLite se configura con `check_same_thread=False` para permitir tests concurrentes.

3. **Timing**: Algunos tests usan timestamps. Se compara hasta segundos (microsegundos se normalizan).

4. **Seed Data**: Los tests que requieren datos iniciales usan `db.init_db(seed=True)` que carga datos de `mock_data.py`.

## 🎯 Comandos Útiles

```bash
# Ver tests más lentos
python -m pytest tests/ --durations=10

# Parar en el primer fallo
python -m pytest tests/ -x

# Mostrar variables locales en errores
python -m pytest tests/ -l

# Ejecutar en paralelo (requiere pytest-xdist)
python -m pytest tests/ -n auto

# Generar reporte JUnit XML
python -m pytest tests/ --junitxml=test-results.xml
```

---
**Implementado**: Septiembre 2026  
**Versión**: pytest 9.1.1, pytest-cov 7.1.0  
**Python**: 3.12.10
