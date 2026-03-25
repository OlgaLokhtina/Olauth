from fastapi import APIRouter

from schemes.users import HealthCheckResponse

user_rout = APIRouter(prefix="/api")


@user_rout.get("/healthcheck")
def healthcheck() -> HealthCheckResponse:
    h = HealthCheckResponse(success=True)
    return h
