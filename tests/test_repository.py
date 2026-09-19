"""
Tests para data/repository.py - Capa de repositorio
"""
import pytest
import os
import json
from datetime import datetime, timedelta
from unittest.mock import patch

from data import db
from data.repository import Repository, ROLE_PERMISSIONS


class TestRolePermissions:
    """Tests para permisos por rol"""
    
    def test_admin_has_all_permissions(self):
        """Administrador tiene acceso a todo"""
        assert "*" in ROLE_PERMISSIONS["Administrador"]
    
    def test_vendedor_permissions(self):
        """Vendedor tiene permisos limitados"""
        perms = ROLE_PERMISSIONS["Vendedor"]
        assert "pos" in perms
        assert "sales" in perms
        assert "products" in perms
        assert "*" not in perms
    
    def test_cajero_permissions(self):
        """Cajero solo tiene acceso a POS y ventas"""
        perms = ROLE_PERMISSIONS["Cajero"]
        assert "pos" in perms
        assert "sales" in perms
        assert "dashboard" in perms
        assert "inventory" not in perms
        assert "purchases" not in perms
    
    def test_all_roles_defined(self):
        """Todos los roles estándar están definidos"""
        expected_roles = {"Administrador", "Vendedor", "Cajero", "Almacén", "Contador"}
        assert expected_roles.issubset(set(ROLE_PERMISSIONS.keys()))


class TestRepositoryUserAuthentication:
    """Tests para autenticación de usuarios"""
    
    @pytest.fixture(autouse=True)
    def setup_temp_db(self):
        """Configurar DB temporal para cada test"""
        original_path = db.DB_PATH
        temp_db = os.path.join(os.path.dirname(db.DB_PATH), "test_repo.db")
        db.DB_PATH = temp_db
        
        if os.path.exists(temp_db):
            os.remove(temp_db)
        
        db.init_db(seed=True)
        self.repo = Repository()
        
        yield
        
        if os.path.exists(temp_db):
            os.remove(temp_db)
        db.DB_PATH = original_path
    
    def test_find_user_valid_credentials(self):
        """Autenticación con credenciales válidas"""
        user = self.repo.find_user("admin", "admin123")
        assert user is not None
        assert user["username"] == "admin"
        assert user["role"] == "Administrador"
        assert user["password"] == "***"  # No retornar hash
    
    def test_find_user_invalid_password(self):
        """Autenticación falla con password incorrecto"""
        user = self.repo.find_user("admin", "wrongpassword")
        assert user is None
    
    def test_find_user_nonexistent(self):
        """Autenticación falla con usuario inexistente"""
        user = self.repo.find_user("nonexistent", "password")
        assert user is None
    
    def test_find_user_inactive(self):
        """Usuario inactivo no puede autenticarse"""
        # 'vendedor' se crea con seed=True (no 'vendedor1')
        self.repo.set_user_active("vendedor", False)
        user = self.repo.find_user("vendedor", "vend123")
        assert user is None
    
    def test_failed_attempts_increments(self):
        """Intentos fallidos incrementan contador"""
        # Intento fallido
        self.repo.find_user("admin", "wrong1")
        user = self.repo.find_user_by_name("admin")
        assert user["failed_attempts"] >= 1
    
    def test_lockout_after_3_failures(self):
        """Usuario se bloquea después de 3 intentos fallidos"""
        # 3 intentos fallidos - admin existe con seed=True
        for i in range(3):
            self.repo.find_user("admin", f"wrong{i}")
        
        user = self.repo.find_user_by_name("admin")
        assert user is not None
        assert user.get("locked_until") is not None
        
        # Verificar que no puede autenticarse incluso con password correcto
        auth_result = self.repo.find_user("admin", "admin123")
        assert auth_result is None
    
    def test_last_login_updated_on_success(self):
        """last_login se actualiza en autenticación exitosa"""
        before = datetime.now()
        self.repo.find_user("admin", "admin123")
        user = self.repo.find_user_by_name("admin")
        after = datetime.now()
        
        assert user["last_login"] is not None
        last_login_dt = datetime.fromisoformat(user["last_login"])
        # Ajustar para microsegundos - comparar solo hasta segundos
        assert last_login_dt.replace(microsecond=0) >= before.replace(microsecond=0)
        assert last_login_dt.replace(microsecond=0) <= after.replace(microsecond=0)


