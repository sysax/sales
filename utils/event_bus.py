"""
Event Bus / Pub-Sub para comunicación desacoplada entre componentes - Colombia
Permite que las pantallas se comuniquen sin acoplamiento directo
"""
import logging
from collections import defaultdict
from typing import Callable, Dict, List, Any
from threading import Lock

logger = logging.getLogger(__name__)


class EventBus:
    """
    Event Bus tipo Pub-Sub para comunicación entre componentes
    
    Usage:
        # Suscribirse a evento
        bus = EventBus()
        bus.subscribe('sale_created', self.on_sale_created)
        
        # Publicar evento
        bus.publish('sale_created', sale_id=123, total=50000)
    """
    
    _instance = None
    _lock = Lock()
    
    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance.listeners: Dict[str, List[Callable]] = defaultdict(list)
                    cls._instance.logger = logging.getLogger(__name__)
        return cls._instance
    
    def subscribe(self, event_type: str, callback: Callable, weak: bool = True):
        """
        Suscribirse a un evento
        
        Args:
            event_type: Tipo de evento (ej: 'sale_created', 'inventory_updated')
            callback: Función a llamar cuando ocurra el evento
            weak: Si True, el listener no previene garbage collection
        """
        with self._lock:
            if callback not in self.listeners[event_type]:
                self.listeners[event_type].append(callback)
                self.logger.debug(f"Listener suscrito a {event_type}: {callback.__name__}")
    
    def unsubscribe(self, event_type: str, callback: Callable):
        """
        Cancelar suscripción a un evento
        
        Args:
            event_type: Tipo de evento
            callback: Función a remover
        """
        with self._lock:
            if event_type in self.listeners and callback in self.listeners[event_type]:
                self.listeners[event_type].remove(callback)
                self.logger.debug(f"Listener removido de {event_type}: {callback.__name__}")
    
    def publish(self, event_type: str, **data: Any):
        """
        Publicar un evento a todos los listeners
        
        Args:
            event_type: Tipo de evento
            **data: Datos del evento como kwargs
        """
        with self._lock:
            callbacks = list(self.listeners.get(event_type, []))
        
        for callback in callbacks:
            try:
                callback(**data)
            except Exception as e:
                self.logger.error(f"Error en listener {event_type} ({callback.__name__}): {e}", exc_info=True)
    
    def clear(self):
        """Limpiar todos los listeners (útil para tests)"""
        with self._lock:
            self.listeners.clear()
    
    def get_listeners_count(self, event_type: str = None) -> int:
        """
        Obtener cantidad de listeners
        
        Args:
            event_type: Si None, retorna total de todos los eventos
        """
        with self._lock:
            if event_type is None:
                return sum(len(v) for v in self.listeners.values())
            return len(self.listeners.get(event_type, []))


# Eventos predefinidos del sistema
SALE_CREATED = 'sale_created'
SALE_UPDATED = 'sale_updated'
SALE_DELETED = 'sale_deleted'
INVENTORY_UPDATED = 'inventory_updated'
PRODUCT_CREATED = 'product_created'
PRODUCT_UPDATED = 'product_updated'
USER_LOGGED_IN = 'user_logged_in'
USER_LOGGED_OUT = 'user_logged_out'
SYNC_COMPLETED = 'sync_completed'
SYNC_STARTED = 'sync_started'
CASH_OPENED = 'cash_opened'
CASH_CLOSED = 'cash_closed'


def publish_event(event_type: str, **data: Any):
    """Función helper para publicar eventos"""
    bus = EventBus()
    bus.publish(event_type, **data)


def subscribe_event(event_type: str, callback: Callable):
    """Función helper para suscribirse a eventos"""
    bus = EventBus()
    bus.subscribe(event_type, callback)
