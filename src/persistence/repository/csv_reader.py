import csv
from pydantic import BaseModel
from typing import Optional


def parse_csv_to_model(file_path: str, target_entity: Optional[BaseModel] = None):
    with open(file=file_path, mode="r") as file:
        content = csv.reader(file, delimiter=",")
        headers = next(content)
        for row in content:
            row_dict = dict(zip(headers, row))
            if target_entity:
                yield target_entity.model_validate(row_dict)
            else:
                yield row_dict
