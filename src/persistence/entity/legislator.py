from pydantic import BaseModel


class Legislator(BaseModel):
    id: int
    name: str
