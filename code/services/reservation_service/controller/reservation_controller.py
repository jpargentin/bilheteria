from services.reservation_service.repository.reservation_repository import ReservationRepository


class ReservationController:
    def __init__(self):
        self.repository = ReservationRepository()

    def _list_available_seats(self, ID_SESSION: str):
        tickets = self.repository.get_tickets()
        available_seats = [ticket for ticket in tickets if ticket.ID_SESSION == ID_SESSION and not ticket.RESERVATION]
        return available_seats

    def show_available_seats(self, ID_SESSION: str):
        available_seats = self._list_available_seats(ID_SESSION)
        print("\nAssentos disponiveis: ")
        for seat in available_seats:
            print(f"\nID: {seat.ID_TICKET}, Fileira: {seat.TICKET_COORDENATES.ROW}, Coluna: {seat.TICKET_COORDENATES.COLUMN}, Sala: {seat.TICKET_COORDENATES.ROOM}, Descricao: {seat.tags[0]}")

    def reserve_seat(self, id_ticket: str, id_user: str, id_web_session: str):
        tickets = self.repository.get_tickets()
        for ticket in tickets:
            if ticket.ID_TICKET == id_ticket:
                ticket.RESERVATION = True
                ticket.ID_USER = id_user
                ticket.ID_WEB_SESSION = id_web_session
                self.repository.write_ticket(tickets)
                return id_ticket

    def buy_ticket(self, id_ticket: str):
        tickets = self.repository.get_tickets()
        for ticket in tickets:
            if ticket.ID_TICKET == id_ticket:
                ticket.BUY = True
                self.repository.write_ticket(tickets)
                return id_ticket

    def cancel_reservation(self, id_ticket: str):
        tickets = self.repository.get_tickets()
        for ticket in tickets:
            if ticket.ID_TICKET == id_ticket:
                ticket.RESERVATION = False
                ticket.ID_USER = None
                ticket.ID_WEB_SESSION = None
                ticket.BUY = False
                self.repository.write_ticket(tickets)
                return id_ticket

    