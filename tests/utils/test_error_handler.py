"""
Tests para el manejador de errores - Colombia
"""
import pytest
from utils.error_handler import (
    handle_errors, 
    BusinessValidationError, 
    DatabaseError,
    AuthenticationError,
    PermissionDeniedError,
    log_operation
)


class MockScreen:
    """Mock de pantalla con método _snack"""
    def __init__(self):
        self.snack_messages = []
    
    def _snack(self, msg):
        self.snack_messages.append(msg)


class TestHandleErrors:
    
    def test_success_no_error(self):
        """Test que función exitosa retorna valor correcto"""
        
        @handle_errors(default_return=None)
        def successful_func():
            return "success"
        
        result = successful_func()
        assert result == "success"
    
    def test_business_validation_error(self):
        """Test manejo de error de validación de negocio"""
        
        screen = MockScreen()
        
        @handle_errors(default_return=[])
        def validation_func(obj):
            raise BusinessValidationError("Datos inválidos")
        
        result = validation_func(screen)
        assert result == []
        assert "Datos inválidos" in screen.snack_messages
    
    def test_database_error(self):
        """Test manejo de error de base de datos"""
        
        screen = MockScreen()
        
        @handle_errors(default_return=None)
        def db_func(obj):
            raise DatabaseError("Error de conexión")
        
        result = db_func(screen)
        assert result is None
        assert any("base de datos" in msg.lower() for msg in screen.snack_messages)
    
    def test_authentication_error(self):
        """Test manejo de error de autenticación"""
        
        screen = MockScreen()
        
        @handle_errors(default_return=None)
        def auth_func(obj):
            raise AuthenticationError("Credenciales inválidas")
        
        result = auth_func(screen)
        assert result is None
        assert any("autenticación" in msg.lower() for msg in screen.snack_messages)
    
    def test_permission_denied_error(self):
        """Test manejo de error de permisos"""
        
        screen = MockScreen()
        
        @handle_errors(default_return=False)
        def permission_func(obj):
            raise PermissionDeniedError("Acceso denegado")
        
        result = permission_func(screen)
        assert result is False
        assert any("denegado" in msg.lower() for msg in screen.snack_messages)
    
    def test_generic_exception(self):
        """Test manejo de excepción genérica"""
        
        screen = MockScreen()
        
        @handle_errors(default_return=None)
        def generic_func(obj):
            raise ValueError("Error inesperado")
        
        result = generic_func(screen)
        assert result is None
        assert any("error interno" in msg.lower() for msg in screen.snack_messages)
    
    def test_default_return_with_list(self):
        """Test que retorna lista vacía como default"""
        
        @handle_errors(default_return=[])
        def list_func():
            raise Exception("Error")
        
        result = list_func()
        assert result == []
        assert isinstance(result, list)
    
    def test_disable_user_error_message(self):
        """Test que puede desactivar mensajes al usuario"""
        
        screen = MockScreen()
        
        @handle_errors(default_return=None, show_user_error=False)
        def silent_func(obj):
            raise Exception("Error silencioso")
        
        result = silent_func(screen)
        assert result is None
        assert len(screen.snack_messages) == 0


class TestLogOperation:
    
    def test_log_operation_success(self, caplog):
        """Test que operación exitosa es loggeada"""
        
        @log_operation("test_operation")
        def successful_op():
            return "ok"
        
        with caplog.at_level("INFO"):
            result = successful_op()
            
        assert result == "ok"
        assert "Iniciando operación: test_operation" in caplog.text
        assert "Completada operación: test_operation - Éxito" in caplog.text
    
    def test_log_operation_failure(self, caplog):
        """Test que operación fallida es loggeada"""
        
        @log_operation("failing_operation")
        def failing_op():
            raise Exception("Error intencional")
        
        with caplog.at_level("INFO"):
            with pytest.raises(Exception):
                failing_op()
            
        # El log de inicio se hace a nivel INFO antes del error
        assert "Fallo en operación: failing_operation" in caplog.text
