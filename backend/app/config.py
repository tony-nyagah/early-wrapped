from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    """Application settings loaded from environment variables"""

    # Spotify API Configuration
    spotify_client_id: str
    spotify_client_secret: str
    spotify_redirect_uri: str = "http://127.0.0.1:8000/auth/callback"

    # Application Security
    secret_key: str
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 60 * 24  # 24 hours

    # Database Configuration
    database_url: str = "sqlite:///./early_wrapped.db"

    # Application Settings
    debug: bool = True
    app_name: str = "Early Wrapped"
    api_v1_prefix: str = "/api/v1"

    # CORS Settings
    allowed_origins: str = "http://localhost:3000,http://127.0.0.1:3000"

    # Spotify API Scopes
    spotify_scopes: str = (
        "user-read-private "
        "user-read-email "
        "user-top-read "
        "user-read-recently-played "
        "user-library-read "
        "playlist-read-private"
    )

    class Config:
        env_file = ".env"
        case_sensitive = False

    @property
    def cors_origins(self) -> List[str]:
        """Parse CORS origins from comma-separated string"""
        return [origin.strip() for origin in self.allowed_origins.split(",")]


# Global settings instance
settings = Settings()
