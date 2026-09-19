"""
Tests para InventoryService - Colombia
"""
import pytest
from unittest.mock import Mock, patch

from services.inventory_service import InventoryService
from utils.error_handler import BusinessValidationError


class TestInventoryService:
    """Tests para el servicio de inventario"""
    
    @pytest.fixture
    def mock_repos(self):
        """Crear repositorios mockeados"""
        inventory_repo = Mock()
        product_repo = Mock()
        
        return {
            'inventory_repo': inventory_repo,
            'product_repo': product_repo
        }
    
    @pytest.fixture
    def inventory_service(self, mock_repos):
        """Crear instancia de InventoryService con mocks"""
        return InventoryService(
            inventory_repo=mock_repos['inventory_repo'],
            product_repo=mock_repos['product_repo']
        )
    
    def test_register_purchase_success(self, inventory_service, mock_repos):
        """Test registrar compra exitosa"""
        # Setup
        mock_repos['product_repo'].get_product.return_value = {
            'id': 1,
            'name': 'Producto Test',
            'sku': 'SKU-001',
            'stock': 50,
            'price_buy': 800
        }
        mock_repos['inventory_repo'].register_movement.return_value = 456
        
        # Execute
        result = inventory_service.register_purchase(
            product_id=1,
            quantity=10,
            cost_price=850,
            supplier_name='Proveedor Test',
            invoice_number='FAC-001'
        )
        
        # Assert
        assert result is not None
        assert result['movement_id'] == 456
        assert result['new_stock'] == 60
        mock_repos['inventory_repo'].register_movement.assert_called_once()
        mock_repos['product_repo'].update_product.assert_called()
    
    def test_register_purchase_zero_quantity_raises_error(self, inventory_service):
        """Test que cantidad cero lanza error"""
        with pytest.raises(BusinessValidationError) as exc_info:
            inventory_service.register_purchase(
                product_id=1,
                quantity=0,
                cost_price=100,
                supplier_name='Proveedor'
            )
        
        assert "mayor a 0" in str(exc_info.value).lower()
    
    def test_register_purchase_nonexistent_product_raises_error(self, inventory_service, mock_repos):
        """Test que producto inexistente lanza error"""
        mock_repos['product_repo'].get_product.return_value = None
        
        with pytest.raises(BusinessValidationError):
            inventory_service.register_purchase(
                product_id=999,
                quantity=10,
                cost_price=100,
                supplier_name='Proveedor'
            )
    
    def test_register_adjustment_positive_success(self, inventory_service, mock_repos):
        """Test ajuste positivo exitoso"""
        mock_repos['product_repo'].get_product.return_value = {
            'id': 1,
            'name': 'Producto Test',
            'stock': 50
        }
        mock_repos['inventory_repo'].register_movement.return_value = 789
        
        # Execute
        result = inventory_service.register_adjustment(
            product_id=1,
            quantity=5,
            reason='Inventario físico mayor'
        )
        
        # Assert
        assert result is not None
        assert result['new_stock'] == 55
        mock_repos['inventory_repo'].register_movement.assert_called()
    
    def test_register_adjustment_negative_success(self, inventory_service, mock_repos):
        """Test ajuste negativo exitoso"""
        mock_repos['product_repo'].get_product.return_value = {
            'id': 1,
            'name': 'Producto Test',
            'stock': 50
        }
        
        # Execute
        result = inventory_service.register_adjustment(
            product_id=1,
            quantity=-10,
            reason='Producto dañado'
        )
        
        # Assert
        assert result is not None
        assert result['new_stock'] == 40
    
    def test_register_adjustment_would_be_negative_raises_error(self, inventory_service, mock_repos):
        """Test que ajuste que resulta en stock negativo lanza error"""
        mock_repos['product_repo'].get_product.return_value = {
            'id': 1,
            'name': 'Producto Test',
            'stock': 5
        }
        
        with pytest.raises(BusinessValidationError) as exc_info:
            inventory_service.register_adjustment(
                product_id=1,
                quantity=-10,  # Resultaría en -5
                reason='Test'
            )
        
        assert "stock negativo" in str(exc_info.value).lower()
    
    def test_register_adjustment_zero_quantity_raises_error(self, inventory_service):
        """Test que cantidad cero en ajuste lanza error"""
        with pytest.raises(BusinessValidationError) as exc_info:
            inventory_service.register_adjustment(
                product_id=1,
                quantity=0,
                reason='Test'
            )
        
        assert "diferente de 0" in str(exc_info.value).lower()
    
    def test_get_low_stock_products(self, inventory_service, mock_repos):
        """Test obtener productos con stock bajo"""
        # Setup
        mock_repos['product_repo'].list_products.return_value = [
            {'id': 1, 'name': 'Prod Bajo', 'stock': 5, 'stock_min': 10},
            {'id': 2, 'name': 'Prod OK', 'stock': 50, 'stock_min': 10},
            {'id': 3, 'name': 'Prod Crítico', 'stock': 2, 'stock_min': 10}
        ]
        
        # Execute
        result = inventory_service.get_low_stock_products()
        
        # Assert
        assert len(result) == 2  # Prod Bajo y Prod Crítico
        assert all(p['stock_status'] == 'low' for p in result)
    
    def test_get_inventory_valuation(self, inventory_service, mock_repos):
        """Test valorización de inventario"""
        # Setup
        mock_repos['product_repo'].list_products.return_value = [
            {'id': 1, 'name': 'Prod 1', 'sku': 'SKU-001', 'stock': 10, 'price_buy': 100},
            {'id': 2, 'name': 'Prod 2', 'sku': 'SKU-002', 'stock': 20, 'price_buy': 50},
            {'id': 3, 'name': 'Prod 3', 'sku': 'SKU-003', 'stock': 0, 'price_buy': 200}  # Sin valor
        ]
        
        # Execute
        result = inventory_service.get_inventory_valuation()
        
        # Assert
        assert result['total_value'] == 2000  # (10*100) + (20*50)
        assert result['products_count'] == 2  # Solo productos con valor > 0
    
    def test_get_movements_by_product(self, inventory_service, mock_repos):
        """Test obtener movimientos por producto"""
        # Setup
        expected_movements = [
            {'id': 1, 'product_id': 1, 'quantity': 10, 'type': 'purchase'},
            {'id': 2, 'product_id': 1, 'quantity': -5, 'type': 'sale'}
        ]
        mock_repos['inventory_repo'].get_movements_by_product.return_value = expected_movements
        
        # Execute
        result = inventory_service.get_movements_by_product(
            product_id=1,
            start_date='2024-01-01',
            end_date='2024-12-31'
        )
        
        # Assert
        assert len(result) == 2
        mock_repos['inventory_repo'].get_movements_by_product.assert_called_once_with(
            1, '2024-01-01', '2024-12-31'
        )
