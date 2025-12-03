"""
Authentication Schemas - Pydantic models for auth-related data
"""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class TokenData(BaseModel):
    """Schema for token data stored in session/JWT"""

    access_token: str
    refresh_token: str
    expires_at: int  # Unix timestamp
    token_type: str = "Bearer"
    scope: str


class UserProfile(BaseModel):
    """Schema for Spotify user profile data"""

    id: str = Field(..., description="Spotify user ID")
    display_name: Optional[str] = Field(None, description="User's display name")
    email: Optional[str] = Field(None, description="User's email address")
    country: Optional[str] = Field(None, description="User's country code")
    product: Optional[str] = Field(None, description="User's subscription type (free/premium)")
    images: list = Field(default_factory=list, description="User profile images")
    followers: Optional[dict] = Field(None, description="Follower information")
    external_urls: Optional[dict] = Field(None, description="External URLs")

    class Config:
        json_schema_extra = {
            "example": {
                "id": "spotify_user_123",
                "display_name": "John Doe",
                "email": "john@example.com",
                "country": "US",
                "product": "premium",
                "images": [{"url": "https://i.scdn.co/image/abc123", "height": 300, "width": 300}],
                "followers": {"total": 42},
                "external_urls": {"spotify": "https://open.spotify.com/user/spotify_user_123"},
            }
        }


class AuthResponse(BaseModel):
    """Schema for authentication response"""

    access_token: str = Field(..., description="Access token for Spotify API")
    token_type: str = Field("Bearer", description="Token type")
    expires_in: int = Field(..., description="Seconds until token expires")
    user: UserProfile = Field(..., description="User profile information")

    class Config:
        json_schema_extra = {
            "example": {
                "access_token": "BQC...",
                "token_type": "Bearer",
                "expires_in": 3600,
                "user": {
                    "id": "spotify_user_123",
                    "display_name": "John Doe",
                    "email": "john@example.com",
                },
            }
        }


class LoginRequest(BaseModel):
    """Schema for login request"""

    state: Optional[str] = Field(None, description="State parameter for CSRF protection")


class CallbackRequest(BaseModel):
    """Schema for OAuth callback request"""

    code: str = Field(..., description="Authorization code from Spotify")
    state: Optional[str] = Field(None, description="State parameter for CSRF protection")


class LogoutResponse(BaseModel):
    """Schema for logout response"""

    message: str = Field(..., description="Logout confirmation message")
    success: bool = Field(True, description="Logout success status")


class TokenRefreshRequest(BaseModel):
    """Schema for token refresh request"""

    refresh_token: str = Field(..., description="Refresh token")


class TokenRefreshResponse(BaseModel):
    """Schema for token refresh response"""

    access_token: str = Field(..., description="New access token")
    token_type: str = Field("Bearer", description="Token type")
    expires_in: int = Field(..., description="Seconds until token expires")
    scope: str = Field(..., description="Token scopes")
