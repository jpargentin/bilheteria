from services.product_service.repository.product_repository import ProductRepository


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