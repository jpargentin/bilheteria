import time


class PaymentUseCase:
    def payment_endpoint(self):
        print("Iniciando processo de pagamento...")
        print("Processando pagamento...")
        time.sleep(1)  
        print("Pagamento realizado com sucesso!")
        return "Pagamento realizado com sucesso!"