"""
Authentication Router - Handles Spotify OAuth flow
"""

import logging
import secrets
from typing import Optional

from fastapi import APIRouter, HTTPException, Query, Request, Response
from fastapi.responses import JSONResponse, RedirectResponse

from app.config import settings
from app.schemas.auth import (
    AuthResponse,
    CallbackRequest,
    LogoutResponse,
    TokenRefreshRequest,
    TokenRefreshResponse,
    UserProfile,
)
from app.services.spotify import SpotifyService

logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/login")
async def login(response: Response):
    """
    Initiate Spotify OAuth flow

    Returns a redirect to Spotify's authorization page
    """
    try:
        # Generate a random state for CSRF protection
        state = secrets.token_urlsafe(16)

        # Store state in cookie for verification in callback
        response.set_cookie(
            key="spotify_auth_state",
            value=state,
            httponly=True,
            max_age=600,  # 10 minutes
            samesite="lax",
        )

        # Get authorization URL from Spotify
        auth_url = SpotifyService.get_authorization_url(state)

        logger.info("Redirecting user to Spotify authorization")
        return RedirectResponse(url=auth_url)

    except Exception as e:
        logger.error(f"Error initiating login: {e}")
        raise HTTPException(status_code=500, detail="Failed to initiate login")


@router.get("/callback")
async def callback(
    request: Request,
    code: Optional[str] = Query(None, description="Authorization code from Spotify"),
    state: Optional[str] = Query(None, description="State parameter for CSRF protection"),
    error: Optional[str] = Query(None, description="Error from Spotify"),
):
    """
    Handle Spotify OAuth callback

    Exchanges authorization code for access token and fetches user profile
    """
    # Check for errors from Spotify
    if error:
        logger.error(f"Spotify authorization error: {error}")
        # Redirect to frontend with error
        return RedirectResponse(url=f"{settings.cors_origins[0]}/auth/error?error={error}")

    if not code:
        logger.error("No authorization code received")
        raise HTTPException(status_code=400, detail="No authorization code received")

    try:
        # Verify state parameter for CSRF protection
        stored_state = request.cookies.get("spotify_auth_state")
        if not stored_state or stored_state != state:
            logger.error("State mismatch - possible CSRF attack")
            raise HTTPException(status_code=400, detail="Invalid state parameter")

        # Exchange authorization code for access token
        logger.info("Exchanging authorization code for access token")
        token_info = SpotifyService.get_access_token(code)

        if not token_info or "access_token" not in token_info:
            raise HTTPException(status_code=400, detail="Failed to get access token")

        # Get user profile using access token
        spotify_service = SpotifyService(access_token=token_info["access_token"])
        user_data = spotify_service.get_current_user()

        # Create response with redirect to frontend
        frontend_url = settings.cors_origins[0]
        response = RedirectResponse(url=f"{frontend_url}/auth/success")

        # Store tokens in httponly cookies for security
        response.set_cookie(
            key="spotify_access_token",
            value=token_info["access_token"],
            httponly=True,
            max_age=token_info.get("expires_in", 3600),
            samesite="lax",
            secure=not settings.debug,  # Use secure cookies in production
        )

        response.set_cookie(
            key="spotify_refresh_token",
            value=token_info.get("refresh_token", ""),
            httponly=True,
            max_age=60 * 60 * 24 * 30,  # 30 days
            samesite="lax",
            secure=not settings.debug,
        )

        # Store user info in a separate cookie (not httponly so frontend can read it)
        response.set_cookie(
            key="user_profile",
            value=user_data.get("id", ""),
            max_age=60 * 60 * 24 * 30,  # 30 days
            samesite="lax",
            secure=not settings.debug,
        )

        # Clear the state cookie
        response.delete_cookie("spotify_auth_state")

        logger.info(f"User {user_data.get('id')} authenticated successfully")
        return response

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error in callback: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Authentication failed")


@router.post("/refresh", response_model=TokenRefreshResponse)
async def refresh_token(
    request: Request,
    response: Response,
):
    """
    Refresh an expired access token using refresh token from cookie
    """
    try:
        # Get refresh token from cookie
        refresh_token = request.cookies.get("spotify_refresh_token")

        if not refresh_token:
            raise HTTPException(status_code=401, detail="No refresh token found")

        # Request new access token
        logger.info("Refreshing access token")
        token_info = SpotifyService.refresh_access_token(refresh_token)

        if not token_info or "access_token" not in token_info:
            raise HTTPException(status_code=400, detail="Failed to refresh token")

        # Update access token cookie
        response.set_cookie(
            key="spotify_access_token",
            value=token_info["access_token"],
            httponly=True,
            max_age=token_info.get("expires_in", 3600),
            samesite="lax",
            secure=not settings.debug,
        )

        # If a new refresh token was provided, update it
        if "refresh_token" in token_info:
            response.set_cookie(
                key="spotify_refresh_token",
                value=token_info["refresh_token"],
                httponly=True,
                max_age=60 * 60 * 24 * 30,  # 30 days
                samesite="lax",
                secure=not settings.debug,
            )

        return TokenRefreshResponse(
            access_token=token_info["access_token"],
            token_type="Bearer",
            expires_in=token_info.get("expires_in", 3600),
            scope=token_info.get("scope", ""),
        )

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error refreshing token: {e}")
        raise HTTPException(status_code=500, detail="Failed to refresh token")


@router.post("/logout", response_model=LogoutResponse)
async def logout(response: Response):
    """
    Logout user by clearing authentication cookies
    """
    try:
        # Clear all auth-related cookies
        response.delete_cookie("spotify_access_token")
        response.delete_cookie("spotify_refresh_token")
        response.delete_cookie("user_profile")
        response.delete_cookie("spotify_auth_state")

        logger.info("User logged out successfully")
        return LogoutResponse(
            message="Logged out successfully",
            success=True,
        )

    except Exception as e:
        logger.error(f"Error during logout: {e}")
        raise HTTPException(status_code=500, detail="Logout failed")


@router.get("/me", response_model=UserProfile)
async def get_current_user(request: Request):
    """
    Get current authenticated user's profile
    """
    try:
        # Get access token from cookie
        access_token = request.cookies.get("spotify_access_token")

        if not access_token:
            raise HTTPException(status_code=401, detail="Not authenticated")

        # Fetch user profile from Spotify
        spotify_service = SpotifyService(access_token=access_token)
        user_data = spotify_service.get_current_user()

        return UserProfile(**user_data)

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error fetching user profile: {e}")
        raise HTTPException(status_code=500, detail="Failed to fetch user profile")


@router.get("/check")
async def check_auth(request: Request):
    """
    Check if user is authenticated

    Returns authentication status
    """
    access_token = request.cookies.get("spotify_access_token")

    return {
        "authenticated": bool(access_token),
        "message": "User is authenticated" if access_token else "User is not authenticated",
    }
