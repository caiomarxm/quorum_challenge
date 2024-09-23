from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


from src.api.controller import get_all_legislators_summary, get_all_bills_summary

templates = Jinja2Templates(directory="templates")


router = APIRouter()


@router.get("/legislators", response_class=HTMLResponse, name="legislators")
async def legislators_summary(request: Request):
    legislators = get_all_legislators_summary()

    return templates.TemplateResponse(
        "legislators.html", {"request": request, "legislators": legislators}
    )


@router.get("/bills", response_class=HTMLResponse, name="bills")
async def bills_summary(request: Request):
    bills = get_all_bills_summary()

    return templates.TemplateResponse(
        "bills.html", {"request": request, "bills": bills}
    )
