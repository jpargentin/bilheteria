import pytest
from unittest.mock import patch, MagicMock
from services.authentication_service.use_cases.authentication_use_case import AuthenticationUseCase
from services.authentication_service.model.user_model import UserModel

@pytest.fixture
def use_case():
    return AuthenticationUseCase()

def make_user(id):
    return UserModel(ID_USER=str(id), NAME="Test", EMAIL="test@email.com", PASSWORD="password")

@patch("services.authentication_service.use_cases.authentication_use_case.input")
@patch("services.authentication_service.use_cases.authentication_use_case.AuthenticationController")
def test_authentication_endpoint_login_success(mock_controller_cls, mock_input, use_case):
    mock_controller = mock_controller_cls.return_value
    user = make_user(42)
    mock_controller.login.return_value = user
    mock_input.side_effect = ['1', 'test@email.com', 'password']
    with patch("builtins.print"):
        result = use_case.authentication_endpoint()
    assert isinstance(result, UserModel)
    assert result.ID_USER == user.ID_USER

@patch("services.authentication_service.use_cases.authentication_use_case.input")
@patch("services.authentication_service.use_cases.authentication_use_case.AuthenticationController")
def test_authentication_endpoint_login_fail_then_register_success(mock_controller_cls, mock_input, use_case):
    mock_controller = mock_controller_cls.return_value
    mock_controller.login.return_value = None
    user = make_user(99)
    mock_controller.register.return_value = user
    # login fail, then register
    mock_input.side_effect = [
        '1', 'fail@email.com', 'wrongpass',  # login fail
        '2', 'New User', 'new@email.com', 'newpass'
    ]
    with patch("builtins.print"):
        result = use_case.authentication_endpoint()
    assert isinstance(result, UserModel)
    assert result.ID_USER == user.ID_USER

@patch("services.authentication_service.use_cases.authentication_use_case.input")
@patch("services.authentication_service.use_cases.authentication_use_case.AuthenticationController")
def test_authentication_endpoint_invalid_option_then_login_success(mock_controller_cls, mock_input, use_case):
    mock_controller = mock_controller_cls.return_value
    user = make_user(7)
    mock_controller.login.return_value = user
    # invalid option, then login
    mock_input.side_effect = [
        'x',  # invalid
        '1', 'user@email.com', 'pass'
    ]
    with patch("builtins.print"):
        result = use_case.authentication_endpoint()
    assert isinstance(result, UserModel)
    assert result.ID_USER == user.ID_USER

@patch("services.authentication_service.use_cases.authentication_use_case.input")
@patch("services.authentication_service.use_cases.authentication_use_case.AuthenticationController")
def test_authentication_endpoint_register_success(mock_controller_cls, mock_input, use_case):
    mock_controller = mock_controller_cls.return_value
    user = make_user(55)
    mock_controller.register.return_value = user
    mock_input.side_effect = ['2', 'Test Name', 'test@reg.com', 'regpass']
    with patch("builtins.print"):
        result = use_case.authentication_endpoint()
    assert isinstance(result, UserModel)
    assert result.ID_USER == user.ID_USER