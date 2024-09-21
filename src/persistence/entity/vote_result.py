from pydantic import BaseModel


class VoteResult(BaseModel):
    id: int
    legislator_id: int
    vote_id: int
    vote_type: int
