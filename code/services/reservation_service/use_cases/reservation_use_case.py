from services.reservation_service.controller.reservation_controller import ReservationController
from services.session_service.model.session_model import SessionModel


class ReservationUseCase():
    def __init__(self):
        self.controller = ReservationController()
        self.list_reserved_seats = []
        
    def reservation_endpoint(self, session: SessionModel):
        loop = True
        while loop:
            choice = self._show_menu()
            if choice == '1':
                self.list_reserved_seats.append(self.choose_seat(session.ID_SESSION))
                if input("Deseja comprar mais ingressos? (s/n): ") == 's':
                    continue
                else:
                    loop = False

            elif choice == '2':
                print("Saindo do serviço de sessões. Voltando ao menu principal...")
                #TODO: Implementar retorno ao menu principal
                loop = False
            else:
                print("Opção inválida. Tente novamente.")
        
        return self.list_reserved_seats
    
    def choose_seat(self, id_session: str):
        self.controller.show_available_seats(id_session)
        print("Escolha um assento")
        loop = True
        while loop:
            input_id = input("\nDigite o ID do assento que deseja escolher: ")
            selected_seat = self.controller.reserve_seat(input_id)
            if selected_seat:
                print("Assento escolhido com sucesso!")
                loop = False
            else:
                print("Assento não encontrado ou já reservado.")
        return selected_seat
    
    def _show_menu(self):
        print("\nMenu de Reserva:")
        print("1. Escolher um assento")
        print("2. Cancelar e sair")