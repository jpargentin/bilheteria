from services.virtual_queue_service.controller.virtual_queue_controller import VirtualQueueController
from services.virtual_queue_service.model.virtual_queue_model import VirtualQueueModel
from services.authentication_service.model.user_model import UserModel

# def create_virtual_queue():
#     controller = VirtualQueueController()
#     controller.write_queue([VirtualQueueModel(ID_WEB_SESSION='1', ID_USER='JOAO.PEDRO@GMAIL.COM'),
#                              VirtualQueueModel(ID_WEB_SESSION='2', ID_USER='MARIA@GMAIL.COM')])

class VirtualQueueService:
    def __init__(self):
        self.controller = VirtualQueueController()

    def virtual_queue_service_endpoint(self, user: UserModel, id_web_session: str):
        item = VirtualQueueModel(ID_WEB_SESSION=id_web_session, ID_USER=user.ID_USER)
        print(f"Adicionando usuario {user.ID_USER} à fila virtual com sessão {id_web_session}")
        self.controller.add_to_queue(item)
        print(f"Usuário {user.ID_USER} está na posicao {self.controller.get_queue_position(id_web_session)}º da fila virtual")
        self.controller.process_queue(id_web_session)
        print(f"CHEGOU SUA VEZ, {user.NAME}!")
        input("Pressione Enter para seguir com sua compra...")
        return item

    