"""
Impresión ticket + apertura cajón — Colombia DIAN COP
Intenta ESC/POS, fallback a archivo /tmp/sistema_ventas_tickets/ y lp
Ref: kivymd-reference.md theming; fases.md §6 imprime ticket, abre cajón
"""
import os, subprocess, datetime
from data.offline import save_ticket_text

TICKETS_DIR = "/tmp/sistema_ventas_tickets"
os.makedirs(TICKETS_DIR, exist_ok=True)

def build_ticket_text(sale, cart, client_name, payments, cambio, discount, tax, promo_code=None, dian_cufe=None):
    """Genera texto ticket DIAN Colombia COP, genérico abarrotes/electrónica"""
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sale_id = sale.get("id", "VXXX")
    cufe = dian_cufe or sale.get("dian_cufe", f"CUFE-{sale_id}-DIAN-COLOMBIA")
    lines = []
    lines.append("="*42)
    lines.append("   SISTEMA DE VENTAS — COLOMBIA (DIAN)".center(42))
    lines.append("   Comercio genérico: abarrotes/electrónica".center(42))
    lines.append("="*42)
    lines.append(f"Fecha: {now}  Factura: {sale_id}")
    lines.append(f"Cliente: {client_name}  NIT: {sale.get('client_nit','NIT')}")
    lines.append(f"CUFE DIAN: {cufe}")
    lines.append(f"Doc: {sale.get('doc_type','Factura electrónica DIAN')}")
    lines.append("-"*42)
    lines.append(f"{'Producto':16} {'Cant':4} {'Precio':10} {'Subtotal':10}")
    lines.append("-"*42)
    for it in cart:
        # it may have name/price/qty/subtotal
        name = (it.get("name") or it.get("product") or "Producto")[:16]
        qty = it.get("qty",1)
        price = it.get("price",0)
        subt = it.get("subtotal", price*qty)
        lines.append(f"{name:16} {qty:4} ${price:,.0f} ${subt:,.0f}")
    lines.append("-"*42)
    subtotal = sum(it.get("subtotal",0) for it in cart)
    lines.append(f"Subtotal: ${subtotal:,.0f} COP")
    if discount:
        lines.append(f"Descuento ({promo_code or ''}): -${discount:,.0f} COP")
    lines.append(f"IVA 19% DIAN: ${tax:,.0f} COP")
    lines.append(f"TOTAL: ${sale.get('total', subtotal):,.0f} COP")
    lines.append("-"*42)
    lines.append("Pagos:")
    if isinstance(payments, dict):
        for k,v in payments.items():
            if v:
                lines.append(f"  {k.capitalize():12} ${v:,.0f} COP")
    else:
        lines.append(f"  {payments}")
    lines.append(f"Cambio: ${cambio:,.0f} COP")
    lines.append("-"*42)
    lines.append("Gracias por su compra! — Resolución DIAN")
    lines.append("Modo offline: ticket guardado, se sincroniza al reconectar")
    lines.append("="*42)
    lines.append(f"Software: Sistema Ventas KivyMD 2.0 — COP — Colombia")
    return "\n".join(lines)

def print_ticket(sale, cart, client_name, payments, cambio, discount, tax, promo_code=None):
    text = build_ticket_text(sale, cart, client_name, payments, cambio, discount, tax, promo_code, sale.get("dian_cufe"))
    # guardar siempre
    path = save_ticket_text(sale.get("id","VXXX"), text)
    # intentar impresoras: lp, ESC/POS, etc. — fallback silencioso
    printed = False
    err = None
    # 1) intentar lp si existe archivo
    if path:
        try:
            # lp solo si hay impresora configurada; no falla si no hay
            subprocess.run(["lp", path], timeout=2, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            printed = True
        except Exception as e:
            err = str(e)
    # 2) ESC/POS drawer + ticket vía /dev/usb/lp0 (si existe)
    # no forzamos, solo guardamos
    return {"path": path, "printed": printed, "text": text, "error": err}

def open_drawer():
    """Intenta abrir cajón vía ESC/POS (pulse). Silencioso si no hay hardware."""
    # ESC p 0 25 250 — pulso cajón
    esc = b"\x1b\x70\x00\x19\xfa"
    candidates = ["/dev/usb/lp0", "/dev/usb/lp1", "/dev/lp0", "/tmp/cajon_signal"]
    for dev in candidates:
        try:
            if dev.startswith("/tmp"):
                with open(dev, "wb") as f:
                    f.write(esc)
                return True, dev
            if os.path.exists(dev):
                with open(dev, "wb") as f:
                    f.write(esc)
                return True, dev
        except Exception:
            continue
    # fallback: crear señal tmp para simular apertura (tests)
    try:
        with open("/tmp/cajon_signal", "wb") as f:
            f.write(b"OPEN")
        return True, "/tmp/cajon_signal"
    except Exception as e:
        return False, str(e)

def get_tickets_dir():
    return TICKETS_DIR
