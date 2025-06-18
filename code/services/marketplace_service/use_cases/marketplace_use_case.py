from services.product_service.controller.product_controller import ProductController
from services.marketplace_service.controller.shopping_list_controller import ShoppingListController
from services.reservation_service.model.ticket_model import TicketModel
from services.product_service.model.product_model import ProductModel
from services.authentication_service.model.user_model import UserModel


class MarketPlaceUseCase():
    def __init__(self, user: UserModel, id_web_session: str):
        self.user = user
        self.id_web_session = id_web_session
        self.product_controller = ProductController()
        self.shopping_list_controller = ShoppingListController(user, id_web_session)
        
    def marketplace_endpoint(self, ticket_list: list[TicketModel]=[]):
        print("\nBem-vindo ao Marketplace!")
        print("Seus ingressos já estão reservados e prontos para serem comprados")
        print("Mas antes... temos uma seleção incrível de produtos que podem acompanhar sua sessão!")
        print("Você pode escolher produtos maravilhosos como pipoca, refrigerante, doces e muito mais!")
        
        sugested_product = self.product_controller.sugestion(ticket_list)
        print("\n SUGESTÃO ESPECIAL PARA VOCÊ COM BASE NO SEU INGRESSO: ")
        print(f"ID: {sugested_product.ID_PRODUCT}, Nome: {sugested_product.NAME}, Preço: R${sugested_product.PRICE:.2f}")
        
        
        if ticket_list:
            for ticket in ticket_list:
                product_ticket = ProductModel(
                    ID_PRODUCT=ticket.ID_TICKET,
                    NAME=f"TICKET SESSÃO: {ticket.ID_SESSION}",
                    QUANTITY=1,
                    PRICE=ticket.PRICE,
                    TAGS=""
                )
                self.shopping_list_controller.add_item(product_ticket)

        loop = True
        while loop:
            choice = self._show_menu()
            if choice == '1':
                print("\nProduto adicionado ao seu carrinho!")
                self.shopping_list_controller.add_item(sugested_product)
                
            elif choice == '2':
                print("\nEscolha um produto:")
                product = self.choose_product()
                if product:
                    self.shopping_list_controller.add_item(product)
            
            elif choice == '3':
                print("\nCarrinho de compras:")
                self.shopping_list_controller.show_items()
            
            elif choice == '4':
                print("\nAvançando para pagamento...")
                loop = False
            
            elif choice == '5':
                print("Saindo do serviço de produtos. Voltando ao menu principal...")
                return None
            else:
                print("Opção inválida. Tente novamente.")
        
        return self.shopping_list_controller.get_shopping_list()

    def choose_product(self):
        self.product_controller.show_products()
        loop = True
        while loop:
            input_id = input("\nDigite o ID do produto que deseja escolher ou 'N' para sair: ")
            if input_id.capitalize() == "N":
                return None
            selected_product = self.product_controller.get_product(input_id.capitalize())
            if selected_product:
                print("Produto escolhido com sucesso!")
                loop = False
            else:
                print("Produto não encontrado.")
        return selected_product
        
    def _show_menu(self):
        print("\nMenu de Marketplace:")
        print("1. Quero o produto sugerido")
        print("2. Escolher um produto")
        print("3. Ver carrinho de compras")
        print("4. Pagamento")
        print("5. Cancelar e sair")
        return input("Escolha uma opção: ")