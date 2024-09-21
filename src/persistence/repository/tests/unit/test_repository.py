import pytest
from src.persistence.entity.models import Bill, Legislator, Vote, VoteResult
from src.persistence.repository.repository import (
    get_legislator,
    get_vote_results_for_legislator,
    get_bill,
    get_vote_results_for_bill,
)

mock_bills = [
    Bill(id=1, title="Bill 1", sponsor_id=1),
    Bill(id=2, title="Bill 2", sponsor_id=2),
]

mock_legislators = [
    Legislator(id=1, name="Legislator 1"),
    Legislator(id=2, name="Legislator 2"),
]

mock_votes = [
    Vote(id=1, bill_id=1),
    Vote(id=2, bill_id=2),
]

mock_vote_results = [
    VoteResult(id=1, legislator_id=1, vote_id=1, vote_type="1"),
    VoteResult(id=2, legislator_id=1, vote_id=2, vote_type="2"),
    VoteResult(id=3, legislator_id=2, vote_id=1, vote_type="1"),
]


@pytest.fixture
def patch_data(monkeypatch):
    monkeypatch.setattr("src.persistence.repository.repository.bills", mock_bills)
    monkeypatch.setattr(
        "src.persistence.repository.repository.legislators", mock_legislators
    )
    monkeypatch.setattr("src.persistence.repository.repository.votes", mock_votes)
    monkeypatch.setattr(
        "src.persistence.repository.repository.vote_results", mock_vote_results
    )


def test_get_legislator_found(patch_data):
    legislator = get_legislator(1)
    assert legislator.id == 1
    assert legislator.name == "Legislator 1"


def test_get_legislator_not_found(patch_data):
    with pytest.raises(IndexError):
        get_legislator(999)


def test_get_vote_results_for_legislator(patch_data):
    results = get_vote_results_for_legislator(1)
    assert len(results) == 2
    assert results[0].legislator_id == 1
    assert results[1].legislator_id == 1


def test_get_vote_results_for_nonexistent_legislator(patch_data):
    results = get_vote_results_for_legislator(999)
    assert len(results) == 0


def test_get_bill_found(patch_data):
    bill = get_bill(1)
    assert bill.id == 1
    assert bill.title == "Bill 1"


def test_get_bill_not_found(patch_data):
    with pytest.raises(IndexError):
        get_bill(999)


def test_get_vote_results_for_bill(patch_data):
    results = get_vote_results_for_bill(1)
    assert len(results) == 2
    assert results[0].vote_id == 1
    assert results[1].vote_id == 1


def test_get_vote_results_for_nonexistent_bill(patch_data):
    with pytest.raises(StopIteration):
        get_vote_results_for_bill(999)
