import unittest
from unittest.mock import MagicMock, patch
from services.authentication_service.controller.authentication_controller import AuthenticationController
from services.authentication_service.model.user_model import UserModel

class TestAuthenticationController(unittest.TestCase):
    def setUp(self):
        patcher = patch('services.authentication_service.controller.authentication_controller.AuthenticationRepository')
        self.MockRepo = patcher.start()
        self.addCleanup(patcher.stop)
        self.mock_repo_instance = self.MockRepo.return_value
        self.controller = AuthenticationController()

    def test_login_success(self):
        mock_user = MagicMock()
        mock_user.check_password.return_value = True
        self.mock_repo_instance.find_by_email.return_value = mock_user

        result = self.controller.login('test@example.com', 'password')
        self.mock_repo_instance.find_by_email.assert_called_once_with('test@example.com')
        mock_user.check_password.assert_called_once_with('password')
        self.assertEqual(result, mock_user)

    def test_login_failure_wrong_password(self):
        mock_user = MagicMock()
        mock_user.check_password.return_value = False
        self.mock_repo_instance.find_by_email.return_value = mock_user

        result = self.controller.login('test@example.com', 'wrongpassword')
        self.assertIsNone(result)

    def test_login_failure_no_user(self):
        self.mock_repo_instance.find_by_email.return_value = None
        result = self.controller.login('notfound@example.com', 'password')
        self.assertIsNone(result)

    def test_register_creates_user(self):
        self.mock_repo_instance._get_users.return_value = []
        self.mock_repo_instance.create_user.return_value = 'user_created'
        with patch('services.authentication_service.controller.authentication_controller.UserModel') as MockUserModel:
            mock_user_instance = MockUserModel.return_value
            result = self.controller.register('Test User', 'test@example.com', 'password123')
            MockUserModel.assert_called_once_with(ID_USER='1', NAME='Test User', EMAIL='test@example.com', PASSWORD='password123')
            self.mock_repo_instance.create_user.assert_called_once_with(mock_user_instance)
            self.assertEqual(result, 'user_created')

    def test_get_user_info(self):
        self.mock_repo_instance.get_user_info.return_value = {'ID_USER': '1', 'NAME': 'Test User'}
        result = self.controller.get_user_info('1')
        self.mock_repo_instance.get_user_info.assert_called_once_with('1')
        self.assertEqual(result, {'ID_USER': '1', 'NAME': 'Test User'})

if __name__ == '__main__':
    unittest.main()