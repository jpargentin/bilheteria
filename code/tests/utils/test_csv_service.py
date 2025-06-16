import tempfile
import pytest
from utils.csv_service import CSVService

class ConcreteCSVService(CSVService):
    def write_csv(self, directory, filename, data, header=None):
        super().write_csv(directory, filename, data, header)

    def read_csv(self, directory, filename, skip_header=True):
        return super().read_csv(directory, filename, skip_header)

@pytest.fixture
def csv_service():
    return ConcreteCSVService()

def test_write_and_read_csv_with_header(csv_service):
    with tempfile.TemporaryDirectory() as tmpdir:
        filename = "test.csv"
        header = ["col1", "col2"]
        data = [["a", "1"], ["b", "2"]]
        csv_service.write_csv(tmpdir, filename, data, header=header)
        result = csv_service.read_csv(tmpdir, filename, skip_header=True)
        assert result == data

def test_write_and_read_csv_without_header(csv_service):
    with tempfile.TemporaryDirectory() as tmpdir:
        filename = "test_no_header.csv"
        data = [["x", "10"], ["y", "20"]]
        csv_service.write_csv(tmpdir, filename, data)
        result = csv_service.read_csv(tmpdir, filename, skip_header=False)
        assert result == data

def test_read_csv_skip_header_false(csv_service):
    with tempfile.TemporaryDirectory() as tmpdir:
        filename = "test_header.csv"
        header = ["h1", "h2"]
        data = [["foo", "bar"]]
        csv_service.write_csv(tmpdir, filename, data, header=header)
        result = csv_service.read_csv(tmpdir, filename, skip_header=False)
        assert result[0] == header
        assert result[1] == data[0]