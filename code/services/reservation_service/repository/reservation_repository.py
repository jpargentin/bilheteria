from services.reservation_service.model.ticket_model import TicketModel
from utils.csv_service import CSVService
from typing import List


class ReservationRepository:
    header = ["ID_TICKET","TICKET_COORDENATES","ID_SESSION","RESERVATION","BUY","ID_USER","ID_WEB_SESSION","tags", "PRICE"]
    
    def get_tickets(self):
        tickets = CSVService().read_csv('repositories/tickets', 'tickets.csv')
        return [TicketModel(**dict(zip(self.header, ticket))) for ticket in tickets]

    def write_ticket(self, tickets: List[TicketModel]):
        CSVService().write_csv('repositories/tickets', 'tickets.csv', [ticket.model_dump().values() for ticket in tickets],
                              header=self.header)
