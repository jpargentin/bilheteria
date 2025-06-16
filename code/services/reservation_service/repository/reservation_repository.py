from services.reservation_service.model.ticket_model import TicketModel
from utils.csv_service import CSVService
from typing import List


class ReservationRepository:
    def get_tickets(self):
        tickets = CSVService().read_csv('repositories/tickets', 'tickets.csv')
        return [TicketModel(**ticket) for ticket in tickets]
    
    def write_ticket(self, tickets: List[TicketModel]):
        CSVService().write_csv('repositories/tickets', 'tickets.csv', [ticket.model_dump() for ticket in tickets])
