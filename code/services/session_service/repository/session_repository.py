from utils.csv_service import CSVService
from services.session_service.model.session_model import SessionModel


class SessionRepository:
    header = ["ID_SESSION","LOCAL","MOVIE","DATE"]
    
    def get_sessions(self):
        sessions = CSVService().read_csv('repositories/sessions', 'sessions.csv')
        return [SessionModel(**dict(zip(self.header,session))) for session in sessions]
