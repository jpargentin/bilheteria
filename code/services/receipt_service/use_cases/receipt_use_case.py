from services.product_service.model.product_model import ProductModel


class ReceiptUseCase:
    def receipt_endpoint(self, shopping_list:list[ProductModel]):
        print("Gerando recibo...")
        print("Enviando recibo por e-mail...")
        print("Recibo enviado com sucesso!")
        
        print("\nCompra realizada com sucesso!")
        print("\nResumo dos itens comprados:")
        for item in shopping_list:
            print(f" - ID Produto: {item.ID_PRODUCT}, Item: {item.NAME}, Preço: {item.PRICE}")
        print("\nObrigado por comprar conosco!")
        
        
        return "Recibo enviado com sucesso!"