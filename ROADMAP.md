# Early Wrapped - Project Roadmap

A Spotify Wrapped clone that lets you view your listening statistics anytime!

## 🎯 Project Goals

- Fetch and analyze Spotify listening history
- Create beautiful, shareable visualizations
- Make it available anytime (not just end of year)
- Learn and have fun building it!

## 🛠️ Tech Stack

- **Backend**: Python (FastAPI)
- **Frontend**: React/Next.js
- **Data Processing**: pandas/numpy
- **Visualization**: Chart.js or Recharts
- **Database**: SQLite (for now)
- **API**: Spotify Web API

## 📋 Implementation Phases

### Phase 1: Foundation (MVP) 🏗️

#### 1.1 Project Setup ✅
- [x] Initialize project structure
- [x] Set up Python virtual environment (using `uv`)
- [x] Initialize Next.js project (using `bun`)
- [x] Create `.gitignore` and environment files
- [x] Set up basic README
- [x] Create `pyproject.toml` for modern Python config
- [x] Create `Makefile` for easy development commands
- [x] Set up dev scripts

#### 1.2 Spotify Developer Setup
- [ ] Create Spotify Developer account (USER ACTION REQUIRED)
- [ ] Register application on Spotify Dashboard (USER ACTION REQUIRED)
- [ ] Get Client ID and Client Secret (USER ACTION REQUIRED)
- [ ] Configure redirect URIs (USER ACTION REQUIRED)
- [x] Document API credentials setup

#### 1.3 Backend - FastAPI Setup ✅
- [x] Create FastAPI application structure
- [x] Set up CORS for frontend communication
- [x] Create basic health check endpoint
- [x] Set up environment variable management
- [x] Install required packages (fastapi, uvicorn, spotipy, etc.)
- [x] Create directory structure (auth, api, services, schemas, models, utils)
- [x] Set up module imports and __init__ files

#### 1.4 Backend - Spotify Authentication ✅
- [x] Implement OAuth 2.0 authorization flow
- [x] Create `/auth/login` endpoint
- [x] Create `/auth/callback` endpoint
- [x] Implement token refresh logic
- [x] Store tokens securely (httponly cookies)
- [x] Create `/auth/logout` endpoint
- [x] Create `/auth/me` endpoint for user profile
- [x] Create `/auth/check` endpoint for auth status
- [x] Implement CSRF protection with state parameter

#### 1.5 Backend - Data Fetching ✅
- [x] Create endpoint to fetch user profile
- [x] Create endpoint to fetch top tracks
- [x] Create endpoint to fetch top artists
- [x] Create endpoint to fetch recently played tracks
- [x] Implement error handling and rate limiting
- [x] Create SpotifyService class for API interactions
- [x] Create endpoints for saved tracks and playlists
- [x] Create endpoint for audio features
- [x] Create endpoints for individual track/artist lookup

#### 1.6 Frontend - Next.js Setup
- [ ] Create Next.js app with TypeScript
- [ ] Set up Tailwind CSS or styling solution
- [ ] Create basic routing structure
- [ ] Set up API client/fetch utilities
- [ ] Create layout components

#### 1.7 Frontend - Authentication Flow
- [ ] Create landing page with "Login with Spotify" button
- [ ] Implement OAuth redirect handling
- [ ] Store authentication state
- [ ] Create protected routes
- [ ] Add logout functionality

#### 1.8 Frontend - Basic Dashboard
- [ ] Create dashboard layout
- [ ] Fetch and display user profile
- [ ] Display basic loading states
- [ ] Add error handling UI
- [ ] Test end-to-end authentication flow

**Milestone**: User can log in and see their basic Spotify data

---

### Phase 2: Data Analysis 📊

#### 2.1 Data Collection
- [ ] Implement data caching in backend
- [ ] Create database schema for listening history
- [ ] Store user's listening data
- [ ] Implement periodic data refresh
- [ ] Add data validation

#### 2.2 Analytics Engine - Top Stats
- [ ] Calculate top 10 tracks (short term - 4 weeks)
- [ ] Calculate top 10 tracks (medium term - 6 months)
- [ ] Calculate top 10 tracks (long term - all time)
- [ ] Calculate top 10 artists (all time ranges)
- [ ] Calculate top 5 genres

#### 2.3 Analytics Engine - Listening Patterns
- [ ] Calculate total listening time
- [ ] Analyze listening by time of day
- [ ] Analyze listening by day of week
- [ ] Find most active listening month
- [ ] Calculate average session length

