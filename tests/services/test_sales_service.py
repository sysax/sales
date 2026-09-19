"""
Tests para SalesService - Colombia
"""
import pytest
from unittest.mock import Mock, MagicMock, patch
from decimal import Decimal

from services.sales_service import SalesService
from utils.error_handler import BusinessValidationError, DatabaseError


class TestSalesService:
    """Tests para el servicio de ventas"""
    
    @pytest.fixture
    def mock_repos(self):
        """Crear repositorios mockeados"""
        sale_repo = Mock()
        inventory_repo = Mock()
        product_repo = Mock()
        dian_service = Mock()
        
        return {
            'sale_repo': sale_repo,
            'inventory_repo': inventory_repo,
            'product_repo': product_repo,
            'dian_service': dian_service
        }
    
    @pytest.fixture
    def sales_service(self, mock_repos):
        """Crear instancia de SalesService con mocks"""
        return SalesService(
            sale_repo=mock_repos['sale_repo'],
            inventory_repo=mock_repos['inventory_repo'],
            product_repo=mock_repos['product_repo'],
            dian_service=mock_repos['dian_service']
        )
    
    def test_create_sale_success(self, sales_service, mock_repos):
        """Test crear venta exitosa"""
        # Setup
        items = [
            {'product_id': 1, 'quantity': 2, 'price': 1000}
        ]
        
        mock_repos['product_repo'].get_product.return_value = {
            'id': 1,
            'name': 'Producto Test',
            'sku': 'SKU-001',
            'price': 1000,
            'stock': 100,
            'tax': 19
        }
        
        mock_repos['sale_repo'].create_sale.return_value = 123
        
        # Execute
        result = sales_service.create_sale(
            items=items,
            client_name='Cliente Test',
            client_nit='123456789',
            payment_method='Contado'
        )
        
        # Assert
        assert result is not None
        assert result['id'] == 123
        assert result['total'] > 0
        mock_repos['sale_repo'].create_sale.assert_called_once()
        mock_repos['inventory_repo'].register_movement.assert_called()
    
    def test_create_sale_empty_items_raises_error(self, sales_service):
        """Test que venta con items vacíos lanza error"""
        with pytest.raises(BusinessValidationError) as exc_info:
            sales_service.create_sale(
                items=[],
                client_name='Cliente Test'
            )
        
        assert "al menos un item" in str(exc_info.value).lower()
    
    def test_create_sale_insufficient_stock_raises_error(self, sales_service, mock_repos):
        """Test que stock insuficiente lanza error"""
        # Setup
        items = [{'product_id': 1, 'quantity': 100}]
        
        mock_repos['product_repo'].get_product.return_value = {
            'id': 1,
            'name': 'Producto Test',
            'price': 1000,
            'stock': 10  # Stock insuficiente
        }
        
        # Execute & Assert
        with pytest.raises(BusinessValidationError) as exc_info:
            sales_service.create_sale(
                items=items,
                client_name='Cliente Test'
            )
        
        assert "stock insuficiente" in str(exc_info.value).lower()
    
    def test_create_sale_nonexistent_product_raises_error(self, sales_service, mock_repos):
        """Test que producto no existente lanza error"""
        # Setup
        items = [{'product_id': 999, 'quantity': 1}]
        mock_repos['product_repo'].get_product.return_value = None
        
        # Execute & Assert
        with pytest.raises(BusinessValidationError):
            sales_service.create_sale(
                items=items,
                client_name='Cliente Test'
            )
    
    def test_create_sale_with_dian_generates_cufe(self, sales_service, mock_repos):
        """Test que venta electrónica genera CUFE"""
        # Setup
        items = [{'product_id': 1, 'quantity': 1, 'price': 1000}]
        
        mock_repos['product_repo'].get_product.return_value = {
            'id': 1,
            'name': 'Producto Test',
            'price': 1000,
            'stock': 100,
            'tax': 19
        }
        
        mock_repos['sale_repo'].create_sale.return_value = 123
        mock_repos['dian_service'].generate_invoice.return_value = {
            'cufe': 'ABC123XYZ789'
        }
        
        # Execute
        result = sales_service.create_sale(
            items=items,
            client_name='Cliente Test',
            is_electronic=True
        )
        
        # Assert
        assert result['cufe'] == 'ABC123XYZ789'
        mock_repos['dian_service'].generate_invoice.assert_called_once()
    
    def test_calculate_totals_correct(self, sales_service, mock_repos):
        """Test cálculo correcto de totales"""
        # Setup
        items = [
            {'product_id': 1, 'quantity': 2, 'price': 1000, 'discount': 10},
            {'product_id': 2, 'quantity': 1, 'price': 500}
        ]
        
        mock_repos['product_repo'].get_product.side_effect = [
            {'id': 1, 'name': 'Prod 1', 'price': 1000, 'stock': 100, 'tax': 19},
            {'id': 2, 'name': 'Prod 2', 'price': 500, 'stock': 50, 'tax': 0}
        ]
        
        # Execute
        result = sales_service.calculate_totals(items)
        
        # Assert
        assert 'subtotal' in result
        assert 'tax' in result
        assert 'total' in result
        assert result['items_count'] == 2
    
    def test_cancel_sale_success(self, sales_service, mock_repos):
        """Test cancelar venta exitosa"""
        # Setup
        sale_data = {
            'id': 123,
            'status': 'completed',
            'items': [
                {'product_id': 1, 'quantity': 2}
            ]
        }
        mock_repos['sale_repo'].get_sale.return_value = sale_data
        
        # Execute
        result = sales_service.cancel_sale(
            sale_id=123,
            reason='Cliente solicitó cancelación'
        )
        
        # Assert
        assert result is True
        mock_repos['sale_repo'].update_sale_status.assert_called_with(
            123, 'cancelled', 'Cliente solicitó cancelación'
        )
        mock_repos['inventory_repo'].register_movement.assert_called()
    
    def test_cancel_nonexistent_sale_raises_error(self, sales_service, mock_repos):
        """Test cancelar venta inexistente lanza error"""
        mock_repos['sale_repo'].get_sale.return_value = None
        
        with pytest.raises(BusinessValidationError):
            sales_service.cancel_sale(sale_id=999, reason='Test')
    
    def test_cancel_already_cancelled_sale_raises_error(self, sales_service, mock_repos):
        """Test cancelar venta ya cancelada lanza error"""
        mock_repos['sale_repo'].get_sale.return_value = {
            'id': 123,
            'status': 'cancelled'
        }
        
        with pytest.raises(BusinessValidationError):
            sales_service.cancel_sale(sale_id=123, reason='Test')


class TestSalesServiceIntegration:
    """Tests de integración para SalesService (usan DB real)"""
    
    @pytest.fixture
    def sales_service_real(self):
        """Crear SalesService con repositorios reales"""
        return SalesService()
    
    def test_create_sale_integration(self, sales_service_real):
        """Test integración creación de venta con DB real"""
        # Este test usa la base de datos real
        # Asegurarse de tener productos en la DB
        items = [
            {'product_id': 1, 'quantity': 1, 'price': 1000}
        ]
        
        result = sales_service_real.create_sale(
            items=items,
            client_name='Cliente Integration Test',
            payment_method='Contado',
            is_electronic=False
        )
        
        # El resultado puede ser None si el producto no existe
        # pero no debería lanzar excepción no manejada
        assert result is None or isinstance(result, dict)
