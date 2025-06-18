import pytest
from unittest.mock import MagicMock, patch
from services.marketplace_service.controller.shopping_list_controller import ShoppingListController

@pytest.fixture
def mock_user():
    user = MagicMock()
    user.ID_USER = "user123"
    return user

@pytest.fixture
def mock_product():
    product = MagicMock()
    product.ID_PRODUCT = "prod456"
    product.NAME = "Produto Teste"
    product.PRICE = 10.0
    return product

@pytest.fixture
def mock_shopping_list_item(mock_product, mock_user):
    item = MagicMock()
    item.ID_PRODUCT = mock_product.ID_PRODUCT
    item.NAME = mock_product.NAME
    item.QUANTITY = 1
    item.PRICE = mock_product.PRICE
    item.ID_WEB_SESSION = "sess789"
    item.ID_USER = mock_user.ID_USER
    return item

@patch("services.marketplace_service.controller.shopping_list_controller.ShoppingListRepository")
def test_add_item_adds_product(mock_repo_cls, mock_user, mock_product, mock_shopping_list_item):
    mock_repo = mock_repo_cls.return_value
    mock_repo.get_shopping_list.return_value = []
    controller = ShoppingListController(mock_user, "sess789")

    with patch("services.marketplace_service.controller.shopping_list_controller.ShoppingListModel") as mock_model:
        mock_model.return_value = mock_shopping_list_item
        controller.add_item(mock_product)
        mock_repo.write_shopping_list.assert_called_once()
        items_written = mock_repo.write_shopping_list.call_args[0][0]
        assert mock_shopping_list_item in items_written

@patch("services.marketplace_service.controller.shopping_list_controller.ShoppingListRepository")
def test_remove_item_removes_correct_product(mock_repo_cls, mock_user, mock_product, mock_shopping_list_item):
    mock_repo = mock_repo_cls.return_value
    # Add two items, one matching, one not
    other_item = MagicMock()
    other_item.ID_PRODUCT = "other"
    other_item.ID_USER = mock_user.ID_USER
    other_item.ID_WEB_SESSION = "sess789"
    mock_repo.get_shopping_list.return_value = [mock_shopping_list_item, other_item]
    controller = ShoppingListController(mock_user, "sess789")

    controller.remove_item(mock_product.ID_PRODUCT)
    items_written = mock_repo.write_shopping_list.call_args[0][0]
    assert mock_shopping_list_item not in items_written
    assert other_item in items_written

@patch("services.marketplace_service.controller.shopping_list_controller.ShoppingListRepository")
def test_get_shopping_list_filters_by_user_and_session(mock_repo_cls, mock_user, mock_shopping_list_item):
    mock_repo = mock_repo_cls.return_value
    # Add one matching, one with different user, one with different session
    other_user_item = MagicMock()
    other_user_item.ID_USER = "other_user"
    other_user_item.ID_WEB_SESSION = "sess789"
    other_session_item = MagicMock()
    other_session_item.ID_USER = mock_user.ID_USER
    other_session_item.ID_WEB_SESSION = "other_sess"
    mock_repo.get_shopping_list.return_value = [mock_shopping_list_item, other_user_item, other_session_item]
    controller = ShoppingListController(mock_user, "sess789")

    result = controller.get_shopping_list()
    assert result == [mock_shopping_list_item]

@patch("services.marketplace_service.controller.shopping_list_controller.ShoppingListRepository")
def test_show_items_prints_items_and_calls_summarize(mock_repo_cls, mock_user, mock_shopping_list_item, capsys):
    mock_repo = mock_repo_cls.return_value
    mock_repo.get_shopping_list.return_value = [mock_shopping_list_item]
    controller = ShoppingListController(mock_user, "sess789")

    controller.show_items()
    captured = capsys.readouterr()
    assert "ID: prod456" in captured.out
    assert "Produto Teste" in captured.out
    assert "R$10.00" in captured.out
    assert "TOTAL EM CARRINHO" in captured.out

@patch("services.marketplace_service.controller.shopping_list_controller.ShoppingListRepository")
def test_summarize_returns_total_and_prints(mock_repo_cls, mock_user, mock_shopping_list_item, capsys):
    mock_repo = mock_repo_cls.return_value
    mock_shopping_list_item.QUANTITY = 2
    mock_shopping_list_item.PRICE = 15.0
    mock_repo.get_shopping_list.return_value = [mock_shopping_list_item]
    controller = ShoppingListController(mock_user, "sess789")

    total = controller.summarize()
    captured = capsys.readouterr()
    assert total == 30.0
    assert "TOTAL EM CARRINHO: R$30.00" in captured.out