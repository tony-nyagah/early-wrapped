# 🎵 Early Wrapped

Your Spotify listening statistics, anytime you want them. No need to wait until December!

## 🎯 What is this?

Early Wrapped is a web application that analyzes your Spotify listening history and creates beautiful, shareable visualizations similar to Spotify Wrapped - but available whenever you want to see your stats.

## ✨ Features

- 🎧 Comprehensive listening statistics
- 🎨 Beautiful, animated visualizations
- 📊 Top tracks, artists, and genres
- ⏰ Listening patterns and insights
- 🎭 Music personality analysis
- 📱 Responsive design for all devices
- 🔗 Shareable results

## 🛠️ Tech Stack

**Backend:**
- Python 3.9+
- FastAPI
- Spotify Web API
- SQLite/PostgreSQL
- pandas for data analysis

**Frontend:**
- Next.js 14
- React 18
- TypeScript
- Tailwind CSS
- Recharts/Chart.js

## 📋 Prerequisites

- Python 3.9 or higher
- [uv](https://github.com/astral-sh/uv) - Fast Python package installer
- [Bun](https://bun.sh) - Fast JavaScript runtime and package manager
- Spotify account (Free or Premium)
- Spotify Developer App credentials

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone <repository-url>
cd early-wrapped
```

### 2. Spotify Developer Setup

1. Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
2. Create a new app
3. Note your **Client ID** and **Client Secret**
4. Add `http://localhost:8000/auth/callback` to Redirect URIs

### 3. Backend Setup

```bash
cd backend
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv pip install -r requirements.txt
```

Create a `.env` file in the `backend` directory:

```env
SPOTIFY_CLIENT_ID=your_client_id_here
SPOTIFY_CLIENT_SECRET=your_client_secret_here
SPOTIFY_REDIRECT_URI=http://localhost:8000/auth/callback
SECRET_KEY=your_secret_key_here
```

Run the backend:

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

### 4. Frontend Setup

```bash
cd frontend
bun install
```

Create a `.env.local` file in the `frontend` directory:

```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

Run the frontend:

```bash
bun dev
```

The app will be available at `http://localhost:3000`

## 📁 Project Structure

```
early-wrapped/
├── backend/
│   ├── app/
│   │   ├── main.py          # FastAPI app entry point
│   │   ├── auth/            # Authentication logic
│   │   ├── api/             # API endpoints
│   │   ├── services/        # Business logic
│   │   ├── models/          # Data models
│   │   └── utils/           # Utility functions
│   ├── requirements.txt
│   └── .env
├── frontend/
│   ├── src/
│   │   ├── app/             # Next.js app directory
│   │   ├── components/      # React components
│   │   ├── lib/             # Utilities and API clients
│   │   └── styles/          # Global styles
│   ├── package.json
│   └── .env.local
├── ROADMAP.md
└── README.md
```

## 🎮 Usage

1. Open the app in your browser
2. Click "Login with Spotify"
3. Authorize the application
4. View your personalized music statistics!
5. Share your results with friends

## 🔐 Privacy & Security

- We only request necessary Spotify permissions
- Your data is stored securely and never shared
- You can revoke access anytime from your Spotify account settings
- All authentication uses OAuth 2.0

## 📊 API Endpoints

### Authentication
- `GET /auth/login` - Initiate Spotify OAuth flow
- `GET /auth/callback` - OAuth callback handler
- `POST /auth/refresh` - Refresh access token
- `POST /auth/logout` - Logout user

### User Data
- `GET /api/user/profile` - Get user profile
- `GET /api/user/top-tracks` - Get top tracks
- `GET /api/user/top-artists` - Get top artists
- `GET /api/user/recently-played` - Get recently played tracks

### Analytics
- `GET /api/analytics/summary` - Get complete analytics summary
- `GET /api/analytics/genres` - Get genre breakdown
- `GET /api/analytics/insights` - Get personalized insights

## 🤝 Contributing

This is a personal project for learning, but suggestions and feedback are welcome!

## 📝 License

MIT License - feel free to use this for your own learning!

## 🙏 Acknowledgments

- Spotify for their amazing API
- Inspired by the original Spotify Wrapped

## 🐛 Known Issues

- Historical data is limited by Spotify API
- Rate limiting may affect large data requests
- Some features require Spotify Premium

## 📫 Contact

Built with ❤️ by [Your Name]

---

**Current Status**: 🚧 In Development

See [ROADMAP.md](./ROADMAP.md) for development progress and planned features.