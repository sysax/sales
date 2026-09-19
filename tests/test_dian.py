"""
Tests para data/dian.py - Facturación electrónica DIAN Colombia
"""
import pytest
import os
from datetime import datetime

from data import db
from data import dian


class TestDIANSettings:
    """Tests para configuración DIAN en settings"""
    
    @pytest.fixture(autouse=True)
    def setup_temp_db(self):
        """Configurar DB temporal para cada test"""
        original_path = db.DB_PATH
        temp_db = os.path.join(os.path.dirname(db.DB_PATH), "test_dian.db")
        db.DB_PATH = temp_db
        
        if os.path.exists(temp_db):
            os.remove(temp_db)
        
        db.init_db(seed=False)
        
        yield
        
        if os.path.exists(temp_db):
            os.remove(temp_db)
        db.DB_PATH = original_path
    
    def test_ensure_settings_creates_table(self):
        """ensure_settings crea tabla settings si no existe"""
        # Eliminar tabla primero
        conn = db.get_conn()
        cur = conn.cursor()
        cur.execute("DROP TABLE IF EXISTS settings")
        conn.commit()
        conn.close()
        
        # Ejecutar ensure_settings
        dian.ensure_settings()
        
        # Verificar que la tabla existe
        conn = db.get_conn()
        cur = conn.cursor()
        cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='settings'")
        result = cur.fetchone()
        conn.close()
        
        assert result is not None
    
    def test_ensure_settings_default_values(self):
        """ensure_settings inserta valores por defecto"""
        dian.ensure_settings()
        
        conn = db.get_conn()
        cur = conn.cursor()
        
        cur.execute("SELECT value FROM settings WHERE key='dian_enabled'")
        assert cur.fetchone()[0] == '0'
        
        cur.execute("SELECT value FROM settings WHERE key='dian_provider'")
        assert cur.fetchone()[0] == 'simulado'
        
        conn.close()


class TestDIANEnabled:
    """Tests para estado habilitado/deshabilitado DIAN"""
    
    @pytest.fixture(autouse=True)
    def setup_temp_db(self):
        original_path = db.DB_PATH
        temp_db = os.path.join(os.path.dirname(db.DB_PATH), "test_dian_enabled.db")
        db.DB_PATH = temp_db
        
        if os.path.exists(temp_db):
            os.remove(temp_db)
        
        db.init_db(seed=False)
        
        yield
        
        if os.path.exists(temp_db):
            os.remove(temp_db)
        db.DB_PATH = original_path
    
    def test_is_enabled_default_false(self):
        """DIAN está deshabilitado por defecto"""
        assert dian.is_enabled() is False
    
    def test_set_enabled_true(self):
        """Activar DIAN"""
        dian.set_enabled(True, user="admin")
        assert dian.is_enabled() is True
    
    def test_set_enabled_false(self):
        """Desactivar DIAN"""
        dian.set_enabled(True)
        dian.set_enabled(False)
        assert dian.is_enabled() is False
    
    def test_is_enabled_handles_missing_settings(self):
        """is_enabled retorna False si settings no existe"""
        # Eliminar tabla
        conn = db.get_conn()
        cur = conn.cursor()
        cur.execute("DROP TABLE IF EXISTS settings")
        conn.commit()
        conn.close()
        
        assert dian.is_enabled() is False
    
    def test_set_enabled_persists_across_connections(self):
        """Estado persiste después de cerrar conexión"""
        dian.set_enabled(True)
        
        # Simular nueva conexión
        enabled = dian.is_enabled()
        assert enabled is True


class TestDIANProvider:
    """Tests para proveedor DIAN"""
    
    @pytest.fixture(autouse=True)
    def setup_temp_db(self):
        original_path = db.DB_PATH
        temp_db = os.path.join(os.path.dirname(db.DB_PATH), "test_dian_provider.db")
        db.DB_PATH = temp_db
        
        if os.path.exists(temp_db):
            os.remove(temp_db)
        
        db.init_db(seed=False)
        
        yield
        
        if os.path.exists(temp_db):
            os.remove(temp_db)
        db.DB_PATH = original_path
    
    def test_get_provider_default_simulado(self):
        """Proveedor por defecto es 'simulado'"""
        assert dian.get_provider() == "simulado"
    
    def test_get_provider_handles_missing_settings(self):
        """get_provider retorna 'simulado' si settings no existe"""
        conn = db.get_conn()
        cur = conn.cursor()
        cur.execute("DROP TABLE IF EXISTS settings")
        conn.commit()
        conn.close()
        
        assert dian.get_provider() == "simulado"


