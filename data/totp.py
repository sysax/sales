"""TOTP RFC 6238 sin dependencias (stdlib): secretos, códigos 6 dígitos, ventana ±1.

Compatible con Google Authenticator / Authy: el usuario escanea o escribe
el secreto Base32 manualmente. Paso 30s, SHA1, 6 dígitos.
"""
import base64
import hashlib
import hmac
import secrets
import struct
import time


def generate_secret(length_bytes=20) -> str:
    return base64.b32encode(secrets.token_bytes(length_bytes)).decode().rstrip("=")


def _code(secret: str, counter: int, digits=6) -> str:
    try:
        padded = secret.upper() + "=" * (-len(secret) % 8)
        key = base64.b32decode(padded)
    except Exception:
        return ""
    msg = struct.pack(">Q", counter)
    digest = hmac.new(key, msg, hashlib.sha1).digest()
    offset = digest[-1] & 0x0F
    num = struct.unpack(">I", digest[offset:offset + 4])[0] & 0x7FFFFFFF
    return str(num % (10 ** digits)).zfill(digits)


def current_code(secret: str, for_time=None) -> str:
    t = for_time if for_time is not None else time.time()
    return _code(secret, int(t // 30))


def verify(secret: str, code: str, window=1, for_time=None) -> bool:
    """Acepta code si coincide en ventana ±window pasos (default ±30s)."""
    code = (code or "").strip().replace(" ", "")
    if not code.isdigit() or len(code) != 6:
        return False
    t = for_time if for_time is not None else time.time()
    base = int(t // 30)
    for delta in range(-window, window + 1):
        if hmac.compare_digest(_code(secret, base + delta), code):
            return True
    return False


def provisioning_uri(secret: str, account: str, issuer="SistemaVentas") -> str:
    return f"otpauth://totp/{issuer}:{account}?secret={secret}&issuer={issuer}&digits=6&period=30"


def generate_recovery_codes(n=8) -> list:
    """Códigos de un solo uso formato XXXX-XXXX (mayús)."""
    out = []
    for _ in range(n):
        raw = secrets.token_hex(4).upper()
        out.append(f"{raw[:4]}-{raw[4:]}")
    return out


def hash_code(code: str) -> str:
    return hashlib.sha256(f"sistema-ventas:{code.strip().upper()}".encode()).hexdigest()
