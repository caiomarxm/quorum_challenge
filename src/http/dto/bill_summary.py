from pydantic import BaseModel
from typing import List


class BillBaseSummary(BaseModel):
    bill_id: int
    bill_title: str
    bill_supporters_count: int
    bill_opposers_count: int
    bill_primary_sponsor: str


class BillSummaryDetail(BaseModel):
    opposers: List[str]
    supporters: List[str]


class BillSummary(BillBaseSummary):
    bill_id: int
    bill_title: str
    bill_supporters_count: int
    bill_opposers_count: int

    detail: BillSummaryDetail
