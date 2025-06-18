from typing import List

from utils.csv_service import CSVService
from services.virtual_queue_service.model.virtual_queue_model import VirtualQueueModel


class VirtualQueueRepository:
    header = ['ID_WEB_SESSION', 'ID_USER']
    
    def write_queue(self, queue: List[VirtualQueueModel]):
        CSVService().write_csv('repositories/virtual_queue', 'virtual_queue.csv', [queue_item.model_dump().values() for queue_item in queue], header=self.header)

    def get_queue(self):
        queue_list = CSVService().read_csv('repositories/virtual_queue', 'virtual_queue.csv')
        return [VirtualQueueModel(**dict(zip(self.header, queue_item))) for queue_item in queue_list]