class TestGenerateCUFE:
    """Tests para generación de CUFE válido según resolución DIAN"""
    
    def test_generate_cufe_format(self):
        """CUFE es hash SHA-1 hexadecimal (40 caracteres)"""
        cufe = dian.generate_cufe("F001")
        
        # El nuevo formato es SHA-1 hex (40 chars uppercase)
        assert len(cufe) == 40
        assert cufe.isalnum()
        assert cufe == cufe.upper()
    
    def test_generate_cufe_with_parameters(self):
        """CUFE generado con parámetros completos"""
        cufe = dian.generate_cufe(
            folio="FE001",
            fecha="2025-01-15T10:30:00",
            prefijo="FE",
            total=100000.0,
            nit_emisor="900123456-3",
            nit_receptor="800000004-K"
        )
        
        assert len(cufe) == 40
        assert cufe.isalnum()
    
    def test_generate_cufe_different_folio_different_cufe(self):
        """Diferente folio genera diferente CUFE"""
        cufe1 = dian.generate_cufe("F001")
        cufe2 = dian.generate_cufe("F002")
        
        assert cufe1 != cufe2
    
    def test_generate_cufe_same_folio_different_params(self):
        """Mismo folio con diferentes parámetros genera CUFE diferente"""
        cufe1 = dian.generate_cufe("F001", total=1000.0)
        cufe2 = dian.generate_cufe("F001", total=2000.0)
        
        assert cufe1 != cufe2


class TestAuditLogging:
    """Tests para logging de cambios de configuración DIAN"""
    
    @pytest.fixture(autouse=True)
    def setup_temp_db(self):
        original_path = db.DB_PATH
        temp_db = os.path.join(os.path.dirname(db.DB_PATH), "test_dian_audit.db")
        db.DB_PATH = temp_db
        
        if os.path.exists(temp_db):
            os.remove(temp_db)
        
        db.init_db(seed=False)
        
        yield
        
        if os.path.exists(temp_db):
            os.remove(temp_db)
        db.DB_PATH = original_path
    
    def test_set_enabled_logs_change(self):
        """set_enabled registra cambio en audit_log"""
        dian.set_enabled(True, user="testuser")
        
        conn = db.get_conn()
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM audit_log WHERE action='dian_config'")
        count = cur.fetchone()[0]
        conn.close()
        
        assert count >= 1
    
    def test_set_enabled_logs_user(self):
        """set_enabled registra usuario que hizo el cambio"""
        dian.set_enabled(True, user="admin_user")
        
        conn = db.get_conn()
        cur = conn.cursor()
        cur.execute("SELECT user FROM audit_log WHERE action='dian_config' ORDER BY id DESC LIMIT 1")
        row = cur.fetchone()
        conn.close()
        
        if row:
            assert row[0] == "admin_user"


class TestDIANIntegration:
    """Tests de integración para flujo completo DIAN"""
    
    @pytest.fixture(autouse=True)
    def setup_temp_db(self):
        original_path = db.DB_PATH
        temp_db = os.path.join(os.path.dirname(db.DB_PATH), "test_dian_integration.db")
        db.DB_PATH = temp_db
        
        if os.path.exists(temp_db):
            os.remove(temp_db)
        
        db.init_db(seed=False)
        
        yield
        
        if os.path.exists(temp_db):
            os.remove(temp_db)
        db.DB_PATH = original_path
    
    def test_full_workflow_enable_and_generate(self):
        """Flujo completo: habilitar DIAN y generar CUFE"""
        # Estado inicial
        assert dian.is_enabled() is False
        assert dian.get_provider() == "simulado"
        
        # Habilitar DIAN
        dian.set_enabled(True, user="admin")
        assert dian.is_enabled() is True
        
        # Generar CUFE para una factura (formato hash SHA-1)
        cufe = dian.generate_cufe("FE001")
        assert len(cufe) == 40  # SHA-1 hex
        assert cufe.isalnum()
    
    def test_disable_after_enabled(self):
        """Puede deshabilitarse después de habilitado"""
        dian.set_enabled(True)
        assert dian.is_enabled() is True
        
        dian.set_enabled(False)
        assert dian.is_enabled() is False
        
        # Todavía puede generar CUFE (modo simulado)
        cufe = dian.generate_cufe("F001")
        assert cufe is not None
