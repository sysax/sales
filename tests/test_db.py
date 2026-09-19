"""
Tests para data/db.py - Base de datos SQLite
"""
import pytest
import os
import sqlite3
from datetime import datetime, timedelta
from unittest.mock import patch

# Importar módulo bajo test
from data import db


class TestHashPassword:
    """Tests para funciones de hash de contraseñas"""
    
    def test_hash_password_genera_salt_diferente(self):
        """Mismo password genera hashes diferentes por el salt"""
        hash1 = db._hash_password("test123")
        hash2 = db._hash_password("test123")
        assert hash1 != hash2  # Diferente salt
        assert "$" in hash1  # Formato salt$hash
    
    def test_hash_password_mismo_input_mismo_output_sin_salt(self):
        """Verificar que el hash del password es consistente con mismo salt"""
        # Usamos _verify_password que es lo importante
        pwd = "password123"
        hashed = db._hash_password(pwd)
        assert db._verify_password(hashed, pwd) is True
        assert db._verify_password(hashed, "wrong") is False
    
    def test_verify_password_invalid_format(self):
        """Verificación con formato inválido retorna False"""
        assert db._verify_password("invalid_format", "pwd") is False
        assert db._verify_password("", "pwd") is False
    
    def test_verify_password_plaintext_fallback(self):
        """Fallback para passwords en texto plano (migración)"""
        assert db._verify_password("plaintext", "plaintext") is True
        assert db._verify_password("plaintext", "wrong") is False


class TestDatabaseConnection:
    """Tests para conexión y utilidades de DB"""
    
    def test_get_conn_returns_connection(self):
        """get_conn retorna una conexión SQLite válida"""
        conn = db.get_conn()
        assert isinstance(conn, sqlite3.Connection)
        assert conn.row_factory == sqlite3.Row
        conn.close()
    
    def test_db_path_exists(self):
        """DB_PATH apunta a un archivo en el directorio data"""
        assert "sistema_ventas.db" in db.DB_PATH
        assert os.path.dirname(db.DB_PATH).endswith("data")


class TestCounters:
    """Tests para contadores (facturas, cotizaciones, etc.)"""
    
    @pytest.fixture(autouse=True)
    def setup_counters(self):
        """Inicializar DB limpia para cada test"""
        # Usar DB temporal
        original_path = db.DB_PATH
        temp_db = os.path.join(os.path.dirname(db.DB_PATH), "test_counters.db")
        db.DB_PATH = temp_db
        
        # Inicializar
        if os.path.exists(temp_db):
            os.remove(temp_db)
        db.init_db(seed=False)
        
        yield
        
        # Cleanup
        if os.path.exists(temp_db):
            os.remove(temp_db)
        db.DB_PATH = original_path
    
    def test_get_counter_initial_value(self):
        """Contador no existente retorna 0"""
        val = db.get_counter("NON_EXISTENT")
        assert val == 0
    
    def test_set_and_get_counter(self):
        """Setear y obtener contador"""
        db.set_counter("TEST_COUNTER", 42)
        assert db.get_counter("TEST_COUNTER") == 42
    
    def test_next_counter_increments(self):
        """next_counter incrementa y retorna formato correcto"""
        folio1 = db.next_counter("SALE_COUNTER", "F")
        assert folio1 == "F000"
        
        folio2 = db.next_counter("SALE_COUNTER", "F")
        assert folio2 == "F001"
    
    def test_next_counter_with_width(self):
        """next_counter con width personalizado"""
        folio = db.next_counter("QUOTE_COUNTER", "COT", width=5)
        assert folio == "COT00000"
        
        folio2 = db.next_counter("QUOTE_COUNTER", "COT", width=5)
        assert folio2 == "COT00001"


