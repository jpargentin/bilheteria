from services.product_service.repository.product_repository import ProductRepository
from services.reservation_service.model.ticket_model import TicketModel
import difflib


class ProductController:
    def __init__(self):
        self.product_repository = ProductRepository()

    def get_all_products(self):
        return self.product_repository.get_products()

    def get_product(self, id_product: str):
        products = self.product_repository.get_products()
        return next((product for product in products if product.ID_PRODUCT == id_product), None)

    def show_products(self):
        products = self.product_repository.get_products()
        print("\nLista de Produtos Disponíveis:")
        for product in products:
            print(f"\nID: {product.ID_PRODUCT}, Nome: {product.NAME}, Preço: R${product.PRICE:.2f}")
            
    def sugestion(self, ticket_list: list[TicketModel]):
        if len(ticket_list) <= 1:
            id_product = "P4"
        elif len(ticket_list) == 2:
            id_product = "P5"
        else:
            id_product = "P6"
            
        return self.get_product(id_product)
        