import pytest
from unittest.mock import MagicMock, patch
from services.marketplace_service.use_cases.marketplace_use_case import MarketPlaceUseCase

@pytest.fixture
def mock_user():
    user = MagicMock()
    user.ID_USER = "user1"
    return user

@pytest.fixture
def mock_ticket():
    ticket = MagicMock()
    ticket.ID_TICKET = "T1"
    ticket.ID_SESSION = "S1"
    ticket.PRICE = 50.0
    return ticket

@pytest.fixture
def mock_product():
    product = MagicMock()
    product.ID_PRODUCT = "P1"
    product.NAME = "Pipoca"
    product.PRICE = 10.0
    product.QUANTITY = 1
    product.TAGS = ""
    return product

@pytest.fixture
def use_case(mock_user):
    with patch("services.marketplace_service.use_cases.marketplace_use_case.ProductController") as MockProductController, \
         patch("services.marketplace_service.use_cases.marketplace_use_case.ShoppingListController") as MockShoppingListController:
        mock_product_controller = MockProductController.return_value
        mock_shopping_list_controller = MockShoppingListController.return_value
        return MarketPlaceUseCase(mock_user, "session1")

def test_marketplace_endpoint_add_suggested_product(use_case, mock_ticket, mock_product):
    # Setup mocks
    use_case.product_controller.sugestion.return_value = mock_product
    use_case.shopping_list_controller.get_shopping_list.return_value = ["item1"]
    use_case.shopping_list_controller.add_item = MagicMock()
    use_case._show_menu = MagicMock(side_effect=['1', '4'])  # Add suggested, then payment

    with patch("builtins.print"):
        result = use_case.marketplace_endpoint([mock_ticket])

    use_case.shopping_list_controller.add_item.assert_any_call(mock_product)
    assert result == ["item1"]

def test_marketplace_endpoint_choose_product(use_case, mock_ticket, mock_product):
    use_case.product_controller.sugestion.return_value = mock_product
    use_case.shopping_list_controller.get_shopping_list.return_value = ["item2"]
    use_case.shopping_list_controller.add_item = MagicMock()
    use_case._show_menu = MagicMock(side_effect=['2', '4'])  # Choose product, then payment

    # Patch choose_product to return a product
    use_case.choose_product = MagicMock(return_value=mock_product)

    with patch("builtins.print"):
        result = use_case.marketplace_endpoint([mock_ticket])

    use_case.shopping_list_controller.add_item.assert_any_call(mock_product)
    assert result == ["item2"]

def test_marketplace_endpoint_show_cart(use_case, mock_ticket, mock_product):
    use_case.product_controller.sugestion.return_value = mock_product
    use_case.shopping_list_controller.get_shopping_list.return_value = ["item3"]
    use_case.shopping_list_controller.show_items = MagicMock()
    use_case._show_menu = MagicMock(side_effect=['3', '4'])  # Show cart, then payment

    with patch("builtins.print"):
        result = use_case.marketplace_endpoint([mock_ticket])

    use_case.shopping_list_controller.show_items.assert_called_once()
    assert result == ["item3"]

def test_marketplace_endpoint_cancel_and_exit(use_case, mock_ticket, mock_product):
    use_case.product_controller.sugestion.return_value = mock_product
    use_case._show_menu = MagicMock(return_value='5')

    with patch("builtins.print"):
        result = use_case.marketplace_endpoint([mock_ticket])

    assert result is None

def test_choose_product_found(use_case, mock_product):
    use_case.product_controller.show_products = MagicMock()
    use_case.product_controller.get_product = MagicMock(return_value=mock_product)
    with patch("builtins.input", side_effect=["P1"]):
        with patch("builtins.print"):
            result = use_case.choose_product()
    assert result == mock_product

def test_choose_product_not_found_then_found(use_case, mock_product):
    use_case.product_controller.show_products = MagicMock()
    # First call returns None, second returns product
    use_case.product_controller.get_product = MagicMock(side_effect=[None, mock_product])
    with patch("builtins.input", side_effect=["X", "P1"]):
        with patch("builtins.print"):
            result = use_case.choose_product()
    assert result == mock_product

def test_choose_product_exit(use_case):
    use_case.product_controller.show_products = MagicMock()
    with patch("builtins.input", side_effect=["N"]):
        with patch("builtins.print"):
            result = use_case.choose_product()
    assert result is None