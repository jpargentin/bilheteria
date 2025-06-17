import pytest
from unittest.mock import patch
from services.payment_service.use_cases.payment_use_case import PaymentUseCase

def test_payment_endpoint_returns_success_message(capsys):
    payment_use_case = PaymentUseCase()
    with patch("time.sleep", return_value=None):
        result = payment_use_case.payment_endpoint()
    captured = capsys.readouterr()
    assert "Iniciando processo de pagamento..." in captured.out
    assert "Processando pagamento..." in captured.out
    assert "Pagamento realizado com sucesso!" in captured.out
    assert result == "Pagamento realizado com sucesso!"