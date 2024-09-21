from pydantic import BaseModel


class Bill(BaseModel):
    id: int
    title: str
    sponsor_id: int
