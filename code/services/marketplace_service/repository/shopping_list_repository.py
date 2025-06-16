from utils.csv_service import CSVService
from typing import List
from services.marketplace_service.model.shopping_list_model import ShoppingListModel


class ShoppingListRepository:

    def get_shopping_list(self):
        products = CSVService().read_csv('repositories/shopping_list', 'shopping_list.csv')
        return [ShoppingListModel(**product) for product in products]

    def write_shopping_list(self, products: List[ShoppingListModel]):
        CSVService().write_csv('repositories/shopping_list', 'shopping_list.csv', [product.model_dump() for product in products], header=['ID_PRODUCT', 'NAME', 'QUANTITY', 'PRICE', 'ID_WEB_SESSION', 'ID_USER'])
