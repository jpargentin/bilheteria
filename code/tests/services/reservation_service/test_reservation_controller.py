import pytest
from unittest.mock import MagicMock, patch
from services.reservation_service.controller.reservation_controller import ReservationController

class DummyTicket:
    def __init__(self, ID_TICKET, ID_SESSION, RESERVATION, TICKET_COORDENATES, tags, PRICE, BUY=False, ID_USER=None, ID_WEB_SESSION=None):
        self.ID_TICKET = ID_TICKET
        self.ID_SESSION = ID_SESSION
        self.RESERVATION = RESERVATION
        self.TICKET_COORDENATES = TICKET_COORDENATES
        self.tags = tags
        self.PRICE = PRICE
        self.BUY = BUY
        self.ID_USER = ID_USER
        self.ID_WEB_SESSION = ID_WEB_SESSION

@pytest.fixture
def controller():
    with patch('services.reservation_service.controller.reservation_controller.ReservationRepository') as MockRepo:
        repo = MockRepo.return_value
        return ReservationController()

def test_list_available_seats(controller):
    ticket1 = DummyTicket("1", "sess1", False, "[A,1,1]", "[VIP]", 100)
    ticket2 = DummyTicket("2", "sess1", True, "[A,2,1]", "[VIP]", 100)
    ticket3 = DummyTicket("3", "sess2", False, "[B,1,1]", "[NORMAL]", 80)
    controller.repository.get_tickets = MagicMock(return_value=[ticket1, ticket2, ticket3])
    available = controller._list_available_seats("sess1")
    assert available == [ticket1]

def test_show_available_seats_prints_available(capsys, controller):
    ticket = DummyTicket("1", "sess1", False, "[A,1,1]", "[VIP]", 100)
    controller._list_available_seats = MagicMock(return_value=[ticket])
    controller.show_available_seats("sess1")
    captured = capsys.readouterr()
    assert "Assentos disponiveis" in captured.out
    assert "ID: 1" in captured.out

def test_show_available_seats_prints_no_tickets(capsys, controller):
    controller._list_available_seats = MagicMock(return_value=[])
    controller.show_available_seats("sess1")
    captured = capsys.readouterr()
    assert "Infelizmente nossos ingressos para essa sessão ja esgotaram" in captured.out

def test_reserve_seat_success(controller):
    ticket = DummyTicket("1", "sess1", False, "[A,1,1]", "[VIP]", 100)
    controller._list_available_seats = MagicMock(return_value=[ticket])
    controller.repository.write_ticket = MagicMock()
    result = controller.reserve_seat("sess1", "1", "user1", "web1")
    assert result == ticket
    assert ticket.RESERVATION is True
    assert ticket.ID_USER == "user1"
    assert ticket.ID_WEB_SESSION == "web1"
    controller.repository.write_ticket.assert_called_once()

def test_reserve_seat_not_found(controller):
    controller._list_available_seats = MagicMock(return_value=[])
    controller.repository.write_ticket = MagicMock()
    result = controller.reserve_seat("sess1", "999", "user1", "web1")
    assert result is None
    controller.repository.write_ticket.assert_not_called()

def test_buy_ticket_success(controller):
    ticket = DummyTicket("1", "sess1", False, "[A,1,1]", "[VIP]", 100)
    controller.repository.get_tickets = MagicMock(return_value=[ticket])
    controller.repository.write_ticket = MagicMock()
    result = controller.buy_ticket("1")
    assert result == "1"
    assert ticket.BUY is True
    controller.repository.write_ticket.assert_called_once()

def test_buy_ticket_not_found(controller):
    controller.repository.get_tickets = MagicMock(return_value=[])
    controller.repository.write_ticket = MagicMock()
    result = controller.buy_ticket("999")
    assert result is None
    controller.repository.write_ticket.assert_not_called()

def test_cancel_reservation_success(controller):
    ticket = DummyTicket("1", "sess1", True, "[A,1,1]", "[VIP]", 100, BUY=True, ID_USER="user1", ID_WEB_SESSION="web1")
    controller.repository.get_tickets = MagicMock(return_value=[ticket])
    controller.repository.write_ticket = MagicMock()
    result = controller.cancel_reservation("1")
    assert result == "1"
    assert ticket.RESERVATION is False
    assert ticket.ID_USER is None
    assert ticket.ID_WEB_SESSION is None
    assert ticket.BUY is False
    controller.repository.write_ticket.assert_called_once()

def test_cancel_reservation_not_found(controller):
    controller.repository.get_tickets = MagicMock(return_value=[])
    controller.repository.write_ticket = MagicMock()
    result = controller.cancel_reservation("999")
    assert result is None
    controller.repository.write_ticket.assert_not_called()