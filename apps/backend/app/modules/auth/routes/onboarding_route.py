from fastapi import APIRouter

onboarding_route = APIRouter(prefix="/onboarding", tags=["Onboarding"])


@onboarding_route.post("/")
def start_onboarding(): ...
