"""
Spotify Service - Handles all interactions with Spotify Web API
"""

import logging
from datetime import datetime, timedelta
from typing import Any, Dict, List, Optional

import spotipy
from spotipy.oauth2 import SpotifyOAuth

from app.config import settings

logger = logging.getLogger(__name__)


class SpotifyService:
    """Service class for interacting with Spotify API"""

    def __init__(self, access_token: Optional[str] = None):
        """
        Initialize Spotify service with optional access token

        Args:
            access_token: User's Spotify access token
        """
        self.access_token = access_token
        self.client = None

        if access_token:
            self.client = spotipy.Spotify(auth=access_token)

    @staticmethod
    def get_auth_manager(state: Optional[str] = None) -> SpotifyOAuth:
        """
        Get SpotifyOAuth manager for authentication flow

        Args:
            state: Optional state parameter for OAuth flow

        Returns:
            SpotifyOAuth: Configured OAuth manager
        """
        return SpotifyOAuth(
            client_id=settings.spotify_client_id,
            client_secret=settings.spotify_client_secret,
            redirect_uri=settings.spotify_redirect_uri,
            scope=settings.spotify_scopes,
            state=state,
            cache_handler=None,  # We'll handle token storage ourselves
            show_dialog=True,  # Always show Spotify login dialog
        )

    @staticmethod
    def get_authorization_url(state: str) -> str:
        """
        Get the Spotify authorization URL

        Args:
            state: State parameter for CSRF protection

        Returns:
            str: Authorization URL
        """
        auth_manager = SpotifyService.get_auth_manager(state=state)
        return auth_manager.get_authorize_url()

    @staticmethod
    def get_access_token(code: str) -> Dict[str, Any]:
        """
        Exchange authorization code for access token

        Args:
            code: Authorization code from Spotify callback

        Returns:
            dict: Token information including access_token, refresh_token, expires_at
        """
        auth_manager = SpotifyService.get_auth_manager()
        token_info = auth_manager.get_access_token(code, as_dict=True)
        return token_info

    @staticmethod
    def refresh_access_token(refresh_token: str) -> Dict[str, Any]:
        """
        Refresh an expired access token

        Args:
            refresh_token: Refresh token

        Returns:
            dict: New token information
        """
        auth_manager = SpotifyService.get_auth_manager()
        token_info = auth_manager.refresh_access_token(refresh_token)
        return token_info

    def get_current_user(self) -> Dict[str, Any]:
        """
        Get current user's profile information

        Returns:
            dict: User profile data
        """
        if not self.client:
            raise ValueError("Spotify client not initialized with access token")

        try:
            user = self.client.current_user()
            return user
        except Exception as e:
            logger.error(f"Error fetching current user: {e}")
            raise

    def get_top_tracks(
        self, time_range: str = "medium_term", limit: int = 50, offset: int = 0
    ) -> Dict[str, Any]:
        """
        Get user's top tracks

        Args:
            time_range: Time range for top tracks (short_term, medium_term, long_term)
            limit: Number of tracks to return (max 50)
            offset: Index of first track to return

        Returns:
            dict: Top tracks data
        """
        if not self.client:
            raise ValueError("Spotify client not initialized with access token")

        try:
            tracks = self.client.current_user_top_tracks(
                time_range=time_range, limit=limit, offset=offset
            )
            return tracks
        except Exception as e:
            logger.error(f"Error fetching top tracks: {e}")
            raise

    def get_top_artists(
        self, time_range: str = "medium_term", limit: int = 50, offset: int = 0
    ) -> Dict[str, Any]:
        """
        Get user's top artists

        Args:
            time_range: Time range for top artists (short_term, medium_term, long_term)
            limit: Number of artists to return (max 50)
            offset: Index of first artist to return

        Returns:
            dict: Top artists data
        """
        if not self.client:
            raise ValueError("Spotify client not initialized with access token")

        try:
            artists = self.client.current_user_top_artists(
                time_range=time_range, limit=limit, offset=offset
            )
            return artists
        except Exception as e:
            logger.error(f"Error fetching top artists: {e}")
            raise

    def get_recently_played(
        self, limit: int = 50, after: Optional[int] = None, before: Optional[int] = None
    ) -> Dict[str, Any]:
        """
        Get user's recently played tracks

        Args:
            limit: Number of tracks to return (max 50)
            after: Unix timestamp in milliseconds (returns tracks played after this time)
            before: Unix timestamp in milliseconds (returns tracks played before this time)

        Returns:
            dict: Recently played tracks data
        """
        if not self.client:
            raise ValueError("Spotify client not initialized with access token")

        try:
            tracks = self.client.current_user_recently_played(
                limit=limit, after=after, before=before
            )
            return tracks
        except Exception as e:
            logger.error(f"Error fetching recently played tracks: {e}")
            raise

    def get_audio_features(self, track_ids: List[str]) -> List[Dict[str, Any]]:
        """
        Get audio features for multiple tracks

        Args:
            track_ids: List of Spotify track IDs

        Returns:
            list: Audio features for each track
        """
        if not self.client:
            raise ValueError("Spotify client not initialized with access token")

        try:
            # API allows max 100 tracks at a time
            features = self.client.audio_features(track_ids[:100])
            return features
        except Exception as e:
            logger.error(f"Error fetching audio features: {e}")
            raise

    def get_saved_tracks(self, limit: int = 50, offset: int = 0) -> Dict[str, Any]:
        """
        Get user's saved tracks (liked songs)

        Args:
            limit: Number of tracks to return (max 50)
            offset: Index of first track to return

        Returns:
            dict: Saved tracks data
        """
        if not self.client:
            raise ValueError("Spotify client not initialized with access token")

        try:
            tracks = self.client.current_user_saved_tracks(limit=limit, offset=offset)
            return tracks
        except Exception as e:
            logger.error(f"Error fetching saved tracks: {e}")
            raise

    def get_user_playlists(self, limit: int = 50, offset: int = 0) -> Dict[str, Any]:
        """
        Get user's playlists

        Args:
            limit: Number of playlists to return (max 50)
            offset: Index of first playlist to return

        Returns:
            dict: User playlists data
        """
        if not self.client:
            raise ValueError("Spotify client not initialized with access token")

        try:
            playlists = self.client.current_user_playlists(limit=limit, offset=offset)
            return playlists
        except Exception as e:
            logger.error(f"Error fetching user playlists: {e}")
            raise

    def get_track(self, track_id: str) -> Dict[str, Any]:
        """
        Get a specific track by ID

        Args:
            track_id: Spotify track ID

        Returns:
            dict: Track data
        """
        if not self.client:
            raise ValueError("Spotify client not initialized with access token")

        try:
            track = self.client.track(track_id)
            return track
        except Exception as e:
            logger.error(f"Error fetching track: {e}")
            raise

    def get_artist(self, artist_id: str) -> Dict[str, Any]:
        """
        Get a specific artist by ID

        Args:
            artist_id: Spotify artist ID

        Returns:
            dict: Artist data
        """
        if not self.client:
            raise ValueError("Spotify client not initialized with access token")

        try:
            artist = self.client.artist(artist_id)
            return artist
        except Exception as e:
            logger.error(f"Error fetching artist: {e}")
            raise
