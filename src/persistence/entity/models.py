from pydantic import BaseModel, computed_field
from typing import Literal


class Bill(BaseModel):
    id: int
    title: str
    sponsor_id: int


class Legislator(BaseModel):
    id: int
    name: str


class Vote(BaseModel):
    id: int
    bill_id: int


class VoteResult(BaseModel):
    id: int
    legislator_id: int
    vote_id: int
    vote_type: Literal["1", "2"]

    @computed_field
    @property
    def voted_yes(self) -> bool:
        return self.vote_type == "1"
