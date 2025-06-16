# from services.product_service.controller.product_controller import ProductController
# from services.session_service.model.session_model import SessionModel
    

# class ProductUseCase():
#     def __init__(self):
#         self.controller = ProductController()
#         self.list_reserved_products = []
        
#     def marketplace_endpoint(self, session: SessionModel):
#         loop = True
#         while loop:
#             choice = self._show_menu()
#             if choice == '1':
#                 self.list_reserved_products.append(self.choose_product())
#                 if input("Deseja comprar mais produtos? (s/n): ") == 's':
#                     continue
#                 else:
#                     loop = False
#             elif choice == '2':
#                 print("Nenhum produto foi comprado. Avançando para pagamento...")
#                 loop = False
#             elif choice == '3':
#                 print("Saindo do serviço de produtos. Voltando ao menu principal...")
#                 #TODO: Implementar retorno ao menu principal
#                 loop = False
#             else:
#                 print("Opção inválida. Tente novamente.")
        
#         return self.list_reserved_products

#     def choose_product(self):
#         self.controller.show_products()
#         print("Escolha um produto")
#         loop = True
#         while loop:
#             input_id = input("\nDigite o ID do produto que deseja escolher: ")
#             selected_product = self.controller.get_product(input_id)
#             if selected_product:
#                 print("Produto escolhido com sucesso!")
#                 loop = False
#             else:
#                 print("Produto não encontrado.")
#         return selected_product
    
#     def _show_menu(self):
#         print("\nMenu de Produtos:")
#         print("1. Escolher um produto")
#         print("2. Não quero comprar produtos")
#         print("3. Cancelar e sair")



