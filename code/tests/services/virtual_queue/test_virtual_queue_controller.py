import pytest
from unittest.mock import patch, MagicMock
from services.virtual_queue_service.controller.virtual_queue_controller import VirtualQueueController
from services.virtual_queue_service.model.virtual_queue_model import VirtualQueueModel

@pytest.fixture
def controller():
    return VirtualQueueController()

@pytest.fixture
def sample_item():
    return VirtualQueueModel(ID_WEB_SESSION='sess1', ID_USER='user1')

@patch('services.virtual_queue_service.controller.virtual_queue_controller.CSVService')
def test_add_to_queue(mock_csv_service, controller, sample_item):
    mock_csv = mock_csv_service.return_value
    mock_csv.read_csv.return_value = []
    controller.add_to_queue(sample_item)
    mock_csv.write_csv.assert_called_once()
    args, kwargs = mock_csv.write_csv.call_args
    assert args[0] == 'repositories/virtual_queue'
    assert args[1] == 'virtual_queue.csv'
    assert sample_item in args[2]
    assert kwargs['header'] == ['ID_WEB_SESSION', 'ID_USER']

@patch('services.virtual_queue_service.virtual_queue_controller.CSVService')
def test_get_queue(mock_csv_service, controller):
    mock_csv = mock_csv_service.return_value
    mock_csv.read_csv.return_value = [{'ID_WEB_SESSION': 'sess1', 'ID_USER': 'user1'}]
    queue = controller._get_queue()
    assert queue == [{'ID_WEB_SESSION': 'sess1', 'ID_USER': 'user1'}]
    mock_csv.read_csv.assert_called_once_with('repositories/virtual_queue', 'virtual_queue.csv')

@patch('services.virtual_queue_service.virtual_queue_controller.CSVService')
@patch.object(VirtualQueueController, 'process_item')
def test_process_queue_calls_process_item(mock_process_item, mock_csv_service, controller):
    mock_csv = mock_csv_service.return_value
    mock_csv.read_csv.return_value = [{'ID_WEB_SESSION': 'sess1', 'ID_USER': 'user1'}]
    result = controller.process_queue()
    mock_process_item.assert_called_once()
    assert result == {'ID_WEB_SESSION': 'sess1', 'ID_USER': 'user1'}

@patch('services.virtual_queue_service.virtual_queue_controller.time.sleep', return_value=None)
def test_process_item_sleeps_and_prints(mock_sleep, controller, sample_item, capsys):
    controller.process_item(sample_item)
    mock_sleep.assert_called_once_with(60)
    captured = capsys.readouterr()
    assert f"Processing item: {sample_item}" in captured.out