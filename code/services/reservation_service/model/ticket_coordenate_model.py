from pydantic import BaseModel


class TicketCoordinateModel(BaseModel):
    ROW: str
    COLUMN: str
    ROOM: str
