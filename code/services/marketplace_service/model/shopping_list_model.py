
from pydantic import BaseModel


class ShoppingListModel(BaseModel):
    ID_PRODUCT: str
    NAME: str
    QUANTITY: int
    PRICE: float
    ID_WEB_SESSION: str 
    ID_USER: str
     

    
