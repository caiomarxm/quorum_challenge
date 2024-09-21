from pydantic import BaseModel

from src.persistence.repository.csv_reader import parse_csv_to_model


SAMPLE_CSV_PATH = "src/persistence/repository/tests/fixtures/sample.csv"


class ContentRow(BaseModel):
    id: int
    name: str
    description: str


def test_read_csv_with_model():
    content = parse_csv_to_model(file_path=SAMPLE_CSV_PATH, target_model=ContentRow)
    for item in content:
        assert isinstance(item, ContentRow)


def test_read_csv_without_model():
    content = parse_csv_to_model(file_path=SAMPLE_CSV_PATH)
    for item in content:
        assert isinstance(item, dict)
        assert "id" in item.keys()
        assert "name" in item.keys()
        assert "description" in item.keys()
