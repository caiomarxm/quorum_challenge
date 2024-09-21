import csv
from pydantic import BaseModel
from typing import Optional, TypeVar, Type, Iterator, Dict, Any


T = TypeVar("T", bound=BaseModel)


def parse_csv_to_model(
    file_path: str, target_model: Optional[Type[T]] = None
) -> Iterator[T | Dict[str, Any]]:
    """
    Parses a CSV file and yields each row as either a dictionary or an instance of the target_model.

    Args:
        file_path (str): The path to the CSV file.
        target_model (Optional[Type[T]]): A Pydantic model class to validate each row.

    Yields:
        Either a dictionary of the row's data or an instance of the target_model.
    """
    with open(file=file_path, mode="r") as file:
        content = csv.reader(file, delimiter=",")
        headers = next(content)
        for row in content:
            row_dict = dict(zip(headers, row))
            if target_model:
                yield target_model.model_validate(row_dict)
            else:
                yield row_dict
