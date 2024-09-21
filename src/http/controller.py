from fastapi import APIRouter

from src.http.dto.legislator_summary import (
    LegislatorSummary,
    LegislatorSummaryDetail,
    LegislatorBaseSummary,
)
from src.persistence.repository.repository import (
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
