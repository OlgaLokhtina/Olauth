from fastapi import APIRouter
from typing import Dict


user_rout = APIRouter(prefix="/api")


@user_rout.get("/healthcheck")
def healthcheck() -> Dict:
    return {"success": True}
