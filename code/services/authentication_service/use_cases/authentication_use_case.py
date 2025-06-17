from services.authentication_service.controller.authentication_controller import AuthenticationController


class AuthenticationUseCase:

    def __init__(self):
        self.auth_controller = AuthenticationController()

    def authentication_endpoint(self):
        loop = True
        while loop:
            self._show_menu()
            choice = input("Escolha uma opção: ")

            if choice == '1':
                email = input("Digite seu email: ")
                password = input("Digite sua senha: ")
                user = self.auth_controller.login(email, password)
                if user:
                    print(f"Login bem-sucedido! ID do usuario: {user.ID_USER}")
                    loop = False
                else:
                    print("Email ou senha incorretos.")
            
            elif choice == '2':
                name = input("Digite seu nome: ")
                email = input("Digite seu email: ")
                password = input("Digite sua senha: ")
                user = self.auth_controller.register(name, email, password)
                print(f"Usuario registrado com sucesso! ID do usuario: {user.ID_USER}")
                loop = False
            
            else:
                print("Opção inválida. Tente novamente.")
        return user
    
    def _show_menu(self):
        print("\nMenu de Autenticação:")
        print("1. Login")
        print("2. Registrar")
