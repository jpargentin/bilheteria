import pytest
from unittest.mock import MagicMock, patch
from services.product_service.controller.product_controller import ProductController
from services.reservation_service.model.ticket_model import TicketModel

class DummyProduct:
    def __init__(self, ID_PRODUCT, NAME, PRICE):
        self.ID_PRODUCT = ID_PRODUCT
        self.NAME = NAME
        self.PRICE = PRICE

@pytest.fixture
def dummy_products():
    return [
        DummyProduct("P4", "Produto 4", 10.0),
        DummyProduct("P5", "Produto 5", 20.0),
        DummyProduct("P6", "Produto 6", 30.0),
    ]

@pytest.fixture
def controller(dummy_products):
    with patch('services.product_service.controller.product_controller.ProductRepository') as MockRepo:
        instance = MockRepo.return_value
        instance.get_products.return_value = dummy_products
        yield ProductController()

def test_get_all_products(controller, dummy_products):
    products = controller.get_all_products()
    assert products == dummy_products

def test_get_product_found(controller, dummy_products):
    product = controller.get_product("P5")
    assert product is dummy_products[1]

def test_get_product_not_found(controller):
    product = controller.get_product("PX")
    assert product is None

def test_show_products_prints_correctly(controller, dummy_products, capsys):
    controller.show_products()
    captured = capsys.readouterr()
    assert "Lista de Produtos Disponíveis" in captured.out
    for prod in dummy_products:
        assert prod.ID_PRODUCT in captured.out
        assert prod.NAME in captured.out
        assert f"R${prod.PRICE:.2f}" in captured.out

def test_sugestion_one_ticket(controller, dummy_products):
    ticket_list = [MagicMock(spec=TicketModel)]
    product = controller.sugestion(ticket_list)
    assert product is dummy_products[0]  # P4

def test_sugestion_two_tickets(controller, dummy_products):
    ticket_list = [MagicMock(spec=TicketModel), MagicMock(spec=TicketModel)]
    product = controller.sugestion(ticket_list)
    assert product is dummy_products[1]  # P5

def test_sugestion_more_than_two_tickets(controller, dummy_products):
    ticket_list = [MagicMock(spec=TicketModel) for _ in range(3)]
    product = controller.sugestion(ticket_list)
    assert product is dummy_products[2]  # P6