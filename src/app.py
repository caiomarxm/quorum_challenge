from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles


from src.api.controller import router
from src.view import view


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(router=router, prefix="/api")
app.include_router(router=view.router)
