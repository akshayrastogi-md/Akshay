from fastapi import APIRouter

from app.api.v1.endpoints import health, prospects, campaigns

api_router = APIRouter()
api_router.include_router(health.router, tags=["health"])
api_router.include_router(prospects.router, prefix="/prospects", tags=["prospects"])
api_router.include_router(campaigns.router, prefix="/campaigns", tags=["campaigns"])
