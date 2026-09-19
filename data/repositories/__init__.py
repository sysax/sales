"""
Repositorios especializados — Arquitectura por dominio
Cada repositorio maneja una entidad específica con SRP
"""

from data.repositories.user_repository import UserRepository
from data.repositories.product_repository import ProductRepository
from data.repositories.client_repository import ClientRepository, SupplierRepository
from data.repositories.sale_repository import SaleRepository
from data.repositories.inventory_repository import (
    InventoryRepository, CajaRepository, PromoRepository, 
    PurchaseRepository, AuditRepository
)

__all__ = [
    "UserRepository",
    "ProductRepository",
    "ClientRepository",
    "SupplierRepository",
    "SaleRepository",
    "InventoryRepository",
    "CajaRepository",
    "PromoRepository",
    "PurchaseRepository",
    "AuditRepository",
]
