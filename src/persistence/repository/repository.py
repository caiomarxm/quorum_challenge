from src.config.settings import settings

from src.persistence.entity.models import Bill, Legislator, Vote, VoteResult
from src.persistence.repository.csv_reader import parse_csv_to_model


bills = list(
    parse_csv_to_model(file_path=settings.BILLS_CSV_FILE_PATH, target_model=Bill)
)

legislators = list(
    parse_csv_to_model(
        file_path=settings.LEGISLATORS_CSV_FILE_PATH, target_model=Legislator
    )
)

votes = list(parse_csv_to_model(file_path=settings.VOTES_FILE_PATH, target_model=Vote))

vote_results = list(
    parse_csv_to_model(
        file_path=settings.VOTE_RESULTS_CSV_FILE_PATH, target_model=VoteResult
    )
)


def get_legislator(legislator_id: int):
    """
    Searches for a legislator with the provided legislator_id.

    Args:
        legislator_id (int): The ID of the legislator to find.

    Returns:
        Legislator: The legislator object with the matching ID, if found.

    Raises:
        IndexError: If no legislator is found with the provided ID.
    """

    def find_legislator_with_id(legislator: Legislator):
        return legislator.id == legislator_id

    try:
        return next(filter(find_legislator_with_id, legislators))
    except StopIteration:
        raise IndexError(f"No legislator was found with id {legislator_id}")


def get_vote_results_for_legislator(legislator_id: int):
    """
    Retrieves all vote results for a given legislator.

    Args:
        legislator_id (int): The ID of the legislator whose vote results are to be retrieved.

    Returns:
        list: A list of vote results where the legislator's ID matches the provided legislator_id.
    """
    return [
        vote_result
        for vote_result in vote_results
        if vote_result.legislator_id == legislator_id
    ]


def get_bill(bill_id: int):
    """
    Searches for a bill with the provided bill_id.

    Args:
        bill_id (int): The ID of the bill to find.

    Returns:
        Bill: The Bill object with the matching ID, if found.

    Raises:
        IndexError: If no bill is found with the provided ID.
    """

    def is_bill_with_id(bill: Bill):
        return bill.id == bill_id

    try:
        return next(filter(is_bill_with_id, bills))
    except StopIteration:
        raise IndexError(f"No bill was found with id {bill_id}")


def get_vote_results_for_bill(bill_id: int):
    """
    Retrieves the vote results to a given bill.

    Args:
        bill_id (int): The ID of the bill to search vote results for.

    Returns:
        List[VoteResults]: The vote results for the bill.
    """

    def is_vote_for_bill(vote: Vote):
        return vote.bill_id == bill_id

    bill_vote_event: Vote = next(filter(is_vote_for_bill, votes))

    return [
        vote_result
        for vote_result in vote_results
        if vote_result.vote_id == bill_vote_event.id
    ]
