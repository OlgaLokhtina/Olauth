from fastapi import FastAPI
from crud.user import user_router

app = FastAPI()

app.include_router(user_router)
