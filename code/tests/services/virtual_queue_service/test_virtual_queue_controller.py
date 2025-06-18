import pytest
from unittest.mock import MagicMock, patch
from services.virtual_queue_service.use_cases.virtual_queue_use_case import VirtualQueueUseCase
from services.virtual_queue_service.model.virtual_queue_model import VirtualQueueModel
from services.authentication_service.model.user_model import UserModel

@pytest.fixture
def mock_user():
    user = MagicMock(spec=UserModel)
    user.ID_USER = "user123"
    user.NAME = "João"
    return user

@pytest.fixture
def mock_controller(monkeypatch):
    controller = MagicMock()
    monkeypatch.setattr(
        "services.virtual_queue_service.use_cases.virtual_queue_use_case.VirtualQueueController",
        lambda: controller
    )
    return controller

def test_virtual_queue_endpoint_adds_to_queue_and_processes(monkeypatch, mock_user, mock_controller):
    use_case = VirtualQueueUseCase()
    id_web_session = "sess456"
    mock_controller.get_queue_position.return_value = 1

    monkeypatch.setattr("builtins.input", lambda _: "")

    monkeypatch.setattr("builtins.print", lambda *args, **kwargs: None)

    result = use_case.virtual_queue_endpoint(mock_user, id_web_session)

    assert isinstance(result, VirtualQueueModel)
    assert result.ID_WEB_SESSION == id_web_session
    assert result.ID_USER == mock_user.ID_USER
    mock_controller.add_to_queue.assert_called_once()
    mock_controller.get_queue_position.assert_called_once_with(id_web_session)
    mock_controller.process_queue.assert_called_once_with(id_web_session)