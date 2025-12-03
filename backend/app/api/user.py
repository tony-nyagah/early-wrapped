"""
User API Router - Endpoints for fetching user's Spotify data
"""

import logging
from typing import Optional

from fastapi import APIRouter, HTTPException, Query, Request

from app.services.spotify import SpotifyService

logger = logging.getLogger(__name__)

router = APIRouter()


def get_spotify_service(request: Request) -> SpotifyService:
    """
    Helper function to get Spotify service with access token from cookie

    Args:
        request: FastAPI request object

    Returns:
        SpotifyService: Initialized Spotify service

    Raises:
        HTTPException: If user is not authenticated
    """
    access_token = request.cookies.get("spotify_access_token")

    if not access_token:
        raise HTTPException(
            status_code=401,
            detail="Not authenticated. Please login with Spotify.",
        )

    return SpotifyService(access_token=access_token)


@router.get("/profile")
async def get_user_profile(request: Request):
    """
    Get current user's Spotify profile

    Returns:
        dict: User profile information
    """
    try:
        spotify = get_spotify_service(request)
        profile = spotify.get_current_user()

        return {
            "success": True,
            "data": profile,
        }

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error fetching user profile: {e}")
        raise HTTPException(status_code=500, detail="Failed to fetch user profile")


@router.get("/top-tracks")
async def get_top_tracks(
    request: Request,
    time_range: str = Query(
        "medium_term",
        description="Time range: short_term (4 weeks), medium_term (6 months), long_term (all time)",
    ),
    limit: int = Query(20, ge=1, le=50, description="Number of tracks to return"),
    offset: int = Query(0, ge=0, description="Index of first track to return"),
):
    """
    Get user's top tracks

    Args:
        time_range: Time range for top tracks (short_term, medium_term, long_term)
        limit: Number of tracks to return (1-50)
        offset: Offset for pagination

    Returns:
        dict: Top tracks data
    """
    try:
        # Validate time_range
        valid_ranges = ["short_term", "medium_term", "long_term"]
        if time_range not in valid_ranges:
            raise HTTPException(
                status_code=400,
                detail=f"Invalid time_range. Must be one of: {', '.join(valid_ranges)}",
            )

        spotify = get_spotify_service(request)
        tracks = spotify.get_top_tracks(time_range=time_range, limit=limit, offset=offset)

        return {
            "success": True,
            "time_range": time_range,
            "limit": limit,
            "offset": offset,
            "total": tracks.get("total", 0),
            "data": tracks.get("items", []),
        }

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error fetching top tracks: {e}")
        raise HTTPException(status_code=500, detail="Failed to fetch top tracks")


@router.get("/top-artists")
async def get_top_artists(
    request: Request,
    time_range: str = Query(
        "medium_term",
        description="Time range: short_term (4 weeks), medium_term (6 months), long_term (all time)",
    ),
    limit: int = Query(20, ge=1, le=50, description="Number of artists to return"),
    offset: int = Query(0, ge=0, description="Index of first artist to return"),
):
    """
    Get user's top artists

    Args:
        time_range: Time range for top artists (short_term, medium_term, long_term)
        limit: Number of artists to return (1-50)
        offset: Offset for pagination

    Returns:
        dict: Top artists data
    """
    try:
        # Validate time_range
        valid_ranges = ["short_term", "medium_term", "long_term"]
        if time_range not in valid_ranges:
            raise HTTPException(
                status_code=400,
                detail=f"Invalid time_range. Must be one of: {', '.join(valid_ranges)}",
            )

        spotify = get_spotify_service(request)
        artists = spotify.get_top_artists(time_range=time_range, limit=limit, offset=offset)

        return {
            "success": True,
            "time_range": time_range,
            "limit": limit,
            "offset": offset,
            "total": artists.get("total", 0),
            "data": artists.get("items", []),
        }

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error fetching top artists: {e}")
        raise HTTPException(status_code=500, detail="Failed to fetch top artists")


