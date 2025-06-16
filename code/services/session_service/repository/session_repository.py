from utils.csv_service import CSVService
from services.session_service.model.session_model import SessionModel


class SessionRepository:
    def get_sessions(self):
        sessions = CSVService().read_csv('repositories/sessions', 'sessions.csv')
        return [SessionModel(**session) for session in sessions]