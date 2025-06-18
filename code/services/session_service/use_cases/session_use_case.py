from services.session_service.controller.session_controller import SessionController


class SessionUseCase():

    def __init__(self):
        self.controller = SessionController()

    def session_endpoint(self):
        print("\n Serviço de sessões!")
        loop = True
        while loop:
            choice = self._show_menu()
            if choice == '1':
                selected_session = self.choose_session()
                if selected_session:
                    print(f"Sessão selecionada: {selected_session.ID_SESSION}")
                    return selected_session

            elif choice == '2':
                print("Saindo do serviço de sessões. Voltando ao menu principal...")
                return None
            else:
                print("Opção inválida. Tente novamente.")
    
    def choose_session(self):
        session_list = self.show_available_sessions()
        loop = True
        while loop:
            input_id = input("\nDigite o ID da sessão que deseja escolher: ")
            selected_session = next((s for s in session_list if s.ID_SESSION == input_id.capitalize()), None)
            if selected_session:
                print("Sessão escolhida com sucesso!")
                loop = False
            else:
                print("Sessão não encontrada.")
        return selected_session

    def show_available_sessions(self):
        print("\nListando sessões disponíveis...")
        session_list = self.controller.list_available_sessions()
        if not session_list:
            print("Nenhuma sessão disponível no momento.")
            raise ValueError("Nenhuma sessão disponível no momento.")

        for session_model in session_list:
            print(f"\n ID: {session_model.ID_SESSION}, Local: {session_model.LOCAL}, Filme: {session_model.MOVIE}, Data Hora: {session_model.DATE}")

        return session_list
    
    def _show_menu(self):
        print("\nMenu de Sessões:")
        print("1. Escolher Sessão")
        print("2. Sair")
        return input("Escolha uma opção: ")
    
        