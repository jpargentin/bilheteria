import uuid
import time
from services.authentication_service.use_cases.authentication_use_case import AuthenticationUseCase
from services.session_service.use_cases.session_use_case import SessionUseCase
from services.virtual_queue_service.use_cases.virtual_queue_use_case import VirtualQueueUseCase
from services.reservation_service.use_cases.reservation_use_case import ReservationUseCase
from services.marketplace_service.use_cases.marketplace_use_case import MarketPlaceUseCase
from services.payment_service.use_cases.payment_use_case import PaymentUseCase
from services.receipt_service.use_cases.receipt_use_case import ReceiptUseCase
from utils.setup import DataBaseSetup, SystemSetup


def __main__():
    SystemSetup()
    DataBaseSetup()
    while True:
        print("\n=========================================")
        print("           BILHETERIA ONLINE")
        print("=========================================")
        print("\nBem-vindo ao sistema de bilheteira!")
        id_web_session = str(uuid.uuid4())
        user = AuthenticationUseCase().authentication_endpoint()

        selected_session = SessionUseCase().session_endpoint()

        if not selected_session:
            continue

        print("\nVocê será redirecionado para a fila virtual")
        time.sleep(1)
        VirtualQueueUseCase().virtual_queue_endpoint(user, id_web_session)

        reserved_tickets_list = ReservationUseCase().reservation_endpoint(selected_session, user.ID_USER, id_web_session)

        if not reserved_tickets_list:
            continue

        print("\nVocê será redirecionado para o marketplace")
        time.sleep(1)
        shopping_list = MarketPlaceUseCase(user, id_web_session).marketplace_endpoint(reserved_tickets_list)

        if not shopping_list:
            for ticket in reserved_tickets_list:
                ReservationUseCase().cancel_reservation_endpoint(ticket.ID_TICKET)
                _end_message()
            continue

        print("\nVocê será redirecionado para o pagamento")
        time.sleep(1)
        payment = PaymentUseCase().payment_endpoint()

        if not payment:
            for ticket in reserved_tickets_list:
                ReservationUseCase().cancel_reservation_endpoint(ticket.ID_TICKET)
                _end_message()
            continue

        time.sleep(1)
        ReceiptUseCase().receipt_endpoint()
        
        for ticket in reserved_tickets_list:
            ReservationUseCase().buy_ticket_endpoint(ticket.ID_TICKET)
            
        print("\nCompra realizada com sucesso!")
        print("\nResumo da compra:")
        for ticket in reserved_tickets_list:
            print(f" - Ingresso ID: {ticket.ID_TICKET}, Sessão ID: {ticket.ID_SESSION}, Preço: {ticket.PRICE}")
        print("\nObrigado por comprar conosco!")
        
        print("\nVolte sempre!")
        _end_message()

def _end_message():
    print("\nVolte sempre!")
    print("\n=========================================")
    print("           FIM DO PROCESSO")
    print("=========================================")
        
__main__()