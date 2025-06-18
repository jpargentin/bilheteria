import unittest
from unittest.mock import patch, MagicMock
from services.session_service.controller.session_controller import SessionController

class TestSessionController(unittest.TestCase):

    @patch('services.session_service.controller.session_controller.SessionRepository')
    def test_list_available_sessions_returns_sessions(self, MockSessionRepository):
        # Arrange
        mock_repo = MockSessionRepository.return_value
        mock_sessions = [
            {'id': 1, 'name': 'Session 1'},
            {'id': 2, 'name': 'Session 2'}
        ]
        mock_repo.get_sessions.return_value = mock_sessions

        controller = SessionController()

        result = controller.list_available_sessions()

        mock_repo.get_sessions.assert_called_once()
        self.assertEqual(result, mock_sessions)

    @patch('services.session_service.controller.session_controller.SessionRepository')
    def test_init_creates_session_repository_instance(self, MockSessionRepository):
        controller = SessionController()
        self.assertIs(controller.session_repository, MockSessionRepository.return_value)

if __name__ == '__main__':
    unittest.main()