@router.get("/recently-played")
async def get_recently_played(
    request: Request,
    limit: int = Query(20, ge=1, le=50, description="Number of tracks to return"),
    after: Optional[int] = Query(
        None, description="Unix timestamp in ms - return tracks after this time"
    ),
    before: Optional[int] = Query(
        None, description="Unix timestamp in ms - return tracks before this time"
    ),
):
    """
    Get user's recently played tracks

    Args:
        limit: Number of tracks to return (1-50)
        after: Unix timestamp in milliseconds
        before: Unix timestamp in milliseconds

    Returns:
        dict: Recently played tracks data
    """
    try:
        spotify = get_spotify_service(request)
        tracks = spotify.get_recently_played(limit=limit, after=after, before=before)

        return {
            "success": True,
            "limit": limit,
            "data": tracks.get("items", []),
            "cursors": tracks.get("cursors", {}),
        }

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error fetching recently played tracks: {e}")
        raise HTTPException(status_code=500, detail="Failed to fetch recently played tracks")


@router.get("/saved-tracks")
async def get_saved_tracks(
    request: Request,
    limit: int = Query(20, ge=1, le=50, description="Number of tracks to return"),
    offset: int = Query(0, ge=0, description="Index of first track to return"),
):
    """
    Get user's saved tracks (liked songs)

    Args:
        limit: Number of tracks to return (1-50)
        offset: Offset for pagination

    Returns:
        dict: Saved tracks data
    """
    try:
        spotify = get_spotify_service(request)
        tracks = spotify.get_saved_tracks(limit=limit, offset=offset)

        return {
            "success": True,
            "limit": limit,
            "offset": offset,
            "total": tracks.get("total", 0),
            "data": tracks.get("items", []),
        }

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error fetching saved tracks: {e}")
        raise HTTPException(status_code=500, detail="Failed to fetch saved tracks")


@router.get("/playlists")
async def get_user_playlists(
    request: Request,
    limit: int = Query(20, ge=1, le=50, description="Number of playlists to return"),
    offset: int = Query(0, ge=0, description="Index of first playlist to return"),
):
    """
    Get user's playlists

    Args:
        limit: Number of playlists to return (1-50)
        offset: Offset for pagination

    Returns:
        dict: User playlists data
    """
    try:
        spotify = get_spotify_service(request)
        playlists = spotify.get_user_playlists(limit=limit, offset=offset)

        return {
            "success": True,
            "limit": limit,
            "offset": offset,
            "total": playlists.get("total", 0),
            "data": playlists.get("items", []),
        }

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error fetching user playlists: {e}")
        raise HTTPException(status_code=500, detail="Failed to fetch user playlists")


@router.get("/audio-features")
async def get_audio_features(
    request: Request,
    track_ids: str = Query(..., description="Comma-separated list of Spotify track IDs"),
):
    """
    Get audio features for multiple tracks

    Args:
        track_ids: Comma-separated track IDs (max 100)

    Returns:
        dict: Audio features for tracks
    """
    try:
        # Parse track IDs from comma-separated string
        track_id_list = [tid.strip() for tid in track_ids.split(",") if tid.strip()]

        if not track_id_list:
            raise HTTPException(status_code=400, detail="No track IDs provided")

        if len(track_id_list) > 100:
            raise HTTPException(
                status_code=400,
                detail="Maximum 100 track IDs allowed per request",
            )

        spotify = get_spotify_service(request)
        features = spotify.get_audio_features(track_id_list)

        return {
            "success": True,
            "count": len(features),
            "data": features,
        }

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error fetching audio features: {e}")
        raise HTTPException(status_code=500, detail="Failed to fetch audio features")


@router.get("/track/{track_id}")
async def get_track(request: Request, track_id: str):
    """
    Get a specific track by ID

    Args:
        track_id: Spotify track ID

    Returns:
        dict: Track data
    """
    try:
        spotify = get_spotify_service(request)
        track = spotify.get_track(track_id)

        return {
            "success": True,
            "data": track,
        }

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error fetching track: {e}")
        raise HTTPException(status_code=500, detail="Failed to fetch track")


@router.get("/artist/{artist_id}")
async def get_artist(request: Request, artist_id: str):
    """
    Get a specific artist by ID

    Args:
        artist_id: Spotify artist ID

    Returns:
        dict: Artist data
    """
    try:
        spotify = get_spotify_service(request)
        artist = spotify.get_artist(artist_id)

        return {
            "success": True,
            "data": artist,
        }

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error fetching artist: {e}")
        raise HTTPException(status_code=500, detail="Failed to fetch artist")
