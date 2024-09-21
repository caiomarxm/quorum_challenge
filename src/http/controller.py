from fastapi import APIRouter

router = APIRouter()


@router.get("/legislators")
def get_legislators():
    pass
