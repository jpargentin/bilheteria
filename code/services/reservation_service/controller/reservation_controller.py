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
        if not available_seats:
            print("Infelizmente nossos ingressos para essa sessão ja esgotaram")
        for seat in available_seats:
            cordinates = seat.TICKET_COORDENATES.replace('[','').replace(']','').split(',')
            tags = seat.tags.replace('[','').replace(']','').split(',')
            print(f"\nID: {seat.ID_TICKET}, Fileira: {cordinates[0]}, Coluna: {cordinates[1]}, Sala: {cordinates[2]}, Descricao: {tags[0]}, Preço: {seat.PRICE}")

    def reserve_seat(self, id_session: str, id_ticket: str, id_user: str, id_web_session: str):
        # tickets = self.repository.get_tickets()
        tickets = self._list_available_seats(id_session)
        for ticket in tickets:
            if ticket.ID_TICKET == id_ticket:
                ticket.RESERVATION = True
                ticket.ID_USER = id_user
                ticket.ID_WEB_SESSION = id_web_session
                self.repository.write_ticket(tickets)
                return ticket
        return None
    
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

    