class TestRepositoryUserManagement:
    """Tests para gestión de usuarios (CRUD)"""
    
    @pytest.fixture(autouse=True)
    def setup_temp_db(self):
        original_path = db.DB_PATH
        temp_db = os.path.join(os.path.dirname(db.DB_PATH), "test_repo_users.db")
        db.DB_PATH = temp_db
        
        if os.path.exists(temp_db):
            os.remove(temp_db)
        
        db.init_db(seed=False)
        self.repo = Repository()
        
        yield
        
        if os.path.exists(temp_db):
            os.remove(temp_db)
        db.DB_PATH = original_path
    
    def test_add_user_success(self):
        """Añadir usuario exitosamente"""
        self.repo.add_user("testuser", "pass123", "Vendedor")
        user = self.repo.find_user_by_name("testuser")
        
        assert user is not None
        assert user["username"] == "testuser"
        assert user["role"] == "Vendedor"
        assert user["active"] is True
    
    def test_add_user_duplicate(self):
        """Añadir usuario duplicado lanza error"""
        self.repo.add_user("testuser", "pass123", "Vendedor")
        
        with pytest.raises(ValueError, match="ya existe"):
            self.repo.add_user("testuser", "pass456", "Cajero")
    
    def test_add_user_invalid_role(self):
        """Añadir usuario con rol inválido lanza error"""
        with pytest.raises(ValueError, match="Rol inválido"):
            self.repo.add_user("testuser", "pass123", "RolInvalido")
    
    def test_add_user_short_password(self):
        """Contraseña muy corta lanza error"""
        with pytest.raises(ValueError, match="mínimo 4"):
            self.repo.add_user("testuser", "123", "Vendedor")
    
    def test_update_user_password(self):
        """Actualizar contraseña de usuario"""
        self.repo.add_user("testuser", "oldpass", "Vendedor")
        self.repo.update_user("testuser", password="newpass")
        
        # Verificar que puede autenticarse con nueva contraseña
        user = self.repo.find_user("testuser", "newpass")
        assert user is not None
        
        # Verificar que old password ya no funciona
        user_old = self.repo.find_user("testuser", "oldpass")
        assert user_old is None
    
    def test_update_user_role(self):
        """Actualizar rol de usuario"""
        self.repo.add_user("testuser", "pass123", "Vendedor")
        self.repo.update_user("testuser", role="Cajero")
        
        user = self.repo.find_user_by_name("testuser")
        assert user["role"] == "Cajero"
    
    def test_set_user_active_deactivate(self):
        """Desactivar usuario"""
        self.repo.add_user("testuser", "pass123", "Vendedor")
        self.repo.set_user_active("testuser", False)
        
        user = self.repo.find_user_by_name("testuser")
        assert user["active"] is False
    
    def test_set_user_active_reactivate(self):
        """Reactivar usuario"""
        self.repo.add_user("testuser", "pass123", "Vendedor")
        self.repo.set_user_active("testuser", False)
        self.repo.set_user_active("testuser", True)
        
        user = self.repo.find_user_by_name("testuser")
        assert user["active"] is True
        assert user["failed_attempts"] == 0  # Resetear intentos
        assert user["locked_until"] is None  # Quitar bloqueo
    
    def test_cannot_deactivate_admin(self):
        """No se puede desactivar usuario admin"""
        db.init_db(seed=True)  # Crear admin
        
        with pytest.raises(ValueError, match="No se puede bloquear admin"):
            self.repo.set_user_active("admin", False)
    
    def test_delete_user_success(self):
        """Eliminar usuario exitosamente"""
        self.repo.add_user("testuser", "pass123", "Vendedor")
        self.repo.delete_user("testuser")
        
        user = self.repo.find_user_by_name("testuser")
        assert user is None
    
    def test_cannot_delete_admin(self):
        """No se puede eliminar usuario admin"""
        db.init_db(seed=True)
        
        with pytest.raises(ValueError, match="No se puede eliminar admin"):
            self.repo.delete_user("admin")
    
    def test_reset_password(self):
        """Resetear contraseña de usuario"""
        self.repo.add_user("testuser", "oldpass", "Vendedor")
        self.repo.reset_password("testuser", "newpass")
        
        user = self.repo.find_user("testuser", "newpass")
        assert user is not None


