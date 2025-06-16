from services.marketplace_service.repository.shopping_list_repository import ShoppingListRepository
from services.product_service.model.product_model import ProductModel
from services.authentication_service.model.user_model import UserModel  
from services.marketplace_service.model.shopping_list_model import ShoppingListModel



class ShoppingListController:
    def __init__(self, user: UserModel, id_web_session: str):
        self.shopping_list_repository = ShoppingListRepository()
        self.user_id = user.ID_USER
        self.web_session_id = id_web_session

    def add_item(self, product: ProductModel):
        items = self.shopping_list_repository.get_shopping_list()
        item = ShoppingListModel(
            ID_PRODUCT=product.ID_PRODUCT,
            NAME=product.NAME,
            QUANTITY=1,
            PRICE=product.PRICE,
            ID_WEB_SESSION=self.web_session_id,
            ID_USER=self.user_id
        )
        items.append(item)
        self.shopping_list_repository.write_shopping_list(items)

    def remove_item(self, product_id: str):
        items = self.shopping_list_repository.get_shopping_list()
        items = [item for item in items if not (item.ID_PRODUCT == product_id and item.ID_USER == self.user_id and item.ID_WEB_SESSION == self.web_session_id)]
        self.shopping_list_repository.write_shopping_list(items)

    def get_shopping_list(self):
        items = self.shopping_list_repository.get_shopping_list()
        return [item for item in items if (item.ID_USER==self.user_id and item.ID_WEB_SESSION==self.web_session_id)]

    def show_items(self):
        items = self.shopping_list_repository.get_shopping_list()
        for item in items:
            print(f"ID: {item.ID_PRODUCT}, Name: {item.NAME}, Price: {item.PRICE}, Quantity: {item.QUANTITY}, Total: {item.PRICE * item.QUANTITY}")
        print("TOTAL EM CARRINHO: ", self.summarize())
    
    def summarize(self):
        items = self.get_shopping_list()
        total = sum(item.PRICE * item.QUANTITY for item in items)
        print(f"Total: {total}")
        return total