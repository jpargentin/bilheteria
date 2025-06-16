from pydantic import BaseModel


class SessionModel(BaseModel):
    ID_SESSION: str
    LOCAL: str
    MOVIE: str
    DATE: str