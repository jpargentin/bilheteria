import pytest
from unittest.mock import patch, MagicMock
from services.session_service.use_cases.session_use_case import SessionUseCase

class DummySession:
    def __init__(self, ID_SESSION, LOCAL, MOVIE, DATE):
        self.ID_SESSION = ID_SESSION
        self.LOCAL = LOCAL
        self.MOVIE = MOVIE
        self.DATE = DATE

@pytest.fixture
def dummy_sessions():
    return [
        DummySession("A1", "Sala 1", "Filme X", "2024-06-01 20:00"),
        DummySession("B2", "Sala 2", "Filme Y", "2024-06-02 21:00"),
    ]

@pytest.fixture
def use_case():
    return SessionUseCase()

def test_show_available_sessions_returns_sessions(use_case, dummy_sessions):
    use_case.controller.list_available_sessions = MagicMock(return_value=dummy_sessions)
    sessions = use_case.show_available_sessions()
    assert sessions == dummy_sessions

def test_show_available_sessions_raises_when_empty(use_case):
    use_case.controller.list_available_sessions = MagicMock(return_value=[])
    with pytest.raises(ValueError):
        use_case.show_available_sessions()

@patch("builtins.input", side_effect=["A1"])
def test_choose_session_success(mock_input, use_case, dummy_sessions):
    use_case.show_available_sessions = MagicMock(return_value=dummy_sessions)
    selected = use_case.choose_session()
    assert selected.ID_SESSION == "A1"

@patch("builtins.input", side_effect=["C3", "B2"])
def test_choose_session_retry_then_success(mock_input, use_case, dummy_sessions):
    use_case.show_available_sessions = MagicMock(return_value=dummy_sessions)
    selected = use_case.choose_session()
    assert selected.ID_SESSION == "B2"

@patch.object(SessionUseCase, "choose_session")
@patch.object(SessionUseCase, "_show_menu")
def test_session_endpoint_choose_session(mock_menu, mock_choose, use_case, dummy_sessions):
    mock_menu.side_effect = ["1"]
    dummy = dummy_sessions[0]
    mock_choose.return_value = dummy
    result = use_case.session_endpoint()
    assert result == dummy

@patch.object(SessionUseCase, "_show_menu")
def test_session_endpoint_exit(mock_menu, use_case):
    mock_menu.side_effect = ["2"]
    result = use_case.session_endpoint()
    assert result is None

@patch.object(SessionUseCase, "_show_menu")
def test_session_endpoint_invalid_option_then_exit(mock_menu, use_case):
    # First invalid, then exit
    mock_menu.side_effect = ["9", "2"]
    with patch("builtins.print") as mock_print:
        result = use_case.session_endpoint()
        assert result is None
        assert any("Opção inválida" in str(call) for call in mock_print.call_args_list)