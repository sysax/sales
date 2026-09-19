#  Módulos Principales

## 1. Gestión de Usuarios y Roles
Controla quién puede hacer qué en el sistema.

| Rol | Permisos típicos |
| :--- | :--- |
| **Administrador** | Todo: configurar, ver reportes, gestionar usuarios |
| **Vendedor** | Crear ventas, ver clientes, consultar stock |
| **Cajero** | Solo procesar cobros |
| **Almacén** | Recibir mercancía, ajustar inventario |
| **Contador** | Ver reportes fiscales, facturación |

**Funcionalidades:**
- Login con autenticación segura
- Control de permisos por módulo
- Bitácora de acciones (quién hizo qué y cuándo)

---

## 2. Catálogo de Productos
La base de datos de todo lo que se vende.

**Campos reales:**
- Código de barras (EAN/UPC)
- SKU interno
- Nombre y descripción
- Categoría y subcategoría
- Marca y proveedor
- Precio de compra, precio de venta, precio mayoreo
- Impuestos aplicables (IVA, IEPS)
- Unidad de medida (pieza, kg, litro)
- Stock mínimo, stock máximo, stock actual
- Ubicación en almacén (pasillo, estante)
- Imagen del producto
- Estado (activo, descontinuado, agotado)

**Funcionalidades:**
- Alta, baja y modificación (ABM)
- Importación masiva desde Excel/CSV
- Códigos de barras (generar e imprimir)
- Control de lotes y fechas de caducidad
- Productos compuestos (kits)

---

## 3. Gestión de Clientes (CRM básico)
Información completa de quien compra.

**Datos reales:**
- Datos fiscales (RFC, razón social, régimen fiscal)
- Datos de contacto (teléfono, email, dirección)
- Límite de crédito
- Descuento personalizado
- Historial de compras
- Saldo pendiente
- Lista de precios asignada

**Funcionalidades:**
- Búsqueda rápida por nombre, RFC o teléfono
- Segmentación (mayorista, menudeo, corporativo)
- Programa de lealtad / puntos
- Bloqueo de clientes morosos

---

## 4. Proveedores
Quienes surten la mercancía.

**Datos:**
- Razón social y RFC
- Datos de contacto y representante
- Catálogo de productos que surten
- Tiempos de entrega
- Condiciones de pago
- Historial de compras

---

## 5. Inventario / Almacén ⭐ *(el corazón del sistema)*

**Movimientos reales:**
- **Entradas:** compras a proveedores, devoluciones de clientes, ajustes
- **Salidas:** ventas, devoluciones a proveedor, merma, robos, ajustes
- **Transferencias:** entre sucursales o almacenes

**Conceptos clave:**
- Stock físico vs stock en sistema (siempre deben coincidir)
- Inventario valorizado (cuánto vale lo que tengo en almacén)
- Métodos de valuación: PEPS (primeras en entrar, primeras en salir), Promedio, Costo específico
- Inventario cíclico: conteos parciales programados
- Alertas: stock bajo, por caducar, exceso de stock

**Funcionalidades:**
- Escáner de código de barras para entradas/salidas
- Órdenes de compra
- Recepción de mercancía
- Ajustes de inventario con justificación
- Reportes de rotación (qué se vende rápido y qué no)

---

## 6. Punto de Venta (POS) ⭐ *(donde ocurre la magia)*

**Flujo típico en caja:**
1. Cajero inicia sesión en la caja
2. Escanea o teclea productos
3. Sistema calcula subtotal, impuestos, total
4. Aplica descuentos (por producto, por cliente, promociones)
5. Selecciona método de pago (efectivo, tarjeta, transferencia, mixto)
6. Calcula cambio si es en efectivo
7. Imprime ticket
8. Abre cajón de dinero
9. Registra en sistema y actualiza inventario

**Funcionalidades avanzadas:**
- Ventas a crédito (abonos parciales)
- Apartados / reservaciones
- Devoluciones y cancelaciones
- Facturación electrónica (CFDI en México)
- Cortes de caja (apertura y cierre)
- Modo offline (si se cae internet)
- Múltiples formas de pago en una misma venta

---

## 7. Ventas y Facturación
Registro formal de todas las operaciones.

**Tipos de documentos:**
- **Cotización** (propuesta de precio, no compromete inventario)
- **Pedido** (confirmación del cliente)
- **Remisión** (documento de entrega)
- **Factura** (documento fiscal)
- **Nota de crédito** (devolución)
- **Nota de cargo** (ajustes)

**Estados de una venta:**
1. Cotización
2. Pedido
3. Facturada
4. Pagada
5. Entregada
6. Cerrada / Cancelada

---

## 8. Cuentas por Cobrar (CxC)
Dinero que los clientes deben.

**Funcionalidades:**
- Saldos por cliente
- Anticipos y abonos
- Estados de cuenta
- Recordatorios de vencimiento
- Historial de pagos
- Intereses moratorios

---

## 9. Cuentas por Pagar (CxP)
Dinero que se debe a proveedores.

**Funcionalidades:**
- Facturas pendientes de pago
- Programación de pagos
- Pagos parciales
- Descuentos por pronto pago

---

## 10. Reportes e Inteligencia de Negocio 

**Reportes operativos:**
- Ventas del día/semana/mes/año
- Productos más vendidos (top 10)
- Productos menos vendidos
- Clientes que más compran
- Vendedores más productivos
- Margen de ganancia por producto
- Ticket promedio

**Reportes financieros:**
- Estado de resultados
- Flujo de efectivo
- Valor del inventario
- Cuentas por cobrar y por pagar
- Impuestos generados

**Indicadores clave (KPIs):**
- Rotación de inventario
- Días de inventario
- Tasa de conversión
- Margen bruto y neto
- Punto de equilibrio

---

## 11. Compras
Reabastecimiento de mercancía.

**Flujo:**
1. Sistema detecta stock bajo (o usuario lo solicita)
2. Se genera orden de compra
3. Se envía al proveedor
4. Se recibe mercancía (se valida contra la orden)
5. Se actualiza inventario
6. Se registra la cuenta por pagar

---

## 12. Promociones y Descuentos
Estrategias comerciales.

**Tipos:**
- Descuento por porcentaje
- Descuento por monto fijo
- 2x1, 3x2
- Precio especial por volumen
- Descuentos por cliente específico
- Cupones
- Precios por horario (happy hour)

---

## 🎯 Ejemplo de Flujo Completo Real

**Escenario:** Una tienda de electrónicos

1. **Proveedor** "Distribuidora XYZ" vende laptops
2. Se genera **orden de compra** por 20 laptops
3. Llegan al **almacén**, se escanean y entran al **inventario**
4. **Cliente** "Juan Pérez" llega a la tienda
5. **Vendedor** busca el producto, verifica stock
6. Se crea **cotización** por 3 laptops + accesorios
7. Cliente acepta, se convierte en **venta**
8. Se **factura** electrónicamente
9. Cliente paga con **tarjeta** (80%) y **efectivo** (20%)
10. Se **imprime ticket** y se entrega mercancía
11. **Inventario** se descuenta automáticamente (17 laptops quedan)
12. **Corte de caja** al final del día cuadra ingresos
13. **Reporte diario** muestra ventas totales, productos vendidos, etc.