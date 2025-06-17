from typing import List

from utils.csv_service import CSVService
from services.product_service.model.product_model import ProductModel


class ProductRepository:
    header = ['ID_PRODUCT', 'NAME', 'QUANTITY', 'PRICE', 'TAGS']
    
    def get_products(self):
        products = CSVService().read_csv('repositories/products', 'products.csv')
        return [ProductModel(**dict(zip(self.header, product))) for product in products]

    def write_products(self, products: List[ProductModel]):
        CSVService().write_csv('repositories/products', 'products.csv', [product.model_dump().values() for product in products], header=self.header)