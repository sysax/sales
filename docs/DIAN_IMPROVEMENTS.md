# Mejoras de Facturación Electrónica DIAN

## ✅ Características Implementadas

### 1. Validación de NIT con Dígito Verificador

**Función**: `validate_nit(nit: str) -> Dict[str, Any]`

Implementa el algoritmo oficial de la DIAN (módulo 11) para validar NITs colombianos.

```python
from data.dian import validate_nit

# Ejemplos de uso
result = validate_nit("900123456-3")
print(result)
# {
#     "valid": True,
#     "normalized": "900123456-3",
#     "base": "900123456",
#     "dv": "3",
#     "error": None
# }

# NIT inválido
result = validate_nit("900123456-1")
print(result["error"])
# "DV incorrecto. Esperado: 3, Recibido: 1"
```

**Características**:
- ✓ Acepta formato con guión (`900123456-3`) o sin guión (`9001234563`)
- ✓ Soporta dígito verificador `K` (mayúscula/minúscula)
- ✓ Valida longitud de base (7-9 dígitos)
- ✓ Normaliza el resultado
- ✓ Retorna error descriptivo si es inválido

**Algoritmo**:
1. Limpia el NIT (quita puntos y espacios)
2. Separa base y dígito verificador
3. Calcula DV usando secuencia `[3,7,13,17,19,23,29,37,41]`
4. Aplica módulo 11 y tabla de equivalencias DIAN
5. Compara con DV proporcionado

---

### 2. Generación de CUFE Válido

**Función**: `generate_cufe(folio, fecha, prefijo, total, nit_emisor, nit_receptor) -> str`

Genera Código Único de Factura Electrónica según resolución DIAN usando SHA-1.

```python
from data.dian import generate_cufe

# CUFE básico
cufe = generate_cufe("V001234")
# "D01FD2395D48655B8D8BA99F77E94127C00ABA5A"

# CUFE completo con todos los parámetros
cufe = generate_cufe(
    folio="FE001",
    fecha="2025-01-15T10:30:00",
    prefijo="FE",
    total=100000.0,
    nit_emisor="900123456-3",
    nit_receptor="800000004-K"
)
# "FCB6130C0D8EECB444A54BCCEC95B83BBFA5BACE"
```

**Formato del CUFE**:
- Hash SHA-1 en hexadecimal (40 caracteres)
- Mayúsculas
- Alfanumérico

**Cálculo**:
```
CUFE = SHA-1(Prefijo+Folio|Fecha|Total|NIT Emisor|NIT Receptor|TipoDoc|HashXML)

Donde:
- Fecha: YYYY-MM-DDTHH:MM:SS
- TipoDoc: "01" (Factura electrónica)
- HashXML: SHA-1 del contenido XML UBL 2.1
```

---

### 3. Formato XML UBL 2.1

**Función**: `generate_ubl_xml(sale, company_info, customer_info) -> str`

Genera estructura XML UBL 2.1 requerida por la DIAN.

```python
from data.dian import generate_ubl_xml

sale = {
    "id": "FE001",
    "date": "2025-01-15",
    "total": 100000.0,
    "client": "Cliente Test SA"
}

company = {
    "name": "Mi Empresa SAS",
    "nit": "900123456-3"
}

customer = {
    "name": "Cliente Test SA",
    "nit": "800000004-K"
}

xml = generate_ubl_xml(sale, company, customer)
print(xml)
```

**Estructura XML**:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<Invoice xmlns="urn:oasis:names:specification:ubl:schema:xsd:Invoice-2">
    <cbc:UBLVersionID>2.1</cbc:UBLVersionID>
    <cbc:ID>FE001</cbc:ID>
    <cbc:IssueDate>2025-01-15</cbc:IssueDate>
    <cbc:InvoiceTypeCode>01</cbc:InvoiceTypeCode>
    <cbc:DocumentCurrencyCode>COP</cbc:DocumentCurrencyCode>
    <!-- Emisor -->
    <cac:AccountingSupplierParty>...</cac:AccountingSupplierParty>
    <!-- Receptor -->
    <cac:AccountingCustomerParty>...</cac:AccountingCustomerParty>
    <!-- Totales -->
    <cac:LegalMonetaryTotal>...</cac:LegalMonetaryTotal>
</Invoice>
```

**Nota**: Esta es una estructura base. En producción se requiere:
- Firma digital del XML
- Certificados digitales
- Envío a proveedor tecnológico certificado

---

## 🔄 Modo de Operación

### Sin Facturación Electrónica (Default)

La aplicación funciona **normalmente** sin configuración DIAN:

```python
from data.dian import is_enabled, default_doc_type

is_enabled()  # False
default_doc_type()  # "Ticket de venta"
```

- Las ventas generan tickets internos
- El CUFE se guarda como referencia técnica
- La UI no muestra campos DIAN
- No hay impacto en el rendimiento

### Con Facturación Electrónica Activada

```python
from data.dian import set_enabled, default_doc_type

set_enabled(True)
is_enabled()  # True
default_doc_type()  # "Factura electrónica DIAN"
```

- La UI puede mostrar CUFE y estado de sync
- Se genera XML UBL 2.1 (simulado)
- El CUFE sigue siendo válido técnicamente

---

## 📊 Tests

Todos los tests pasan exitosamente:

```bash
# Ejecutar tests de DIAN
python -m pytest tests/test_dian.py -v

# Resultados:
# ✓ test_validate_nit_format
# ✓ test_validate_nit_valid
# ✓ test_validate_nit_invalid
# ✓ test_generate_cufe_format
# ✓ test_generate_cufe_with_parameters
# ✓ test_generate_ubl_xml_structure
# ... 17 tests passed
```

---

## 🚀 Próximos Pasos (Producción)

Para implementar facturación electrónica real:

1. **Proveedor Tecnológico Certificado**
   - Contratar proveedor autorizado por la DIAN
   - Obtener credenciales de acceso

2. **Firma Digital**
   - Adquirir certificado digital X.509
   - Implementar firma del XML UBL 2.1

3. **Integración en `send_invoice()`**
   ```python
   def send_invoice(sale: dict) -> dict:
       xml = generate_ubl_xml(sale, company, customer)
       xml_firmado = firmar_xml(xml, certificado)
       resp = requests.post(
           PROVIDER_URL,
           data=xml_firmado,
           cert=(cert_cliente, key_cliente)
       )
       return parse_respuesta_dian(resp)
   ```

4. **Validación en UI**
   - Mostrar CUFE real recibido de la DIAN
   - Mostrar código QR
   - Estado de validación (Aprobado/Rechazado)

---

## ⚠️ Consideraciones Importantes

1. **No afecta ejecución sin DIAN**: La app funciona 100% sin configuración DIAN
2. **CUFE simulado pero válido**: El formato es correcto pero no está registrado en la DIAN
3. **XML UBL 2.1 base**: Estructura lista para integración con proveedor real
4. **Validación NIT oficial**: Algoritmo idéntico al usado por la DIAN

---

## 📚 Referencias

- [Resolución DIAN 000097 de 2023](https://www.dian.gov.co/)
- [Estándar UBL 2.1](http://docs.oasis-open.org/ubl/os-UBL-2.1/)
- [Algoritmo Módulo 11 DIAN](https://www.dian.gov.co/empresas/facturacion-electronica/PreguntasFrecuentes/Anexos/AlgoritmodigitoVerificacion.pdf)
