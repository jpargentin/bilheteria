from pydantic import BaseModel


class ProductModel(BaseModel):
    ID_PRODUCT: int
    NAME: str
    QUANTITY: int
    PRICE: float
    TAGS: list[str]