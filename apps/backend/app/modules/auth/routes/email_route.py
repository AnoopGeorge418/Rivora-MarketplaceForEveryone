from fastapi import APIRouter

email_auth_route = APIRouter(prefix="/selection")

@email_auth_route.get("/")
def get_something():
    return {
        "status": "cool"
    }
