import pytest
from services.receipt_service.use_cases.receipt_use_case import ReceiptUseCase

def test_receipt_endpoint_returns_success_message(capsys):
    use_case = ReceiptUseCase()
    result = use_case.receipt_endpoint([])
    captured = capsys.readouterr()
    assert "Gerando recibo..." in captured.out
    assert "Enviando recibo por e-mail..." in captured.out
    assert "Recibo enviado com sucesso!" in captured.out
    assert result == "Recibo enviado com sucesso!"