class TestRepositoryListUsers:
    """Tests para listar usuarios"""
    
    @pytest.fixture(autouse=True)
    def setup_temp_db(self):
        original_path = db.DB_PATH
        temp_db = os.path.join(os.path.dirname(db.DB_PATH), "test_list_users.db")
        db.DB_PATH = temp_db
        
        if os.path.exists(temp_db):
            os.remove(temp_db)
        
        db.init_db(seed=False)
        self.repo = Repository()
        
        # Crear algunos usuarios de prueba
        self.repo.add_user("user1", "pass123", "Vendedor")
        self.repo.add_user("user2", "pass456", "Cajero")
        self.repo.add_user("user3", "pass789", "Almacén")
        
        yield
        
        if os.path.exists(temp_db):
            os.remove(temp_db)
        db.DB_PATH = original_path
    
    def test_list_users_returns_all(self):
        """list_users retorna todos los usuarios"""
        users = self.repo.list_users()
        assert len(users) == 3
    
    def test_list_users_sorted_by_username(self):
        """Usuarios ordenados alfabéticamente"""
        users = self.repo.list_users()
        usernames = [u["username"] for u in users]
        assert usernames == sorted(usernames)
    
    def test_list_users_excludes_password(self):
        """list_users no incluye password hash"""
        users = self.repo.list_users()
        for user in users:
            assert "password" not in user or user.get("password") == "***"
    
    def test_list_users_includes_totp_enabled(self):
        """list_users incluye estado de 2FA"""
        users = self.repo.list_users()
        for user in users:
            assert "totp_enabled" in user
            assert isinstance(user["totp_enabled"], bool)


class TestRepositoryAuditLog:
    """Tests para logging de auditoría"""
    
    @pytest.fixture(autouse=True)
    def setup_temp_db(self):
        original_path = db.DB_PATH
        temp_db = os.path.join(os.path.dirname(db.DB_PATH), "test_audit.db")
        db.DB_PATH = temp_db
        
        if os.path.exists(temp_db):
            os.remove(temp_db)
        
        db.init_db(seed=False)
        self.repo = Repository()
        self.repo.add_user("testuser", "pass123", "Vendedor")
        
        yield
        
        if os.path.exists(temp_db):
            os.remove(temp_db)
        db.DB_PATH = original_path
    
    def test_log_creates_entry(self):
        """log crea entrada en audit_log"""
        self.repo.log("testuser", "accion_test", "detalle")
        
        conn = db.get_conn()
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM audit_log WHERE action='accion_test' AND user='testuser'")
        count = cur.fetchone()[0]
        conn.close()
        
        assert count >= 1
    
    def test_log_contains_correct_data(self):
        """Entrada de log contiene datos correctos"""
        timestamp_before = datetime.now()
        self.repo.log("testuser", "accion_test_unique", "detalle_prueba")
        timestamp_after = datetime.now()
        
        conn = db.get_conn()
        cur = conn.cursor()
        cur.execute("SELECT * FROM audit_log WHERE action='accion_test_unique' ORDER BY id DESC LIMIT 1")
        row = dict(cur.fetchone())
        conn.close()
        
        assert row["user"] == "testuser"
        assert row["action"] == "accion_test_unique"
        assert row["detail"] == "detalle_prueba"
        
        ts = datetime.fromisoformat(row["ts"])
        # Comparar solo hasta segundos (ignorar microsegundos)
        assert ts.replace(microsecond=0) >= timestamp_before.replace(microsecond=0)
        assert ts.replace(microsecond=0) <= timestamp_after.replace(microsecond=0)
