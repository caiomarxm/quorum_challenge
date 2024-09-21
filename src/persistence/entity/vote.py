from pydantic import BaseModel


class Vote(BaseModel):
    id: int
    bill_id: int
