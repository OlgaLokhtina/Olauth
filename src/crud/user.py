from fastapi import APIRouter
from typing import Dict


user_router = APIRouter(prefix="/api")


@user_router.get("/healthcheck")
def healthcheck() -> Dict:
    return {"success": True}
