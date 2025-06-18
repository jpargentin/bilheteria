import pytest
from unittest.mock import MagicMock, patch, call
from services.marketplace_service.use_cases.marketplace_use_case import MarketPlaceUseCase
from services.authentication_service.model.user_model import UserModel
from services.reservation_service.model.ticket_model import TicketModel
from services.product_service.model.product_model import ProductModel

@pytest.fixture
def mock_user():
    return MagicMock(spec=UserModel)

@pytest.fixture
def mock_product_controller():
    return MagicMock()

@pytest.fixture
def mock_shopping_list_controller():
    return MagicMock()

@pytest.fixture
def use_case(mock_user, mock_product_controller, mock_shopping_list_controller):
    with patch(
        "services.marketplace_service.use_cases.marketplace_use_case.ProductController",
        return_value=mock_product_controller
    ), patch(
        "services.marketplace_service.use_cases.marketplace_use_case.ShoppingListController",
        return_value=mock_shopping_list_controller
    ):
        return MarketPlaceUseCase(mock_user, "session123")

def test_marketplace_endpoint_adds_tickets_to_cart(use_case, mock_shopping_list_controller):
    ticket = MagicMock(spec=TicketModel)
    ticket.ID_TICKET = "T1"
    ticket.ID_SESSION = "S1"
    ticket.PRICE = 50.0

    with patch.object(use_case, "_show_menu", side_effect=["3"]), \
         patch("builtins.print"):
        result = use_case.marketplace_endpoint([ticket])

    # Should add ticket as a product to shopping list
    assert mock_shopping_list_controller.add_item.call_count == 1
    assert mock_shopping_list_controller.get_shopping_list.called
    assert result == mock_shopping_list_controller.get_shopping_list.return_value

def test_marketplace_endpoint_choose_product_flow(use_case, mock_shopping_list_controller):
    with patch.object(use_case, "_show_menu", side_effect=["1", "3"]), \
         patch.object(use_case, "choose_product", return_value="mock_product"), \
         patch("builtins.print"):
        use_case.marketplace_endpoint([])

    mock_shopping_list_controller.add_item.assert_called_with("mock_product")

def test_marketplace_endpoint_show_cart(use_case, mock_shopping_list_controller):
    with patch.object(use_case, "_show_menu", side_effect=["2", "3"]), \
         patch("builtins.print"):
        use_case.marketplace_endpoint([])

    assert mock_shopping_list_controller.show_items.called

def test_marketplace_endpoint_cancel_and_exit(use_case, mock_shopping_list_controller):
    with patch.object(use_case, "_show_menu", side_effect=["4"]), \
         patch("builtins.print"):
        result = use_case.marketplace_endpoint([])

    assert result is None

def test_choose_product_success(use_case, mock_product_controller):
    mock_product_controller.get_product.side_effect = [None, "product_obj"]
    with patch("builtins.input", side_effect=["id1", "id2"]), \
         patch.object(mock_product_controller, "show_products"), \
         patch("builtins.print"):
        result = use_case.choose_product()
    assert result == "product_obj"
    assert mock_product_controller.get_product.call_count == 2

def test_show_menu_returns_input(use_case):
    with patch("builtins.input", return_value="2"), patch("builtins.print"):
        assert use_case._show_menu() == "2"