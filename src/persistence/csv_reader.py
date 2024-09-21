import csv
from pydantic import BaseModel
from typing import Optional, List


def read_csv(file_path: str, target_entity: Optional[BaseModel] = None):
    with open(file=file_path, mode="r") as file:
        content = csv.reader(csvfile=file, delimiter=",")
