from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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


# Include routers
app.include_router(auth_router.router, prefix="/auth", tags=["authentication"])
app.include_router(user_router.router, prefix="/api/user", tags=["user"])

# Analytics router will be added in Phase 2
# from app.api import analytics
# app.include_router(analytics.router, prefix="/api/analytics", tags=["analytics"])