#### 2.4 Analytics Engine - Audio Features
- [ ] Fetch audio features for top tracks
- [ ] Calculate average danceability
- [ ] Calculate average energy level
- [ ] Calculate average valence (mood)
- [ ] Determine overall music personality

#### 2.5 Analytics Engine - Insights
- [ ] Find "obscure artist" score
- [ ] Calculate artist diversity
- [ ] Find most played track/artist
- [ ] Calculate skip rate (if available)
- [ ] Generate personalized insights

#### 2.6 Backend - Analytics Endpoints
- [ ] Create `/analytics/summary` endpoint
- [ ] Create `/analytics/top-tracks` endpoint
- [ ] Create `/analytics/top-artists` endpoint
- [ ] Create `/analytics/genres` endpoint
- [ ] Create `/analytics/insights` endpoint

**Milestone**: Backend generates comprehensive listening statistics

---

### Phase 3: Visualization 🎨

#### 3.1 Frontend - Component Library
- [ ] Create StatCard component
- [ ] Create TopList component
- [ ] Create Chart components
- [ ] Create SlideShow component
- [ ] Add animations and transitions

#### 3.2 Frontend - Main Stats Pages
- [ ] Display top tracks with album art
- [ ] Display top artists with images
- [ ] Display genre breakdown (pie/bar chart)
- [ ] Display listening time statistics
- [ ] Display audio features radar chart

#### 3.3 Frontend - Wrapped-Style Experience
- [ ] Create slide-by-slide reveal (like Stories)
- [ ] Add slide transitions and animations
- [ ] Implement keyboard/swipe navigation
- [ ] Add progress indicator
- [ ] Create "Share" screen at the end

#### 3.4 Visual Polish
- [ ] Design color scheme (adapt from album art?)
- [ ] Add loading skeletons
- [ ] Implement smooth animations
- [ ] Make it responsive (mobile-first)
- [ ] Add dark mode support

#### 3.5 Data Visualization
- [ ] Genre distribution chart
- [ ] Listening time over day/week chart
- [ ] Audio features comparison chart
- [ ] Artist/track popularity timeline
- [ ] Mood distribution visualization

**Milestone**: Beautiful, interactive visualization of user's music taste

---

### Phase 4: Sharing & Polish ✨

#### 4.1 Image Generation
- [ ] Set up server-side image generation
- [ ] Design shareable image templates
- [ ] Generate images for each stat card
- [ ] Create combined summary image
- [ ] Add watermark/branding

#### 4.2 Sharing Features
- [ ] Add "Share to Twitter" functionality
- [ ] Add "Share to Instagram" functionality
- [ ] Add "Download as Images" option
- [ ] Add "Copy link" functionality
- [ ] Generate unique shareable URLs

#### 4.3 Time Period Selection
- [ ] Add date range picker
- [ ] Implement "Last Month" view
- [ ] Implement "Last 6 Months" view
- [ ] Implement "This Year" view
- [ ] Implement custom date range

#### 4.4 Additional Features
- [ ] Add comparison between time periods
- [ ] Show "new discoveries" (artists found recently)
- [ ] Display listening streaks
- [ ] Show evolution of music taste over time
- [ ] Add achievement badges/fun stats

#### 4.5 Performance & Optimization
- [ ] Optimize API calls (caching, batching)
- [ ] Implement request rate limiting
- [ ] Add service worker for offline support
- [ ] Optimize images and assets
- [ ] Add analytics tracking (optional)

#### 4.6 Testing & Documentation
- [ ] Write API documentation
- [ ] Add error boundaries
- [ ] Test authentication edge cases
- [ ] Test on different devices/browsers
- [ ] Write user guide/FAQ

**Milestone**: Production-ready app with sharing capabilities

---

### Phase 5: Deployment 🚀

#### 5.1 Backend Deployment
- [ ] Choose hosting platform (Railway/Render/Fly.io)
- [ ] Set up production environment variables
- [ ] Configure production database
- [ ] Set up SSL/HTTPS
- [ ] Deploy backend API

#### 5.2 Frontend Deployment
- [ ] Deploy to Vercel/Netlify
- [ ] Configure environment variables
- [ ] Set up custom domain (optional)
- [ ] Configure API endpoints
- [ ] Test production build

#### 5.3 Post-Deployment
- [ ] Monitor error logs
- [ ] Set up uptime monitoring
- [ ] Gather user feedback
- [ ] Fix bugs and issues
- [ ] Plan future features

**Milestone**: Live, publicly accessible application! 🎉

---

## 🎁 Future Ideas (Optional)

