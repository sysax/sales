# Mejoras de Sincronización Offline

## 📋 Resumen de Mejoras Implementadas

Se ha mejorado significativamente la estrategia de sincronización offline con las siguientes características:

### 🚀 **1. Backoff Exponencial con Jitter**

**Problema anterior:** Reintentos inmediatos que saturaban el servidor al recuperarse la conexión.

**Solución:** Algoritmo de backoff exponencial con jitter aleatorio para evitar el "thundering herd problem".

```python
# Configuración
BASE_DELAY = 1.0s       # Delay inicial
MAX_DELAY = 300.0s      # Delay máximo (5 minutos)
JITTER_FACTOR = 0.2     # 20% aleatoriedad

# Fórmula: min(BASE_DELAY * 2^attempts + jitter, MAX_DELAY)
Intento 0: ~1.0s
Intento 1: ~2.0s
Intento 2: ~4.0s
Intento 3: ~8.0s
Intento 4: ~16.0s
Intento 5: ~32.0s (último reintento)
```

**Beneficios:**
- Evita saturar el servidor al recuperarse la conexión
- Distribuye los reintentos en el tiempo
- Aumenta progresivamente la paciencia con fallos persistentes

---

### ⚔️ **2. Estrategias de Conflict Resolution**

**Problema anterior:** No había detección ni resolución de conflictos entre datos locales y del servidor.

**Solución:** Sistema de detección y resolución de conflictos con 5 estrategias configurables:

```python
class ConflictStrategy(Enum):
    LAST_WRITE_WINS = "last_write_wins"  # El más reciente gana (default)
    MERGE = "merge"                      # Combina cambios de ambos lados
    FAIL = "fail"                        # Reporta para resolución manual
    SERVER_WINS = "server_wins"          # Servidor siempre tiene razón
    LOCAL_WINS = "local_wins"            # Local siempre tiene razón
```

**Detección automática:**
- Compara timestamps de `updated_at` o `created_at`
- Identifica campos en conflicto
- Registra información detallada del conflicto

**Resolución:**
- `LAST_WRITE_WINS`: Compara timestamps, el más reciente prevalece
- `MERGE`: Combina datos, servidor tiene prioridad pero mantiene campos locales únicos
- `SERVER_WINS`/`LOCAL_WINS`: Prioridad fija según configuración
- `FAIL`: Lanza excepción para intervención manual

---

### 🔌 **3. Circuit Breaker**

**Problema anterior:** Intentos infinitos de sync cuando el servidor está caído, desperdiciando recursos.

**Solución:** Patrón Circuit Breaker con 3 estados:

```
┌─────────────┐
│   CLOSED    │ ← Estado normal, operaciones fluyen
└──────┬──────┘
       │ 5 fallos consecutivos
       ▼
┌─────────────┐
│    OPEN     │ ← Operaciones bloqueadas por 60s
└──────┬──────┘
       │ Timeout expira
       ▼
┌─────────────┐
│  HALF-OPEN  │ ← Prueba con una operación
└──────┬──────┘
       ├─ Éxito → CLOSED
       └─ Fallo → OPEN
```

**Configuración:**
- `CIRCUIT_BREAKER_THRESHOLD = 5` fallos para abrir
- `CIRCUIT_BREAKER_TIMEOUT = 60s` antes de probar nuevamente

**Beneficios:**
- Previene colapso del servidor bajo carga
- Ahorra recursos de red y CPU
- Permite recuperación automática gradual

---

### 📦 **4. Sync por Lotes (Batching)**

**Problema anterior:** Procesamiento de una operación a la vez, ineficiente para grandes volúmenes.

**Solución:** Procesamiento por lotes configurables:

```python
BATCH_SIZE = 10  # operaciones por lote (configurable)

# Uso
synced, pending = sync_queue(repo, batch_size=20)
```

**Características:**
- Prioriza operaciones más antiguas (FIFO)
- Procesa en transacciones separadas
- Reporta progreso por lote
- Se detiene si circuit breaker se abre

**Beneficios:**
- Mejor throughput general
- Menos overhead de transacciones
- Progreso visible incluso en lotes grandes

---

### 📊 **5. Métricas Detalladas**

**Problema anterior:** Sin visibilidad del estado de sincronización.

**Solución:** Sistema completo de métricas en tiempo real:

