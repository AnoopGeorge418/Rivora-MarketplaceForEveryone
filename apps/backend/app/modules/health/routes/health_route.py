from fastapi import APIRouter

health_route = APIRouter(tags=["Health route"])


@health_route.get("/")
def get_health():
    return {"Progress": "Faststrapy Configured entire project", "status": "healthly"}
