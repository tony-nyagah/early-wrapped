# 🧪 API Testing Guide

This guide shows you how to test the Early Wrapped API endpoints.

## Prerequisites

1. Backend server running: `make backend` or `cd backend && ./dev.sh`
2. Spotify Developer credentials added to `backend/.env`

## Quick Test URLs

**Backend Base URL**: http://localhost:8000

- **API Docs (Interactive)**: http://localhost:8000/docs
- **Alternative Docs**: http://localhost:8000/redoc
- **Health Check**: http://localhost:8000/health

## Testing Authentication Flow

### 1. Check API Status

```bash
curl http://localhost:8000
```

Expected response:

```json
{
  "message": "Welcome to Early Wrapped API",
  "status": "healthy",
  "version": "1.0.0",
  "docs": "/docs",
  "endpoints": {
    "auth": "/auth",
    "user": "/api/user"
  }
}
```

### 2. Check Authentication Status

```bash
curl http://localhost:8000/auth/check
```

Expected response (not authenticated):

```json
{
  "authenticated": false,
  "message": "User is not authenticated"
}
```

### 3. Login with Spotify

**Using Browser (Recommended):**

1. Open: http://localhost:8000/auth/login
2. You'll be redirected to Spotify
3. Login and authorize the app
4. You'll be redirected back to: http://localhost:3000/auth/success

**Using curl:**

```bash
# This will return a redirect URL
curl -I http://localhost:8000/auth/login
```

### 4. Check Authentication After Login

Open browser console and check cookies:

- `spotify_access_token` (httponly)
- `spotify_refresh_token` (httponly)
- `user_profile`

### 5. Get Current User Profile

```bash
curl -b cookies.txt http://localhost:8000/auth/me
```

Or in browser (after login):

```
http://localhost:8000/auth/me
```

## Testing User Data Endpoints

All these endpoints require authentication (must be logged in).

### Get User Profile

```bash
curl -b cookies.txt http://localhost:8000/api/user/profile
```

### Get Top Tracks

**Short term (last 4 weeks):**

```bash
curl "http://localhost:8000/api/user/top-tracks?time_range=short_term&limit=10"
```

**Medium term (last 6 months):**

```bash
curl "http://localhost:8000/api/user/top-tracks?time_range=medium_term&limit=20"
```

**Long term (all time):**

```bash
curl "http://localhost:8000/api/user/top-tracks?time_range=long_term&limit=50"
```

### Get Top Artists

```bash
curl "http://localhost:8000/api/user/top-artists?time_range=medium_term&limit=10"
```

### Get Recently Played Tracks

```bash
curl "http://localhost:8000/api/user/recently-played?limit=20"
```

### Get Saved Tracks (Liked Songs)

```bash
curl "http://localhost:8000/api/user/saved-tracks?limit=20"
```

### Get User Playlists

```bash
curl "http://localhost:8000/api/user/playlists?limit=20"
```

### Get Audio Features

```bash
curl "http://localhost:8000/api/user/audio-features?track_ids=TRACK_ID_1,TRACK_ID_2"
```

### Get Specific Track

```bash
curl "http://localhost:8000/api/user/track/{TRACK_ID}"
```

### Get Specific Artist

```bash
curl "http://localhost:8000/api/user/artist/{ARTIST_ID}"
```

## Using the Interactive API Docs

The easiest way to test the API is using the built-in Swagger UI:

1. Start the backend server
2. Open: http://localhost:8000/docs
3. Click on any endpoint
4. Click "Try it out"
5. Fill in parameters
6. Click "Execute"
7. See the response!

### Testing with Authentication in Swagger

1. First, login via browser: http://localhost:8000/auth/login
2. After successful login, your cookies are set
3. Go to: http://localhost:8000/docs
4. All endpoints will automatically use your auth cookies!
5. Try the `/auth/check` endpoint - should show authenticated: true

## Common Response Formats

### Success Response

```json
{
  "success": true,
  "data": { ... },
  "total": 50,
  "limit": 20,
  "offset": 0
}
```

### Error Response

```json
{
  "detail": "Error message here"
}
```

### Top Tracks Response Example

```json
{
  "success": true,
  "time_range": "medium_term",
  "limit": 5,
  "offset": 0,
  "total": 50,
  "data": [
    {
      "id": "track_id",
      "name": "Song Name",
      "artists": [
        {
          "id": "artist_id",
          "name": "Artist Name"
        }
      ],
      "album": {
        "id": "album_id",
        "name": "Album Name",
        "images": [...]
      },
      "duration_ms": 240000,
      "popularity": 85
    }
  ]
}
```

## Query Parameters

### Time Range Options

- `short_term` - Last 4 weeks
- `medium_term` - Last 6 months (default)
- `long_term` - All time

### Pagination

- `limit` - Number of items to return (1-50, default 20)
- `offset` - Starting position (default 0)

### Examples

```bash
# Get top 10 tracks from last 4 weeks
curl "http://localhost:8000/api/user/top-tracks?time_range=short_term&limit=10"

# Get tracks 20-40 (pagination)
curl "http://localhost:8000/api/user/top-tracks?limit=20&offset=20"

# Get top 5 artists of all time
curl "http://localhost:8000/api/user/top-artists?time_range=long_term&limit=5"
```

## Testing Authentication Refresh

```bash
# Refresh token
curl -X POST http://localhost:8000/auth/refresh
```

## Logout

```bash
curl -X POST http://localhost:8000/auth/logout
```

## Error Codes

- `200` - Success
- `400` - Bad Request (invalid parameters)
- `401` - Unauthorized (not logged in)
- `404` - Not Found
- `500` - Internal Server Error

## Tips

1. **Use the Swagger UI** - It's the easiest way to test: http://localhost:8000/docs
2. **Check the browser console** - Look for cookie values after login
3. **Check backend logs** - The terminal shows all requests and errors
4. **Use browser DevTools** - Network tab shows all API calls

## Testing Workflow

### Complete Test Flow

1. **Start backend**: `make backend`
2. **Check health**: Visit http://localhost:8000/health
3. **Open docs**: Visit http://localhost:8000/docs
4. **Login**: Go to http://localhost:8000/auth/login
5. **Authorize**: Login with Spotify and approve
6. **Check auth**: Try `/auth/check` endpoint in docs
7. **Get profile**: Try `/auth/me` endpoint
8. **Get top tracks**: Try `/api/user/top-tracks` with different time ranges
9. **Get top artists**: Try `/api/user/top-artists`
10. **Explore**: Try all other endpoints!

## Troubleshooting

### "Not authenticated" error

- Make sure you've logged in via `/auth/login`
- Check that cookies are set in your browser
- Try logging out and logging in again

### "Invalid credentials" error

- Check `backend/.env` has correct Spotify credentials
- Verify redirect URI matches: `http://127.0.0.1:8000/auth/callback`
- Check Spotify Dashboard settings

### "Address already in use" error

- Kill the process using port 8000: `lsof -ti:8000 | xargs kill -9`
- Or use a different port: `uvicorn app.main:app --port 8001`

### Empty data responses

- Some endpoints return empty if you're a new Spotify user
- Play some music on Spotify and try again after a few hours
- Try different time ranges (short_term, medium_term, long_term)

## Next Steps

Once you've tested the API endpoints:

1. Build the frontend to display this data beautifully
2. Create analytics to process the data (Phase 2)
3. Add visualizations (Phase 3)
4. Make it shareable (Phase 4)

Happy testing! 🎵✨
