from pydantic import BaseModel


class ProductModel(BaseModel):
    ID_PRODUCT: str
    NAME: str
    QUANTITY: int
    PRICE: float
    TAGS: str