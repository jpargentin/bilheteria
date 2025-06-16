from services.session_service.repository.session_repository import SessionRepository


class SessionController:

    def __init__(self):
        self.session_repository = SessionRepository()

    def list_available_sessions(self):
        return self.session_repository.get_sessions()

