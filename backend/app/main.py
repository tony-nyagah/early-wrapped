from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pathlib import Path

from app.api import user as user_router
from app.auth import router as auth_router
from app.config import settings

app = FastAPI(
    title="Early Wrapped API",
    description="Spotify listening statistics API - Your music stats anytime!",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# Configure CORS
# Allow frontend origins plus Spotify authorization server
cors_origins = settings.cors_origins + [
    "https://accounts.spotify.com",
    "http://127.0.0.1:8000",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)


@app.get("/")
async def root():
    """Root endpoint - health check"""
    return {
        "message": "Welcome to Early Wrapped API",
        "status": "healthy",
        "version": "1.0.0",
        "docs": "/docs",
        "endpoints": {
            "auth": "/auth",
            "user": "/api/user",
        },
    }


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "ok"}


@app.get("/test")
async def test_page():
    """Serve test login page"""
    test_file = Path(__file__).parent.parent / "test_login.html"
    return FileResponse(test_file)


# Include routers
app.include_router(auth_router.router, prefix="/auth", tags=["authentication"])
app.include_router(user_router.router, prefix="/api/user", tags=["user"])

# Analytics router will be added in Phase 2
# from app.api import analytics
# app.include_router(analytics.router, prefix="/api/analytics", tags=["analytics"])