```python
from data.offline import get_sync_metrics

metrics = get_sync_metrics()
# Retorna:
{
    "total_synced": 150,           # Total operaciones exitosas
    "total_failed": 3,             # Total operaciones fallidas
    "total_pending": 5,            # Operaciones pendientes
    "last_sync_time": "2024-...",  # Timestamp último sync
    "consecutive_failures": 0,     # Fallos consecutivos actuales
    "circuit_breaker_open": False, # Estado circuit breaker
    "circuit_breaker_state": "closed",  # closed/open/half-open
    "avg_sync_time_ms": 45.2,      # Tiempo promedio por operación
    "operations_by_type": {        # Desglose por tipo
        "sale": 120,
        "dian": 30
    }
}
```

**Casos de uso:**
- Monitoreo en tiempo real en UI
- Alertas automáticas
- Dashboard administrativo
- Debugging de problemas

---

### 🪵 **6. Logging Estructurado**

**Problema anterior:** Prints dispersos sin contexto ni niveles.

**Solución:** Logging estructurado con niveles y contexto:

```python
import logging
logger = logging.getLogger(__name__)

# Niveles utilizados:
logger.debug("Operación 123 sincronizada en 45.2ms")
logger.info("Iniciando sync de 10 operaciones (lote 10)")
logger.warning("Circuit breaker abierto, sync postponido")
logger.error("Operación 456 falló definitivamente: timeout")
```

**Formato:**
```
2024-01-15 10:30:45 [INFO] data.offline: Iniciando sync de 10 operaciones
2024-01-15 10:30:46 [WARNING] data.offline: Circuit breaker abierto después de 5 fallos
2024-01-15 10:31:46 [INFO] data.offline: Circuit breaker en estado half-open, probando...
```

**Beneficios:**
- Filtrado por nivel (DEBUG/INFO/WARNING/ERROR)
- Timestamp preciso para debugging
- Contexto claro en cada mensaje
- Integración con sistemas de logging externos

---

### 🎯 **7. Detección Inteligente de Errores**

**Problema anterior:** Todos los errores se trataban igual, reintentando innecesariamente.

**Solución:** Clasificación de errores reintentables vs no reintentables:

```python
# Errores NO reintentables (fallan inmediatamente)
non_retryable_errors = [
    "folio no existe",        # Datos corruptos o DB reseteada
    "datos inválidos",        # Error de validación permanente
    "violación de restricción" # Error de integridad
]

# Errores SÍ reintentables
retryable_errors = [
    "timeout",                # Transitorio
    "connection reset",       # Transitorio
    "service unavailable",    # Transitorio
    "rate limit"              # Temporal
]
```

**Lógica:**
```python
if error in non_retryable_errors:
    status = "failed"  # Falla inmediata, sin reintentos
else:
    status = "pending"  # Reintenta con backoff
```

---

### 🔄 **8. Cola de Reintentos con Prioridad**

**Mejoras en la tabla `outbox`:**

```sql
CREATE TABLE outbox (
    id INTEGER PRIMARY KEY,
    created_ts TEXT,
    op_type TEXT,
    idempotency_key TEXT UNIQUE,
    payload_json TEXT,
    status TEXT DEFAULT 'pending',      -- pending/synced/failed
    attempts INTEGER DEFAULT 0,         # Intentos realizados
    last_error TEXT,                    # Último error encontrado
    next_retry_at TEXT,                 # PRÓXIMO REINTENTO (nuevo!)
    synced_ts TEXT
);
```

**Priorización:**
```sql
SELECT * FROM outbox 
WHERE status='pending' 
ORDER BY created_ts ASC, id ASC 
LIMIT 10;
```

**Próximo reintento calculado:**
```python
next_retry_at = now() + calculate_backoff(attempts)
```

---

## 📈 Comparativa Antes/Después

| Característica | Antes | Después |
|---------------|-------|---------|
| **Reintentos** | Inmediatos, sin delay | Backoff exponencial + jitter |
| **Conflictos** | No detectados | 5 estrategias de resolución |
| **Fallos masivos** | Intentos infinitos | Circuit breaker automático |
| **Performance** | 1 operación a la vez | Lotes de 10+ operaciones |
| **Métricas** | Ninguna | 10+ métricas en tiempo real |
| **Logging** | Prints dispersos | Logging estructurado |
| **Errores** | Todos iguales | Clasificación inteligente |
| **Visibilidad** | Limitada | Completa con métricas |

---

## 🧪 Ejemplos de Uso

### Ejemplo 1: Sync Manual con Métricas

