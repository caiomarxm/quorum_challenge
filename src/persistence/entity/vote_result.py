from pydantic import BaseModel, computed_field
from typing import Literal


class VoteResult(BaseModel):
    id: int
    legislator_id: int
    vote_id: int
    vote_type: Literal[1, 2]

    @computed_field
    @property
    def voted_yes(self):
        return self.vote_type == 1
