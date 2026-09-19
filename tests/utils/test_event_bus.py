"""
Tests para Event Bus - Colombia
"""
import pytest
from utils.event_bus import EventBus, publish_event, subscribe_event, SALE_CREATED, INVENTORY_UPDATED


class TestEventBus:
    
    def setup_method(self):
        """Limpiar event bus antes de cada test"""
        EventBus._instance = None
        self.bus = EventBus()
        self.received_events = []
    
    def on_event(self, **data):
        """Callback mock para recibir eventos"""
        self.received_events.append(data)
    
    def test_singleton_instance(self):
        """Test que EventBus es singleton"""
        bus1 = EventBus()
        bus2 = EventBus()
        assert bus1 is bus2
    
    def test_subscribe_and_publish(self):
        """Test suscripción y publicación básica"""
        self.bus.subscribe('test_event', self.on_event)
        self.bus.publish('test_event', value=42, name='test')
        
        assert len(self.received_events) == 1
        assert self.received_events[0]['value'] == 42
        assert self.received_events[0]['name'] == 'test'
    
    def test_multiple_subscribers(self):
        """Test múltiples subscribers al mismo evento"""
        events1 = []
        events2 = []
        
        def callback1(**data):
            events1.append(data)
        
        def callback2(**data):
            events2.append(data)
        
        self.bus.subscribe('multi_event', callback1)
        self.bus.subscribe('multi_event', callback2)
        
        self.bus.publish('multi_event', data='shared')
        
        assert len(events1) == 1
        assert len(events2) == 1
        assert events1[0]['data'] == 'shared'
        assert events2[0]['data'] == 'shared'
    
    def test_unsubscribe(self):
        """Test cancelar suscripción"""
        self.bus.subscribe('temp_event', self.on_event)
        self.bus.publish('temp_event', step=1)
        
        self.bus.unsubscribe('temp_event', self.on_event)
        self.bus.publish('temp_event', step=2)
        
        assert len(self.received_events) == 1
        assert self.received_events[0]['step'] == 1
    
    def test_publish_to_nonexistent_event(self):
        """Test publicar a evento sin subscribers no falla"""
        # No hay subscribers
        self.bus.publish('nonexistent_event', data='test')
        # No debería lanzar excepción
        assert True
    
    def test_listener_error_doesnt_stop_others(self):
        """Test que error en un listener no afecta a los demás"""
        events_received = []
        
        def failing_callback(**data):
            raise Exception("Error intencional")
        
        def working_callback(**data):
            events_received.append(data)
        
        self.bus.subscribe('error_test', failing_callback)
        self.bus.subscribe('error_test', working_callback)
        
        # No debería lanzar excepción
        self.bus.publish('error_test', value='test')
        
        assert len(events_received) == 1
        assert events_received[0]['value'] == 'test'
    
    def test_get_listeners_count(self):
        """Test contar listeners"""
        self.bus.subscribe('event1', self.on_event)
        self.bus.subscribe('event1', lambda **d: None)
        self.bus.subscribe('event2', self.on_event)
        
        assert self.bus.get_listeners_count('event1') == 2
        assert self.bus.get_listeners_count('event2') == 1
        assert self.bus.get_listeners_count() == 3
    
    def test_clear_all_listeners(self):
        """Test limpiar todos los listeners"""
        self.bus.subscribe('event1', self.on_event)
        self.bus.subscribe('event2', self.on_event)
        
        self.bus.clear()
        
        assert self.bus.get_listeners_count() == 0
    
    def test_predefined_events(self):
        """Test que eventos predefinidos existen"""
        assert SALE_CREATED == 'sale_created'
        assert INVENTORY_UPDATED == 'inventory_updated'


class TestHelperFunctions:
    
    def setup_method(self):
        """Limpiar event bus antes de cada test"""
        EventBus._instance = None
        self.received = []
    
    def on_test(self, **data):
        self.received.append(data)
    
    def test_publish_event_helper(self):
        """Test función helper publish_event"""
        subscribe_event('helper_test', self.on_test)
        publish_event('helper_test', value=123)
        
        assert len(self.received) == 1
        assert self.received[0]['value'] == 123
    
    def test_subscribe_event_helper(self):
        """Test función helper subscribe_event"""
        subscribe_event('another_test', self.on_test)
        bus = EventBus()
        bus.publish('another_test', msg='hello')
        
        assert len(self.received) == 1
        assert self.received[0]['msg'] == 'hello'
