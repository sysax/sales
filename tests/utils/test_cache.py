"""
Tests para Caché - Colombia
"""
import pytest
import time
from utils.cache import SimpleCache, cached, cache_invalidate, global_cache


class TestSimpleCache:
    
    def setup_method(self):
        """Crear caché fresca para cada test"""
        self.cache = SimpleCache(ttl_seconds=2, max_size=10)
    
    def test_set_and_get(self):
        """Test guardar y recuperar valor"""
        self.cache.set('key1', 'value1')
        result = self.cache.get('key1')
        assert result == 'value1'
    
    def test_get_nonexistent_key(self):
        """Test recuperar clave inexistente"""
        result = self.cache.get('nonexistent')
        assert result is None
    
    def test_ttl_expiration(self):
        """Test que items expiran después del TTL"""
        self.cache.set('temp', 'value')
        assert self.cache.get('temp') == 'value'
        
        # Esperar a que expire (TTL = 2 segundos)
        time.sleep(2.5)
        
        result = self.cache.get('temp')
        assert result is None
    
    def test_invalidate_single_key(self):
        """Test invalidar una clave específica"""
        self.cache.set('key1', 'value1')
        self.cache.set('key2', 'value2')
        
        self.cache.invalidate('key1')
        
        assert self.cache.get('key1') is None
        assert self.cache.get('key2') == 'value2'
    
    def test_invalidate_pattern(self):
        """Test invalidar por patrón"""
        self.cache.set('products:1', 'prod1')
        self.cache.set('products:2', 'prod2')
        self.cache.set('users:1', 'user1')
        
        self.cache.invalidate_pattern('products:')
        
        assert self.cache.get('products:1') is None
        assert self.cache.get('products:2') is None
        assert self.cache.get('users:1') == 'user1'
    
    def test_clear_all(self):
        """Test limpiar toda la caché"""
        self.cache.set('key1', 'value1')
        self.cache.set('key2', 'value2')
        
        self.cache.clear()
        
        assert len(self.cache) == 0
        assert self.cache.get('key1') is None
    
    def test_max_size_eviction(self):
        """Test que se evicta cuando se alcanza max_size"""
        small_cache = SimpleCache(ttl_seconds=60, max_size=5)
        
        # Llenar hasta el máximo
        for i in range(5):
            small_cache.set(f'key{i}', f'value{i}')
        
        assert len(small_cache) == 5
        
        # Agregar uno más debería causar eviction
        small_cache.set('key_new', 'value_new')
        
        # Debería tener menos o igual al máximo
        assert len(small_cache) <= 5
    
    def test_contains_operator(self):
        """Test operador in"""
        self.cache.set('key1', 'value1')
        
        assert 'key1' in self.cache
        assert 'key2' not in self.cache
    
    def test_len_operator(self):
        """Test operador len"""
        assert len(self.cache) == 0
        
        self.cache.set('key1', 'value1')
        self.cache.set('key2', 'value2')
        
        assert len(self.cache) == 2
    
    def test_get_stats(self):
        """Test estadísticas de caché"""
        self.cache.set('key1', 'value1')
        self.cache.get('key1')  # hit
        self.cache.get('key1')  # hit
        self.cache.get('nonexistent')  # miss
        
        stats = self.cache.get_stats()
        
        assert stats['hits'] == 2
        assert stats['misses'] == 1
        assert 'hit_rate' in stats
        assert stats['size'] == 1


class TestCachedDecorator:
    
    def setup_method(self):
        """Crear caché fresca para cada test"""
        self.cache = SimpleCache(ttl_seconds=60)
        self.call_count = 0
    
    def test_caches_result(self):
        """Test que decorador cachea resultados"""
        @cached(cache_instance=self.cache, key_prefix='test')
        def expensive_function(x):
            self.call_count += 1
            return x * 2
        
        # Primera llamada - debería ejecutar función
        result1 = expensive_function(5)
        assert result1 == 10
        assert self.call_count == 1
        
        # Segunda llamada con mismos args - debería usar caché
        result2 = expensive_function(5)
        assert result2 == 10
        assert self.call_count == 1  # No aumentó
    
    def test_different_args_different_cache(self):
        """Test que diferentes argumentos tienen diferentes entradas"""
        @cached(cache_instance=self.cache, key_prefix='test')
        def multiply(x, y):
            self.call_count += 1
            return x * y
        
        multiply(2, 3)
        multiply(4, 5)
        
        assert self.call_count == 2
        
        # Repetir primeros args
        multiply(2, 3)
        assert self.call_count == 2  # Usó caché
    
    def test_none_result_not_cached(self):
        """Test que resultados None no se cachean"""
        @cached(cache_instance=self.cache, key_prefix='test')
        def maybe_none(x):
            self.call_count += 1
            return None if x < 0 else x
        
        maybe_none(-1)
        maybe_none(-1)  # Debería ejecutar de nuevo
        
        assert self.call_count == 2


class TestCacheInvalidateDecorator:
    
    def setup_method(self):
        """Crear caché fresca para cada test"""
        self.cache = SimpleCache(ttl_seconds=60)
    
    def test_invalidates_after_write(self):
        """Test que invalida caché después de escritura"""
        # Precachear
        self.cache.set('products:1', 'product_data')
        self.cache.set('products:2', 'more_data')
        
        @cache_invalidate(cache_instance=self.cache, key_pattern='products:*')
        def save_product(data):
            return True
        
        save_product({'id': 1, 'name': 'test'})
        
        # Debería haber invalidado
        assert self.cache.get('products:1') is None
        assert self.cache.get('products:2') is None


class TestGlobalCache:
    
    def test_global_cache_exists(self):
        """Test que existe caché global"""
        from utils.cache import global_cache
        
        assert isinstance(global_cache, SimpleCache)
        assert global_cache.ttl == 300
        assert global_cache.max_size == 500
