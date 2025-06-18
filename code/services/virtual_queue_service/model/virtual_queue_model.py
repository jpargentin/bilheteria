from pydantic import BaseModel


class VirtualQueueModel(BaseModel):
    ID_WEB_SESSION: str
    ID_USER: str
