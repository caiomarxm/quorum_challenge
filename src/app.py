from fastapi import FastAPI

from src.http.controller import router


app = FastAPI()

app.include_router(router=router, prefix="/api")
