from pydantic import BaseModel
from typing import List


class LegislatorBaseSummary(BaseModel):
    legislator_id: int
    legislator_name: str
    supported_bills_count: int
    opposed_bills_count: int


class LegislatorSummaryDetail(BaseModel):
    opposed: List[str]
    supported: List[str]


class LegislatorSummary(LegislatorBaseSummary):
    legislator_id: int
    legislator_name: str
    supported_bills_count: int
    opposed_bills_count: int

    detail: LegislatorSummaryDetail
