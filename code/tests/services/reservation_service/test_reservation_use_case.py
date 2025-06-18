import pytest
from unittest.mock import patch, MagicMock
from services.reservation_service.use_cases.reservation_use_case import ReservationUseCase

@pytest.fixture
def use_case():
    return ReservationUseCase()

@pytest.fixture
def mock_session():
    mock = MagicMock()
    mock.ID_SESSION = "sess123"
    return mock

def test_cancel_reservation_endpoint_calls_controller(use_case):
    with patch.object(use_case.controller, "cancel_reservation") as mock_cancel:
        use_case.cancel_reservation_endpoint("ticket1")
        mock_cancel.assert_called_once_with("ticket1")

def test_buy_ticket_endpoint_calls_controller(use_case):
    with patch.object(use_case.controller, "buy_ticket") as mock_buy:
        use_case.buy_ticket_endpoint("ticket2")
        mock_buy.assert_called_once_with("ticket2")

def test_reservation_endpoint_choose_seat_and_exit(use_case, mock_session):
    with patch.object(use_case, "_show_menu", side_effect=['1', '2']), \
         patch.object(use_case, "choose_seat", return_value="seatA"), \
         patch("builtins.input", side_effect=['N']):
        result = use_case.reservation_endpoint(mock_session, "user1", "websess1")
        assert result == ["seatA"]

def test_reservation_endpoint_choose_multiple_seats(use_case, mock_session):
    with patch.object(use_case, "_show_menu", side_effect=['1', '1', '2']), \
         patch.object(use_case, "choose_seat", side_effect=["seatA", "seatB"]), \
         patch("builtins.input", side_effect=['S', 'N']):
        result = use_case.reservation_endpoint(mock_session, "user1", "websess1")
        assert result == ["seatA", "seatB"]

def test_reservation_endpoint_cancel_and_exit(use_case, mock_session):
    with patch.object(use_case, "_show_menu", return_value='2'):
        result = use_case.reservation_endpoint(mock_session, "user1", "websess1")
        assert result is None

def test_reservation_endpoint_invalid_option_then_exit(use_case, mock_session):
    with patch.object(use_case, "_show_menu", side_effect=['3', '2']), \
         patch("builtins.input", return_value='N'):
        result = use_case.reservation_endpoint(mock_session, "user1", "websess1")
        assert result is None

def test_choose_seat_success(use_case):
    with patch.object(use_case.controller, "show_available_seats") as mock_show, \
         patch("builtins.input", side_effect=["seat1"]), \
         patch.object(use_case.controller, "reserve_seat", return_value="seat1") as mock_reserve:
        result = use_case.choose_seat("sess1", "user1", "websess1")
        mock_show.assert_called_once_with("sess1")
        mock_reserve.assert_called_once_with("Seat1", "user1", "websess1")
        assert result == "seat1"

def test_choose_seat_retry_on_failure(use_case):
    with patch.object(use_case.controller, "show_available_seats"), \
         patch("builtins.input", side_effect=["seatX", "seatY"]), \
         patch.object(use_case.controller, "reserve_seat", side_effect=[None, "seatY"]) as mock_reserve:
        result = use_case.choose_seat("sess1", "user1", "websess1")
        assert mock_reserve.call_count == 2
        assert result == "seatY"