from utils.csv_service import CSVService
from typing import List
from services.product_service.model.product_model import ProductModel


class ProductRepository:

    def get_products(self):
        products = CSVService().read_csv('repositories/products', 'products.csv')
        return [ProductModel(**product) for product in products]

    def write_products(self, products: List[ProductModel]):
        CSVService().write_csv('repositories/products', 'products.csv', [product.model_dump() for product in products], header=['ID_PRODUCT', 'NAME', 'QUANTITY', 'PRICE', 'TAGS'])