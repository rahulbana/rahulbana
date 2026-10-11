# ---------------------------------------------------------------------------
# Name:     Rahul Singh Bana
# Email:    bana.saa@gmail.com
# LinkedIn: https://www.linkedin.com/in/rahulsinghbana
# Repo:     https://github.com/rahulbana/rahulbana
# ---------------------------------------------------------------------------
"""Aggregate all API routers under the versioned prefix."""
from fastapi import APIRouter

from app.api.routes import articles, auth, export, generation, search, style

api_router = APIRouter()
api_router.include_router(auth.router)
api_router.include_router(articles.router)
api_router.include_router(generation.router)
api_router.include_router(search.router)
api_router.include_router(export.router)
api_router.include_router(style.router)
