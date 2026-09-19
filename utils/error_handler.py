"""
Manejo de Errores Global con Decoradores - Colombia
Logging estructurado y manejo consistente de errores
"""
import logging
from functools import wraps

# Configurar logging estructurado
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('ventas.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)


class BusinessValidationError(Exception):
    """Error de validación de negocio"""
    pass


class DatabaseError(Exception):
    """Error de base de datos"""
    pass


class AuthenticationError(Exception):
    """Error de autenticación"""
    pass


class PermissionDeniedError(Exception):
    """Error de permisos"""
    pass


def handle_errors(default_return=None, show_user_error=True):
    """
    Decorador para manejo consistente de errores
    
    Args:
        default_return: Valor a retornar en caso de error
        show_user_error: Si True, muestra mensaje al usuario
    
    Usage:
        @handle_errors(default_return=[])
        def load_products(self):
            return self.product_repo.list_products()
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            
            except BusinessValidationError as e:
                logger.warning(f"Error de validación [{func.__name__}]: {e}")
                if show_user_error and len(args) > 0 and hasattr(args[0], '_snack'):
                    args[0]._snack(str(e))
                return default_return
            
            except DatabaseError as e:
                logger.error(f"Error de BD [{func.__name__}]: {e}", exc_info=True)
                if show_user_error and len(args) > 0 and hasattr(args[0], '_snack'):
                    args[0]._snack("Error de base de datos. Intente nuevamente.")
                return default_return
            
            except AuthenticationError as e:
                logger.warning(f"Error de autenticación [{func.__name__}]: {e}")
                if show_user_error and len(args) > 0 and hasattr(args[0], '_snack'):
                    args[0]._snack("Error de autenticación. Verifique sus credenciales.")
                return default_return
            
            except PermissionDeniedError as e:
                logger.warning(f"Permiso denegado [{func.__name__}]: {e}")
                if show_user_error and len(args) > 0 and hasattr(args[0], '_snack'):
                    args[0]._snack("Acceso denegado. No tiene permisos para esta acción.")
                return default_return
            
            except Exception as e:
                logger.critical(f"Error inesperado [{func.__name__}]: {e}", exc_info=True)
                if show_user_error and len(args) > 0 and hasattr(args[0], '_snack'):
                    args[0]._snack("Error interno del sistema. Contacte al administrador.")
                return default_return
        
        return wrapper
    return decorator


def log_operation(operation_name: str):
    """
    Decorador para loggear operaciones
    
    Usage:
        @log_operation("crear_venta")
        def create_sale(self, data):
            ...
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            logger.info(f"Iniciando operación: {operation_name}")
            try:
                result = func(*args, **kwargs)
                logger.info(f"Completada operación: {operation_name} - Éxito")
                return result
            except Exception as e:
                logger.error(f"Fallo en operación: {operation_name} - {e}")
                raise
        return wrapper
    return decorator
