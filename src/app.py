from fastapi import FastAPI
from crud.user import user_rout

app = FastAPI()

app.include_router(user_rout)