class TestDatabaseInitialization:
    """Tests para inicialización de base de datos"""
    
    @pytest.fixture(autouse=True)
    def setup_temp_db(self):
        """Crear DB temporal para tests"""
        original_path = db.DB_PATH
        temp_db = os.path.join(os.path.dirname(db.DB_PATH), "test_init.db")
        db.DB_PATH = temp_db
        
        if os.path.exists(temp_db):
            os.remove(temp_db)
        
        yield temp_db
        
        if os.path.exists(temp_db):
            os.remove(temp_db)
        db.DB_PATH = original_path
    
    def test_init_db_creates_tables(self, setup_temp_db):
        """init_db crea todas las tablas necesarias"""
        db.init_db(seed=False)
        temp_db = setup_temp_db
        
        conn = sqlite3.connect(temp_db)
        cur = conn.cursor()
        cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = {row[0] for row in cur.fetchall()}
        conn.close()
        
        expected_tables = {
            'users', 'products', 'clients', 'suppliers', 'sales',
            'sale_items', 'purchases', 'inventory_movements',
            'payables', 'payments_cxc', 'payments_cxp', 'promos',
            'audit_log', 'caja', 'counters', 'outbox',
            'recovery_tokens', 'settings'
        }
        
        assert expected_tables.issubset(tables)
    
    def test_init_db_seeds_data(self, setup_temp_db):
        """init_db con seed=True inserta datos iniciales"""
        db.init_db(seed=True)
        
        conn = db.get_conn()
        cur = conn.cursor()
        
        cur.execute("SELECT COUNT(*) FROM users")
        assert cur.fetchone()[0] > 0
        
        cur.execute("SELECT COUNT(*) FROM products")
        assert cur.fetchone()[0] > 0
        
        cur.execute("SELECT COUNT(*) FROM counters")
        assert cur.fetchone()[0] >= 5  # SALE, QUOTE, ORDER, CREDIT_NOTE, PURCHASE
        
        conn.close()
    
    def test_init_db_idempotent(self, setup_temp_db):
        """Llamar init_db múltiples veces no duplica datos"""
        db.init_db(seed=True)
        db.init_db(seed=True)
        
        conn = db.get_conn()
        cur = conn.cursor()
        
        cur.execute("SELECT COUNT(*) FROM users")
        count1 = cur.fetchone()[0]
        
        db.init_db(seed=True)
        cur.execute("SELECT COUNT(*) FROM users")
        count2 = cur.fetchone()[0]
        
        conn.close()
        
        assert count1 == count2  # No se duplican
    
    def test_settings_default_values(self, setup_temp_db):
        """Settings tiene valores por defecto correctos"""
        db.init_db(seed=False)
        
        conn = db.get_conn()
        cur = conn.cursor()
        
        cur.execute("SELECT value FROM settings WHERE key='dian_enabled'")
        assert cur.fetchone()[0] == '0'
        
        cur.execute("SELECT value FROM settings WHERE key='dian_provider'")
        assert cur.fetchone()[0] == 'simulado'
        
        conn.close()
    
    def test_caja_initialized(self, setup_temp_db):
        """Tabla caja tiene registro inicial"""
        db.init_db(seed=False)
        
        conn = db.get_conn()
        cur = conn.cursor()
        
        cur.execute("SELECT * FROM caja WHERE id=1")
        row = cur.fetchone()
        assert row is not None
        assert row[1] == 0  # closed
        assert row[2] == 0  # opening_amount
        
        conn.close()


class TestUserMigration:
    """Tests para migración de usuarios"""
    
    @pytest.fixture(autouse=True)
    def setup_temp_db(self):
        original_path = db.DB_PATH
        temp_db = os.path.join(os.path.dirname(db.DB_PATH), "test_migration.db")
        db.DB_PATH = temp_db
        
        if os.path.exists(temp_db):
            os.remove(temp_db)
        
        yield temp_db
        
        if os.path.exists(temp_db):
            os.remove(temp_db)
        db.DB_PATH = original_path
    
    def test_migrate_users_adds_columns(self, setup_temp_db):
        """Migración añade columnas faltantes a users"""
        # Crear tabla sin columnas nuevas
        conn = sqlite3.connect(setup_temp_db)
        cur = conn.cursor()
        cur.execute("""CREATE TABLE users (
            username TEXT PRIMARY KEY, 
            password TEXT, 
            role TEXT
        )""")
        cur.execute("INSERT INTO users VALUES ('test', 'plainpwd', 'Admin')")
        conn.commit()
        conn.close()
        
        # Ejecutar migración
        db.init_db(seed=False)
        
        # Verificar columnas añadidas
        conn = db.get_conn()
        cur = conn.cursor()
        cur.execute("PRAGMA table_info(users)")
        cols = {row[1] for row in cur.fetchall()}
        conn.close()
        
        expected_cols = {'active', 'failed_attempts', 'locked_until', 
                        'created_at', 'last_login', 'totp_secret', 
                        'totp_enabled', 'recovery_json'}
        
        assert expected_cols.issubset(cols)
    
    def test_migrate_users_hashes_plaintext(self, setup_temp_db):
        """Migración hashea passwords en texto plano"""
        conn = sqlite3.connect(setup_temp_db)
        cur = conn.cursor()
        cur.execute("""CREATE TABLE users (
            username TEXT PRIMARY KEY, 
            password TEXT, 
            role TEXT
        )""")
        cur.execute("INSERT INTO users VALUES ('test', 'plaintext123', 'Admin')")
        conn.commit()
        conn.close()
        
        db.init_db(seed=False)
        
        conn = db.get_conn()
        cur = conn.cursor()
        cur.execute("SELECT password FROM users WHERE username='test'")
        password = cur.fetchone()[0]
        conn.close()
        
        assert "$" in password  # Ahora está hasheado
        assert "plaintext123" not in password


class TestProductMigration:
    """Tests para migración de productos"""
    
    @pytest.fixture(autouse=True)
    def setup_temp_db(self):
        original_path = db.DB_PATH
        temp_db = os.path.join(os.path.dirname(db.DB_PATH), "test_product_migration.db")
        db.DB_PATH = temp_db
        
        if os.path.exists(temp_db):
            os.remove(temp_db)
        
        yield temp_db
        
        if os.path.exists(temp_db):
            os.remove(temp_db)
        db.DB_PATH = original_path
    
    def test_migrate_products_adds_columns(self, setup_temp_db):
        """Migración añade columnas de imagen, lote, vencimiento, kit"""
        conn = sqlite3.connect(setup_temp_db)
        cur = conn.cursor()
        cur.execute("""CREATE TABLE products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sku TEXT UNIQUE, name TEXT, price REAL, stock INTEGER
        )""")
        conn.commit()
        conn.close()
        
        db.init_db(seed=False)
        
        conn = db.get_conn()
        cur = conn.cursor()
        cur.execute("PRAGMA table_info(products)")
        cols = {row[1] for row in cur.fetchall()}
        conn.close()
        
        expected_cols = {'image', 'lote', 'vencimiento', 'is_kit', 'kit_json'}
        assert expected_cols.issubset(cols)
