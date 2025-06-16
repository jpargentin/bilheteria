from pydantic import BaseModel
from services.reservation_service.model.ticket_coordenate_model import TicketCoordinateModel


class TicketModel(BaseModel):
    ID_TICKET: str
    TICKET_COORDENATES: TicketCoordinateModel
    ID_SESSION: str
    RESERVATION: bool
    BUY: bool
    ID_USER: str | None 
    ID_WEB_SESSION: str | None 
    tags: list[str]
    PRICE: float