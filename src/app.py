from fastapi import FastAPI

from controllers.user import user_rout

app = FastAPI()

app.include_router(user_rout)
