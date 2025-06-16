from services.product_service.controller.product_controller import ProductController
from services.marketplace_service.model.shopping_list_model import ShoppingListModel
from services.marketplace_service.controller.shopping_list_controller import ShoppingListController

from services.reservation_service.model.ticket_model import TicketModel
from services.product_service.model.product_model import ProductModel
from services.authentication_service.model.user_model import UserModel


class MarketPlaceUseCase():
    def __init__(self):
        self.product_controller = ProductController()
        self.shopping_list_controller = ShoppingListController()
        
    def marketplace_endpoint(self, user: UserModel, id_web_session: str, ticket_list: list[TicketModel]=[]):
        
        if ticket_list:
            for ticket in ticket_list:
                product_ticket = ProductModel(
                    ID_PRODUCT=ticket.ID_TICKET,
                    NAME=f"TICKET SESSAO: {ticket.ID_SESSION}",
                    QUANTITY=1,
                    PRICE=ticket.PRICE,
                    ID_WEB_SESSION=id_web_session,
                    ID_USER=user.ID_USER
                )
                self.shopping_list_controller.add_item(product_ticket)

        loop = True
        while loop:
            choice = self._show_menu()
            if choice == '1':
                self.shopping_list_controller.add_item(self.choose_product())
            
            elif choice == '2':
                self.shopping_list_controller.show_items()
            
            elif choice == '3':
                print("Avançando para pagamento...")
                loop = False
            
            elif choice == '4':
                print("Saindo do serviço de produtos. Voltando ao menu principal...")
                #TODO: Implementar retorno ao menu principal
                loop = False
            else:
                print("Opção inválida. Tente novamente.")
        
        return self.shopping_list_controller.get_shopping_list()

    def choose_product(self):
        self.product_controller.show_products()
        print("Escolha um produto")
        loop = True
        while loop:
            input_id = input("\nDigite o ID do produto que deseja escolher: ")
            selected_product = self.product_controller.get_product(input_id)
            if selected_product:
                print("Produto escolhido com sucesso!")
                loop = False
            else:
                print("Produto não encontrado.")
        return selected_product
        
    def _show_menu(self):
        print("\nMenu de Marketplace:")
        print("1. Escolher um produto")
        print("2. Ver carrinho de compras")
        print("3. Pagamento")
        print("4. Cancelar e sair")