- [ ] Friend comparisons (matching music taste)
- [ ] Playlist generation based on insights
- [ ] Email digest with monthly stats
- [ ] Podcast listening stats
- [ ] Local file music analysis
- [ ] Apple Music / YouTube Music integration
- [ ] Collaborative wrapped with friends
- [ ] Historical data visualization (year over year)
- [ ] Music recommendation engine
- [ ] Concert recommendations based on top artists

---

## 📝 Notes

- Spotify API has rate limits - be mindful of requests
- Free Spotify accounts have limited API access
- Historical data is limited - might need to collect over time
- Some endpoints require specific scopes in OAuth

## 🛠️ Modern Tooling

We're using modern, fast tools for development:
- **uv**: Ultra-fast Python package installer and resolver (replacing pip)
- **Bun**: Fast JavaScript runtime and package manager (replacing npm/yarn)
- **FastAPI**: Modern, fast Python web framework
- **Next.js 14**: Latest React framework with App Router

### Quick Commands
```bash
make setup      # Initial setup (creates .env files and installs deps)
make backend    # Run backend server
make frontend   # Run frontend server
make dev        # Run both with tmux
```

---

## 🐛 Known Issues / Blockers

_Track any issues or blockers here as they come up_

---

**Last Updated**: December 2, 2024
**Current Phase**: Phase 1 - Foundation (In Progress)
**Status**: 🟢 Active Development
**Phases 1.1, 1.3, 1.4, 1.5 Complete!** ✅

## ✅ Recently Completed

### Phase 1.1 - Project Setup ✅ COMPLETE!
- ✅ Created backend and frontend directories
- ✅ Set up FastAPI with basic structure and config
- ✅ Initialized Next.js 14 with TypeScript and Tailwind CSS
- ✅ Created comprehensive .gitignore
- ✅ Set up environment file templates (.env.example)
- ✅ Created project README and documentation
- ✅ Switched to modern tooling (uv for Python, bun for JS)
- ✅ Updated all dependencies to latest compatible versions (Python 3.13 compatible)
- ✅ Created Makefile and dev scripts for easy development
- ✅ Successfully installed and tested all dependencies
- ✅ Created GETTING_STARTED.md with detailed setup instructions
- ✅ Created STATUS.md to track project progress
- ✅ Backend server tested and running successfully
- ✅ Frontend initialized with Next.js App Router

### Phase 1.3 - Backend FastAPI Setup ✅ COMPLETE!
- ✅ Created complete directory structure (auth, api, services, schemas, models, utils)
- ✅ Set up all module __init__ files for proper imports
- ✅ Updated main.py with router configuration
- ✅ Tested backend imports and server startup

### Phase 1.4 - Backend Spotify Authentication ✅ COMPLETE!
- ✅ Implemented full OAuth 2.0 authorization flow
- ✅ Created SpotifyService class with all auth methods
- ✅ Created authentication router with 5 endpoints:
  - `/auth/login` - Initiate OAuth flow
  - `/auth/callback` - Handle OAuth callback
  - `/auth/refresh` - Refresh access token
  - `/auth/logout` - Clear authentication
  - `/auth/me` - Get current user
  - `/auth/check` - Check auth status
- ✅ Implemented secure token storage with httponly cookies
- ✅ Added CSRF protection with state parameter
- ✅ Created Pydantic schemas for validation

### Phase 1.5 - Backend Data Fetching ✅ COMPLETE!
- ✅ Created comprehensive SpotifyService with 10+ methods
- ✅ Created user API router with 9 endpoints:
  - `/api/user/profile` - User profile
  - `/api/user/top-tracks` - Top tracks (with time ranges)
  - `/api/user/top-artists` - Top artists (with time ranges)
  - `/api/user/recently-played` - Recently played tracks
  - `/api/user/saved-tracks` - Liked songs
  - `/api/user/playlists` - User playlists
  - `/api/user/audio-features` - Audio features for tracks
  - `/api/user/track/{id}` - Individual track lookup
  - `/api/user/artist/{id}` - Individual artist lookup
- ✅ Implemented proper error handling and validation
- ✅ Added query parameters for pagination and filtering

**Backend Complete**: 15+ API endpoints, full authentication, data fetching ready!
**Files Created**: 50+ files including complete backend structure
**Lines of Code**: ~1500+ lines of Python backend code

## 🎯 Next Steps
1. **Phase 1.2** - Spotify Developer Setup (USER ACTION REQUIRED - add credentials to .env)
2. **Phase 1.6** - Frontend Next.js Setup (landing page, auth UI)
3. **Phase 1.7** - Frontend Auth Flow (connect to backend)
4. **Phase 1.8** - Basic Dashboard (display user data)