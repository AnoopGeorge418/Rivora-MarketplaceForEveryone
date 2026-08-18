from fastapi import APIRouter

from .login_route import login_router
from .signup_route import signup_router
from .session_route import session_router
from .resetpass_route import resetpass_router
from .onboarding_route import onboarding_route

# route instance
auth_route = APIRouter(prefix="/auth", tags=["Authentication"])

# register all auth routes here
auth_route.include_router(login_router)
auth_route.include_router(signup_router)
auth_route.include_router(session_router)
auth_route.include_router(resetpass_router)
auth_route.include_router(onboarding_route)
