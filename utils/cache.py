"""
Caché simple para consultas frecuentes - Colombia
Mejora performance evitando consultas repetitivas a la base de datos
"""
from functools import wraps
from time import time
from threading import Lock
from typing import Any, Optional, Callable
import logging

logger = logging.getLogger(__name__)


class SimpleCache:
    """
    Caché en memoria con TTL (Time To Live)
    
    Usage:
        cache = SimpleCache(ttl_seconds=300)
        cache.set('key', value)
        value = cache.get('key')
    """
    
    def __init__(self, ttl_seconds: int = 300, max_size: int = 1000):
        """
        Args:
            ttl_seconds: Tiempo de vida de los items en segundos (default: 5 min)
            max_size: Máximo número de items en caché (default: 1000)
        """
        self._cache: dict = {}
        self._timestamps: dict = {}
        self._lock = Lock()
        self.ttl = ttl_seconds
        self.max_size = max_size
        self.hits = 0
        self.misses = 0
    
    def get(self, key: str) -> Optional[Any]:
        """
        Obtener valor de la caché
        
        Args:
            key: Clave del valor
            
        Returns:
            El valor si existe y no ha expirado, None otherwise
        """
        with self._lock:
            if key in self._cache:
                if time() - self._timestamps[key] < self.ttl:
                    self.hits += 1
                    return self._cache[key]
                else:
                    # Item expirado, removerlo
                    del self._cache[key]
                    del self._timestamps[key]
            
            self.misses += 1
            return None
    
    def set(self, key: str, value: Any) -> None:
        """
        Guardar valor en la caché
        
        Args:
            key: Clave del valor
            value: Valor a guardar
        """
        with self._lock:
            # Si alcanza el tamaño máximo, remover el 10% más antiguo
            if len(self._cache) >= self.max_size:
                self._evict_oldest(percentage=0.1)
            
            self._cache[key] = value
            self._timestamps[key] = time()
    
    def invalidate(self, key: str) -> None:
        """
        Invalidar un item específico de la caché
        
        Args:
            key: Clave a invalidar
        """
        with self._lock:
            if key in self._cache:
                del self._cache[key]
                del self._timestamps[key]
    
    def invalidate_pattern(self, pattern: str) -> None:
        """
        Invalidar items que coincidan con un patrón
        
        Args:
            pattern: Patrón a buscar en las claves (ej: 'products:*')
        """
        with self._lock:
            keys_to_remove = [k for k in self._cache.keys() if k.startswith(pattern.replace('*', ''))]
            for key in keys_to_remove:
                del self._cache[key]
                del self._timestamps[key]
    
    def clear(self) -> None:
        """Limpiar toda la caché"""
        with self._lock:
            self._cache.clear()
            self._timestamps.clear()
            self.hits = 0
            self.misses = 0
    
    def _evict_oldest(self, percentage: float = 0.1) -> None:
        """
        Remover los items más antiguos
        
        Args:
            percentage: Porcentaje de items a remover (default: 10%)
        """
        count_to_remove = int(len(self._cache) * percentage)
        if count_to_remove == 0:
            count_to_remove = 1
        
        # Ordenar por timestamp y remover los más viejos
        sorted_keys = sorted(self._timestamps.keys(), key=lambda k: self._timestamps[k])
        
        for key in sorted_keys[:count_to_remove]:
            del self._cache[key]
            del self._timestamps[key]
    
    def get_stats(self) -> dict:
        """
        Obtener estadísticas de la caché
        
        Returns:
            Diccionario con hits, misses, hit_rate y size
        """
        total = self.hits + self.misses
        hit_rate = (self.hits / total * 100) if total > 0 else 0
        
        return {
            'hits': self.hits,
            'misses': self.misses,
            'hit_rate': f"{hit_rate:.2f}%",
            'size': len(self._cache),
            'max_size': self.max_size,
            'ttl_seconds': self.ttl
        }
    
    def __contains__(self, key: str) -> bool:
        """Verificar si una clave está en la caché"""
        return self.get(key) is not None
    
    def __len__(self) -> int:
        """Retornar número de items en la caché"""
        return len(self._cache)


# Instancia global de caché para uso general
global_cache = SimpleCache(ttl_seconds=300, max_size=500)


def cached(cache_instance: SimpleCache = None, key_prefix: str = '', ttl_override: int = None):
    """
    Decorador para cachear resultados de funciones
    
    Args:
        cache_instance: Instancia de SimpleCache (usa global_cache si None)
        key_prefix: Prefijo para las claves (ej: 'products')
        ttl_override: Override del TTL para esta función específica
    
    Usage:
        @cached(key_prefix='products')
        def list_products(self):
            return self.product_repo.list_products()
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Determinar instancia de caché
            cache = cache_instance if cache_instance else global_cache
            
            # Generar clave única basada en argumentos
            args_key = str(args[1:]) if args else ''  # Excluir self
            kwargs_key = str(sorted(kwargs.items())) if kwargs else ''
            cache_key = f"{key_prefix}:{func.__name__}:{args_key}:{kwargs_key}"
            
            # Intentar obtener de caché
            result = cache.get(cache_key)
            if result is not None:
                logger.debug(f"CACHE HIT: {cache_key}")
                return result
            
            # Ejecutar función y guardar en caché
            result = func(*args, **kwargs)
            
            # Guardar en caché si el resultado no es None
            if result is not None:
                cache.set(cache_key, result)
                logger.debug(f"CACHE MISS (guardado): {cache_key}")
            
            return result
        
        return wrapper
    return decorator


def cache_invalidate(cache_instance: SimpleCache = None, key_pattern: str = ''):
    """
    Decorador para invalidar caché después de ejecutar una función
    Útil para operaciones de escritura (create, update, delete)
    
    Args:
        cache_instance: Instancia de SimpleCache
        key_pattern: Patrón de claves a invalidar (ej: 'products:*')
    
    Usage:
        @cache_invalidate(key_pattern='products:*')
        def save_product(self, data):
            ...
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            
            cache = cache_instance if cache_instance else global_cache
            cache.invalidate_pattern(key_pattern)
            logger.debug(f"CACHE INVALIDATED: {key_pattern}")
            
            return result
        
        return wrapper
    return decorator
