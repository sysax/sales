"""
UserRepository — Gestión de usuarios, autenticación y 2FA
Responsabilidad única: manejo de usuarios y seguridad
"""
import json
from datetime import datetime, timedelta
from data import db as sqlite
from data import mock_data as mock
from data.db import _hash_password, _verify_password


class UserRepository:
    """Repositorio especializado en usuarios y autenticación"""
    
    ROLE_PERMISSIONS = {
        "Administrador": {"*"},
        "Vendedor": {"dashboard", "products", "pos", "sales", "clients", "inventory"},
        "Cajero": {"dashboard", "pos", "sales"},
        "Almacén": {"dashboard", "products", "inventory", "purchases", "suppliers"},
        "Contador": {"dashboard", "sales", "receivables", "payables", "reports", "purchases"},
    }

    def __init__(self, audit_callback=None):
        """
        Args:
            audit_callback: Función opcional para logging de auditoría
        """
        self.audit_callback = audit_callback

    def _log(self, user, action, detail=""):
        """Log de auditoría si hay callback"""
        if self.audit_callback:
            self.audit_callback(user, action, detail)

    # ── Consultas de usuarios ──
    def list_users(self):
        """Lista todos los usuarios con información básica"""
        conn = sqlite.get_conn()
        cur = conn.cursor()
        cur.execute(
            "SELECT username, role, active, failed_attempts, locked_until, "
            "created_at, last_login, totp_enabled FROM users ORDER BY username"
        )
        rows = [dict(r) for r in cur.fetchall()]
        conn.close()
        for r in rows:
            r["totp_enabled"] = bool(r.get("totp_enabled", 0))
        return rows

    def find_user(self, username, password):
        """
        Autenticación segura con hash PBKDF2, control de intentos y lockout.
        
        Returns:
            dict con datos del usuario (sin hash) o None si falla
        """
        conn = sqlite.get_conn()
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE username=?", (username,))
        row = cur.fetchone()
        
        if not row:
            conn.close()
            return None
        
        user = self._row_to_dict(row)
        
        # Verificar usuario activo
        if not user.get("active", 1):
            conn.close()
            return None
        
        # Verificar lockout por intentos fallidos
        locked = user.get("locked_until")
        if locked:
            try:
                locked_dt = datetime.fromisoformat(locked)
                if datetime.now() < locked_dt:
                    conn.close()
                    return None
                else:
                    # Lockout expirado, resetear
                    cur.execute(
                        "UPDATE users SET failed_attempts=0, locked_until=NULL WHERE username=?",
                        (username,)
                    )
                    conn.commit()
            except Exception:
                pass
        
        # Verificar contraseña
        stored = row["password"]
        if _verify_password(stored, password):
            cur.execute(
                "UPDATE users SET failed_attempts=0, locked_until=NULL, last_login=? WHERE username=?",
                (datetime.now().isoformat(timespec="seconds"), username)
            )
            conn.commit()
            conn.close()
            user["password"] = "***"  # Ocultar hash
            return user
        else:
            # Incrementar intentos fallidos
            attempts = (user.get("failed_attempts") or 0) + 1
            locked_until = None
            if attempts >= 3:
                locked_until = (datetime.now() + timedelta(minutes=5)).isoformat(timespec="seconds")
            cur.execute(
                "UPDATE users SET failed_attempts=?, locked_until=? WHERE username=?",
                (attempts, locked_until, username)
            )
            conn.commit()
            conn.close()
            return None

    def find_user_by_name(self, username):
        """Obtiene usuario por nombre (sin hash de contraseña)"""
        conn = sqlite.get_conn()
        cur = conn.cursor()
        cur.execute(
            "SELECT username, role, active, failed_attempts, locked_until, "
            "created_at, last_login, totp_enabled FROM users WHERE username=?",
            (username,)
        )
        r = cur.fetchone()
        if r:
            d = dict(r)
            d["active"] = bool(d["active"])
            d["totp_enabled"] = bool(d.get("totp_enabled", 0))
            conn.close()
            return d
        conn.close()
        return None

    def find_user_raw(self, username):
        """Devuelve fila completa para admin (con hash) - uso interno"""
        conn = sqlite.get_conn()
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE username=?", (username,))
        r = self._row_to_dict(cur.fetchone())
        conn.close()
        return r

    # ── CRUD de usuarios ──
    def add_user(self, username, password, role):
        """Crea nuevo usuario con validaciones"""
        if self.find_user_by_name(username):
            raise ValueError("Usuario ya existe")
        if role not in mock.ROLES:
            raise ValueError(f"Rol inválido: {role}")
        if len(password) < 4:
            raise ValueError("Contraseña mínimo 4 caracteres")
        
        conn = sqlite.get_conn()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO users (username, password, role, active, failed_attempts, created_at) "
            "VALUES (?,?,?,?,?,?)",
            (username, _hash_password(password), role, 1, 0, 
             datetime.now().isoformat(timespec="seconds"))
        )
        conn.commit()
        conn.close()
        self._log(username, "alta_usuario", f"rol={role}")

    def update_user(self, username, password=None, role=None):
        """Actualiza contraseña y/o rol de usuario"""
        u = self.find_user_by_name(username)
        if not u:
            raise ValueError("Usuario no encontrado")
        
        conn = sqlite.get_conn()
        cur = conn.cursor()
        
        if password:
            if len(password) < 4:
                conn.close()
                raise ValueError("Contraseña mínimo 4")
            cur.execute(
                "UPDATE users SET password=? WHERE username=?",
                (_hash_password(password), username)
            )
        
        if role:
            if role not in mock.ROLES:
                conn.close()
                raise ValueError(f"Rol inválido: {role}")
            cur.execute(
                "UPDATE users SET role=? WHERE username=?",
                (role, username)
            )
        
        conn.commit()
        conn.close()

    def set_user_active(self, username, active: bool):
        """Activa o bloquea usuario"""
        if username == "admin" and not active:
            raise ValueError("No se puede bloquear admin")
        
        conn = sqlite.get_conn()
        cur = conn.cursor()
        cur.execute(
            "UPDATE users SET active=?, failed_attempts=0, locked_until=NULL WHERE username=?",
            (1 if active else 0, username)
        )
        if cur.rowcount == 0:
            conn.close()
            raise ValueError("Usuario no encontrado")
        conn.commit()
        conn.close()
        self._log("sistema", "usuario_bloqueo" if not active else "usuario_desbloqueo", username)

    def reset_password(self, username, new_password):
        """Resetea contraseña de usuario"""
        if len(new_password) < 4:
            raise ValueError("Contraseña mínimo 4")
        
        conn = sqlite.get_conn()
        cur = conn.cursor()
        cur.execute(
            "UPDATE users SET password=?, failed_attempts=0, locked_until=NULL WHERE username=?",
            (_hash_password(new_password), username)
        )
        if cur.rowcount == 0:
            conn.close()
            raise ValueError("Usuario no encontrado")
        conn.commit()
        conn.close()
        self._log("sistema", "reset_password", username)

    def delete_user(self, username):
        """Elimina usuario (excepto admin)"""
        if username == "admin":
            raise ValueError("No se puede eliminar admin")
        
        conn = sqlite.get_conn()
        cur = conn.cursor()
        cur.execute("DELETE FROM users WHERE username=?", (username,))
        if cur.rowcount == 0:
            conn.close()
            raise ValueError("Usuario no encontrado")
        conn.commit()
        conn.close()

    # ── Permisos ──
    def can_access(self, role, screen_name):
        """Verifica si un rol tiene acceso a una pantalla"""
        perms = self.ROLE_PERMISSIONS.get(role, set())
        return "*" in perms or screen_name in perms

    # ── 2FA TOTP ──
    def is_2fa_enabled(self, username) -> bool:
        """Verifica si 2FA está activado"""
        conn = sqlite.get_conn()
        cur = conn.cursor()
        cur.execute("SELECT totp_enabled FROM users WHERE username=?", (username,))
        r = cur.fetchone()
        conn.close()
        return bool(r and r[0])

    def enable_2fa(self, username):
        """
        Genera secreto TOTP y lo guarda pendiente (enabled=0).
        Returns: secreto para configurar en app authenticator
        """
        from data import totp as t
        u = self.find_user_by_name(username)
        if not u:
            raise ValueError("Usuario no encontrado")
        
        secret = t.generate_secret()
        conn = sqlite.get_conn()
        cur = conn.cursor()
        cur.execute(
            "UPDATE users SET totp_secret=?, totp_enabled=0 WHERE username=?",
            (secret, username)
        )
        conn.commit()
        conn.close()
        self._log("sistema", "2fa_secret", username)
        return secret

    def confirm_2fa(self, username, code):
        """
        Verifica código TOTP contra secreto pendiente y activa 2FA.
        Returns: códigos de recuperación (una vez)
        """
        from data import totp as t
        conn = sqlite.get_conn()
        cur = conn.cursor()
        cur.execute("SELECT totp_secret FROM users WHERE username=?", (username,))
        r = cur.fetchone()
        
        if not r or not r[0]:
            conn.close()
            raise ValueError("Sin secreto 2FA — genere primero")
        
        if not t.verify(r[0], code):
            conn.close()
            raise ValueError("Código 2FA inválido")
        
        codes = t.generate_recovery_codes(8)
        hashed = json.dumps([t.hash_code(c) for c in codes])
        cur.execute(
            "UPDATE users SET totp_enabled=1, recovery_json=? WHERE username=?",
            (hashed, username)
        )
        conn.commit()
        conn.close()
        self._log(username, "2fa_activado", "")
        return codes

    def verify_2fa(self, username, code):
        """
        Verifica código 2FA (acepta TOTP o recovery code de un solo uso).
        Returns: True si válido, False otherwise
        """
        from data import totp as t
        conn = sqlite.get_conn()
        cur = conn.cursor()
        cur.execute(
            "SELECT totp_secret, recovery_json FROM users WHERE username=?",
            (username,)
        )
        r = cur.fetchone()
        
        if not r:
            conn.close()
            return False
        
        secret, rec_json = r[0], r[1]
        
        # Verificar TOTP
        if secret and t.verify(secret, code):
            conn.close()
            return True
        
        # Verificar recovery code
        try:
            hashed = json.loads(rec_json or "[]")
        except Exception:
            hashed = []
        
        h = t.hash_code(code)
        if h in hashed:
            hashed.remove(h)
            cur.execute(
                "UPDATE users SET recovery_json=? WHERE username=?",
                (json.dumps(hashed), username)
            )
            conn.commit()
            conn.close()
            self._log(username, "2fa_recovery_usado", f"quedan {len(hashed)}")
            return True
        
        conn.close()
        return False

    def disable_2fa(self, username):
        """Desactiva 2FA y elimina secretos"""
        conn = sqlite.get_conn()
        cur = conn.cursor()
        cur.execute(
            "UPDATE users SET totp_secret=NULL, totp_enabled=0, recovery_json='[]' WHERE username=?",
            (username,)
        )
        if cur.rowcount == 0:
            conn.close()
            raise ValueError("Usuario no encontrado")
        conn.commit()
        conn.close()
        self._log("sistema", "2fa_desactivado", username)

    def regenerate_recovery_codes(self, username):
        """Regenera códigos de recuperación (requiere 2FA activo)"""
        from data import totp as t
        if not self.is_2fa_enabled(username):
            raise ValueError("2FA no activo para este usuario")
        
        codes = t.generate_recovery_codes(8)
        hashed = json.dumps([t.hash_code(c) for c in codes])
        conn = sqlite.get_conn()
        cur = conn.cursor()
        cur.execute(
            "UPDATE users SET recovery_json=? WHERE username=?",
            (hashed, username)
        )
        conn.commit()
        conn.close()
        self._log(username, "2fa_recovery_regenerado", "")
        return codes

    def recovery_codes_left(self, username) -> int:
        """Retorna cantidad de códigos de recuperación restantes"""
        conn = sqlite.get_conn()
        cur = conn.cursor()
        cur.execute("SELECT recovery_json FROM users WHERE username=?", (username,))
        r = cur.fetchone()
        conn.close()
        try:
            return len(json.loads((r[0] if r else "[]") or "[]"))
        except Exception:
            return 0

    # ── Recuperación de contraseña ──
    def request_recovery(self, username):
        """
        Genera token de recuperación (6 chars, 30 min expiración).
        Sin servidor correo: se muestra en UI y bitácora.
        Returns: (token, expiration)
        """
        import secrets as _s
        u = self.find_user_by_name(username)
        if not u:
            raise ValueError("Usuario no existe")
        
        token = _s.token_hex(3).upper()  # 6 hex chars
        now = datetime.now()
        exp = (now + timedelta(minutes=30)).isoformat(timespec="seconds")
        
        conn = sqlite.get_conn()
        cur = conn.cursor()
        cur.execute(
            "INSERT OR REPLACE INTO recovery_tokens (token, username, created_ts, expires_ts, used) "
            "VALUES (?,?,?,?,0)",
            (token, username, now.isoformat(timespec="seconds"), exp)
        )
        conn.commit()
        conn.close()
        self._log(username, "recovery_solicitado", f"expira {exp}")
        return token, exp

    def redeem_recovery(self, username, token, new_password):
        """Canjea token por nueva contraseña (un solo uso)"""
        if len(new_password) < 4:
            raise ValueError("Contraseña mínimo 4")
        
        conn = sqlite.get_conn()
        cur = conn.cursor()
        cur.execute(
            "SELECT username, expires_ts, used FROM recovery_tokens WHERE token=?",
            (token.strip().upper(),)
        )
        r = cur.fetchone()
        
        if not r:
            conn.close()
            raise ValueError("Token inválido")
        
        if (r[0] or "").lower() != username.strip().lower():
            conn.close()
            raise ValueError("Token no corresponde a este usuario")
        
        if r[2]:
            conn.close()
            raise ValueError("Token ya usado")
        
        cur.execute(
            "SELECT expires_ts FROM recovery_tokens WHERE token=?",
            (token.strip().upper(),)
        )
        try:
            exp = datetime.fromisoformat(cur.fetchone()[0])
        except Exception:
            conn.close()
            raise ValueError("Token expirado")
        
        if datetime.now() > exp:
            conn.close()
            raise ValueError("Token expirado (30 min)")
        
        cur.execute(
            "UPDATE users SET password=?, failed_attempts=0, locked_until=NULL WHERE username=?",
            (_hash_password(new_password), username)
        )
        cur.execute(
            "UPDATE recovery_tokens SET used=1 WHERE token=?",
            (token.strip().upper(),)
        )
        conn.commit()
        conn.close()
        self._log(username, "recovery_completado", "")
        return True

    # ── Helpers ──
    def _row_to_dict(self, row):
        """Convierte fila SQLite a dict con decodificación JSON"""
        if row is None:
            return None
        d = dict(row)
        # Decodificar campos JSON
        if "payments_json" in d and d["payments_json"]:
            try:
                d["payments"] = json.loads(d["payments_json"])
            except Exception:
                d["payments"] = {}
        if "items_json" in d and d["items_json"]:
            try:
                d["items"] = json.loads(d["items_json"])
            except Exception:
                d["items"] = []
        if "sales_today_json" in d and d["sales_today_json"]:
            try:
                d["sales_today"] = json.loads(d["sales_today_json"])
            except Exception:
                d["sales_today"] = []
        # Boolean active
        if "active" in d:
            d["active"] = bool(d["active"])
        return d