```python
from data.offline import sync_queue, get_sync_metrics
from data.repositories import SaleRepository

repo = SaleRepository()

# Ejecutar sync
synced, pending = sync_queue(repo, batch_size=20)
print(f"Sincronizadas: {synced}, Pendientes: {pending}")

# Ver métricas
metrics = get_sync_metrics()
print(f"Éxito: {metrics['total_synced']}")
print(f"Fallidas: {metrics['total_failed']}")
print(f"Circuit breaker: {metrics['circuit_breaker_state']}")
```

### Ejemplo 2: Monitoreo en UI KivyMD

```python
from kivy.clock import Clock
from data.offline import get_sync_metrics, is_online

def update_sync_status(dt):
    metrics = get_sync_metrics()
    
    if metrics['circuit_breaker_open']:
        label_sync.text = "⚠️ Servidor no disponible"
        label_sync.color = (1, 0, 0, 1)  # Rojo
    elif metrics['total_pending'] > 0:
        label_sync.text = f"🔄 Sincronizando... ({metrics['total_pending']} pendientes)"
        label_sync.color = (1, 1, 0, 1)  # Amarillo
    elif is_online():
        label_sync.text = "✅ Sincronizado"
        label_sync.color = (0, 1, 0, 1)  # Verde
    else:
        label_sync.text = "📴 Offline"
        label_sync.color = (0.5, 0.5, 0.5, 1)  # Gris

# Actualizar cada 5 segundos
Clock.schedule_interval(update_sync_status, 5)
```

### Ejemplo 3: Reset de Métricas para Testing

```python
from data.offline import reset_metrics, queue_operation

# Limpiar métricas anteriores
reset_metrics()

# Simular operaciones
queue_operation("sale", {"folio": "123"}, "sale-123")
queue_operation("sale", {"folio": "124"}, "sale-124")

# Verificar que métricas están limpias
metrics = get_sync_metrics()
assert metrics['total_synced'] == 0
assert metrics['total_failed'] == 0
```

---

## 🔧 Configuración Avanzada

Todos los parámetros son configurables al inicio del módulo:

```python
# offline.py - Sección de configuración

MAX_ATTEMPTS = 5                  # Máximos intentos antes de fallar
BASE_DELAY = 1.0                  # Delay inicial en segundos
MAX_DELAY = 300.0                 # Delay máximo (5 minutos)
JITTER_FACTOR = 0.2               # 20% variación aleatoria
BATCH_SIZE = 10                   # Operaciones por lote
SYNC_TIMEOUT = 30                 # Timeout para sync remoto
CIRCUIT_BREAKER_THRESHOLD = 5     # Fallos para activar circuit breaker
CIRCUIT_BREAKER_TIMEOUT = 60      # Segundos que permanece abierto
```

**Ajustes recomendados por escenario:**

| Escenario | BATCH_SIZE | BASE_DELAY | CIRCUIT_BREAKER_THRESHOLD |
|-----------|-----------|------------|--------------------------|
| **LAN rápida** | 50 | 0.5 | 10 |
| **WiFi público** | 10 | 2.0 | 5 |
| **3G/4G inestable** | 5 | 5.0 | 3 |
| **Servidor lento** | 5 | 10.0 | 5 |

---

## 🎯 Próximas Mejoras Sugeridas

1. **Scheduler de reintentos:** Programar reintentos exactos usando `next_retry_at`
2. **Sync bidireccional:** Resolver conflictos con datos reales del servidor
3. **Compresión de payloads:** Reducir tamaño de operaciones en cola
4. **Prioridad por tipo:** Ventas > Inventarios > Auditoría
5. **Webhooks:** Notificar cambios en tiempo real al servidor
6. **Analytics:** Historial de métricas para tendencias

---

## ✅ Tests de Verificación

Ejecutar tests para verificar implementación:

```bash
# Verificar que el módulo importa correctamente
python -c "from data.offline import sync_queue, get_sync_metrics; print('✓ OK')"

# Verificar backoff exponencial
python -c "from data.offline import _calculate_backoff; print(_calculate_backoff(3))"

# Verificar estrategias de conflicto
python -c "from data.offline import ConflictStrategy; print(list(ConflictStrategy))"

# Verificar métricas
python -c "from data.offline import get_sync_metrics; print(get_sync_metrics())"

# Ejecutar todos los tests existentes
python -m pytest tests/ -v
```

---

## 📚 Referencias

- **Backoff Exponencial:** https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/
- **Circuit Breaker Pattern:** https://martinfowler.com/bliki/CircuitBreaker.html
- **Conflict Resolution:** https://en.wikipedia.org/wiki/Conflict_resolution_(computing)
- **Offline-First Architecture:** https://offlinefirst.org/
