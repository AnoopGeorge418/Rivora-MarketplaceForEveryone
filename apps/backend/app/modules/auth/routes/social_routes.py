from fastapi import APIRouter

social_auth_route = APIRouter(prefix="/selection")

@social_auth_route.get("/")
def get_something():
    return {
        "status": "cool"
    }
