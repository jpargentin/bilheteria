import time

from services.virtual_queue_service.model.virtual_queue_model import VirtualQueueModel
from services.virtual_queue_service.repository.virtual_queue_repository import VirtualQueueRepository   


class VirtualQueueController:
    def __init__(self):
        self.repository = VirtualQueueRepository()

    def add_to_queue(self, item: VirtualQueueModel):
        queue = self.repository.get_queue()
        queue.append(item)
        self.repository.write_queue(queue)
    
    def process_queue(self, id_web_session: str):
        queue = self.repository.get_queue()
        while queue:
            print("Processing queue...")
            item = VirtualQueueModel(**queue.pop(0))
            self.process_item()
            
            if item.ID_WEB_SESSION == id_web_session:
                return item
            # self.repository.write_queue(queue)

    def process_item(self):
        time.sleep(60)
       
        
    def get_queue_position(self, id_web_session: str):
        queue = self.repository.get_queue()
        for index, item in enumerate(queue):
            if item.ID_WEB_SESSION == id_web_session:
                return index + 1
        return None
