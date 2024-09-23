from fastapi import APIRouter
from typing import List

from src.api.dto.legislator_summary import (
    LegislatorSummary,
    LegislatorSummaryDetail,
    LegislatorBaseSummary,
)
from src.api.dto.bill_summary import BillSummary, BillSummaryDetail, BillBaseSummary

from src.persistence.repository.repository import (
    legislators,
    bills,
    get_bill,
    get_legislator,
    get_vote_results_for_bill,
    get_vote_results_for_legislator,
    get_bill_for_vote_event,
)

router = APIRouter()


@router.get("/legislators/{legislator_id}")
def get_legislator_summary(
    legislator_id: int, include_details: bool = False
) -> LegislatorBaseSummary | LegislatorSummary:
    legislator = get_legislator(legislator_id=legislator_id)
    legislator_vote_results = get_vote_results_for_legislator(
        legislator_id=legislator_id
    )

    supported_bills = [
        vote_result for vote_result in legislator_vote_results if vote_result.voted_yes
    ]
    opposed_bills = [
        vote_result
        for vote_result in legislator_vote_results
        if not vote_result.voted_yes
    ]

    legislator_summary = LegislatorBaseSummary(
        legislator_id=legislator_id,
        legislator_name=legislator.name,
        supported_bills_count=len(supported_bills),
        opposed_bills_count=len(opposed_bills),
    )

    if not include_details:
        return legislator_summary

    return LegislatorSummary(
        **legislator_summary.model_dump(),
        detail=LegislatorSummaryDetail(
            opposed=[
                get_bill_for_vote_event(vote_result.vote_id).title
                for vote_result in opposed_bills
            ],
            supported=[
                get_bill_for_vote_event(vote_result.vote_id).title
                for vote_result in supported_bills
            ],
        ),
    )


@router.get("/legislators")
def get_all_legislators_summary() -> List[LegislatorBaseSummary]:
    return [
        get_legislator_summary(legislator_id=legislator.id)
        for legislator in legislators
    ]


@router.get("/bills/{bill_id}")
def get_bill_summary(bill_id: int, include_details: bool = False):
    bill = get_bill(bill_id=bill_id)
    vote_results = get_vote_results_for_bill(bill_id=bill_id)

    sponsor = get_legislator(legislator_id=bill.sponsor_id)

    supporters = [vote_result for vote_result in vote_results if vote_result.voted_yes]
    opposers = [
        vote_result for vote_result in vote_results if not vote_result.voted_yes
    ]

    bill_summary = BillBaseSummary(
        bill_id=bill.id,
        bill_title=bill.title,
        bill_opposers_count=len(opposers),
        bill_supporters_count=len(supporters),
        bill_primary_sponsor=sponsor.name if sponsor else "Sponsor wasn't found",
    )

    if not include_details:
        return bill_summary

    return BillSummary(
        **bill_summary.model_dump(),
        detail=BillSummaryDetail(
            opposers=[
                get_legislator(opposer.legislator_id).name for opposer in opposers
            ],
            supporters=[
                get_legislator(supporter.legislator_id).name for supporter in supporters
            ],
        ),
    )


@router.get("/legislators")
def get_all_bills_summary() -> List[BillBaseSummary]:
    return [get_bill_summary(bill_id=bill.id) for bill in bills]
