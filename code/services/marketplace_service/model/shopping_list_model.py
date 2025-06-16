
from pydantic import BaseModel


class ShoppingListModel(BaseModel):
    ID_PRODUCT: int
    NAME: str
    QUANTITY: int
    PRICE: float
    ID_WEB_SESSION: str 
    ID_USER: str
     

    
