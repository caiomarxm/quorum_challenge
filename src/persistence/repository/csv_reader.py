import csv
from pydantic import BaseModel
from typing import Optional


def parse_csv_to_model(file_path: str, target_model: Optional[BaseModel] = None):
    with open(file=file_path, mode="r") as file:
        content = csv.reader(file, delimiter=",")
        headers = next(content)
        for row in content:
            row_dict = dict(zip(headers, row))
            if target_model:
                yield target_model.model_validate(row_dict)
            else:
                yield row_dict
