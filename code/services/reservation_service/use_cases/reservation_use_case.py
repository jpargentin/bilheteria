from services.reservation_service.controller.reservation_controller import ReservationController
from services.session_service.model.session_model import SessionModel


class ReservationUseCase():
    def __init__(self):
        self.controller = ReservationController()
        self.list_reserved_seats = []

    def cancel_reservation_endpoint(self, id_ticket: str):
        self.controller.cancel_reservation(id_ticket)
        
    def buy_ticket_endpoint(self, id_ticket: str):
        self.controller.buy_ticket(id_ticket)

    def reservation_endpoint(self, session: SessionModel, id_user: str, id_web_session: str):
        loop = True
        while loop:
            choice = self._show_menu()
            if choice == '1':
                seat = self.choose_seat(session.ID_SESSION, id_user, id_web_session)
                if seat is not None:
                    self.list_reserved_seats.append(seat)
                if input("\nDeseja comprar mais ingressos? (S/N): ").capitalize() == 'S':
                    continue
                else:
                    loop = False

            elif choice == '2':
                print("Saindo do serviço de sessões. Voltando ao menu principal...")
                return None
            else:
                print("Opção inválida. Tente novamente.")
        
        return self.list_reserved_seats
    
    def choose_seat(self, id_session: str, id_user: str, id_web_session: str):
        self.controller.show_available_seats(id_session)
        loop = True
        while loop:
            input_id = input("\nDigite o ID do assento que deseja escolher ou 'N' para sair: ")
            if input_id.capitalize() == 'N':
                return None
            selected_seat = self.controller.reserve_seat(id_session, input_id.capitalize(), id_user, id_web_session)
            if selected_seat:
                print("Assento escolhido com sucesso!")
                loop = False
            else:
                print("Assento não encontrado ou já reservado.")
        return selected_seat
    
    def _show_menu(self):
        print("\nMenu de Reserva:")
        print("1. Escolher um assento")
        print("2. Desistir da compra e sair")
        return input("Escolha uma opção: ")