# 🚀 Getting Started with Early Wrapped

Welcome! This guide will help you get Early Wrapped up and running on your local machine.

## 📋 Prerequisites

Before you begin, make sure you have the following installed:

- **Python 3.9+** - Check with `python3 --version`
- **[uv](https://github.com/astral-sh/uv)** - Fast Python package installer
  ```bash
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```
- **[Bun](https://bun.sh)** - Fast JavaScript runtime
  ```bash
  curl -fsSL https://bun.sh/install | bash
  ```
- **Spotify Account** - Free or Premium
- **Git** - For version control

## 🎵 Step 1: Spotify Developer Setup

1. Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
2. Log in with your Spotify account
3. Click **"Create app"**
4. Fill in the details:
   - **App name**: `Early Wrapped` (or any name you like)
   - **App description**: `Personal Spotify statistics viewer`
   - **Redirect URI**: `http://127.0.0.1:8000/auth/callback`
   - **Which API/SDKs are you planning to use?**: Select "Web API"
5. Agree to the terms and click **"Save"**
6. On your app page, click **"Settings"**
7. Copy your **Client ID** and **Client Secret** (click "View client secret")
8. Keep these safe - you'll need them in the next step!

## ⚙️ Step 2: Project Setup

### Option A: Quick Setup (Recommended)

```bash
# Clone the repository (if you haven't already)
cd early-wrapped

# Run the setup script
make setup
```

This will:

- Create `.env` files from templates
- Install all backend dependencies with uv
- Install all frontend dependencies with bun

### Option B: Manual Setup

```bash
# Backend setup
cd backend
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv pip install -r requirements.txt
cp .env.example .env

# Frontend setup
cd ../frontend
bun install
cp .env.example .env.local
```

## 🔐 Step 3: Configure Environment Variables

### Backend Configuration

Open `backend/.env` and add your Spotify credentials:

```env
# Spotify API Credentials
SPOTIFY_CLIENT_ID=your_client_id_from_step_1
SPOTIFY_CLIENT_SECRET=your_client_secret_from_step_1
SPOTIFY_REDIRECT_URI=http://127.0.0.1:8000/auth/callback

# Application Security (generate a random string for production)
SECRET_KEY=your_secret_key_here_change_in_production

# Database Configuration
DATABASE_URL=sqlite:///./early_wrapped.db

# Application Settings
DEBUG=True
ALLOWED_ORIGINS=http://localhost:3000,http://127.0.0.1:3000

# API Settings
API_V1_PREFIX=/api/v1
```

**Important**: Replace `your_client_id_from_step_1` and `your_client_secret_from_step_1` with the actual values from your Spotify app!

### Frontend Configuration

The `frontend/.env.local` file should already be created. Verify it contains:

```env
NEXT_PUBLIC_API_URL=http://localhost:8000
NEXT_PUBLIC_APP_NAME=Early Wrapped
NEXT_PUBLIC_APP_URL=http://localhost:3000
```

## 🚀 Step 4: Run the Application

### Option A: Run Both Servers Together (with tmux)

```bash
make dev
```

This will start both the backend and frontend in a split tmux session.

- Left pane: Backend (http://localhost:8000)
- Right pane: Frontend (http://localhost:3000)

To exit tmux: Press `Ctrl+B` then `D` (detach)

### Option B: Run Servers Separately

**Terminal 1 - Backend:**

```bash
make backend
# or
cd backend && source .venv/bin/activate && uvicorn app.main:app --reload
```

**Terminal 2 - Frontend:**

```bash
make frontend
# or
cd frontend && bun dev
```

## ✅ Step 5: Verify Everything Works

1. **Check Backend**: Open http://localhost:8000

   - You should see: `{"message": "Welcome to Early Wrapped API", "status": "healthy", "version": "1.0.0"}`

2. **Check API Docs**: Open http://localhost:8000/docs

   - You should see the FastAPI interactive documentation

3. **Check Frontend**: Open http://localhost:3000
   - You should see the Next.js welcome page (we'll build the real UI soon!)

## 🎉 You're Ready!

Everything is set up! Now you can start building the features.

## 📚 Useful Commands

```bash
# View all available commands
make help

# Start development servers
make dev              # Both servers (requires tmux)
make backend          # Backend only
make frontend         # Frontend only

# Maintenance
make clean            # Clean all build artifacts
make test             # Run tests

# Manual commands
cd backend && source .venv/bin/activate  # Activate Python venv
cd frontend && bun dev                    # Run frontend
```

## 🐛 Troubleshooting

### Backend won't start

**Error: "No module named 'app'"**

- Make sure you're in the `backend` directory
- Make sure the virtual environment is activated: `source .venv/bin/activate`

**Error: "Could not load settings"**

- Check that `backend/.env` exists and has valid values
- Verify your Spotify credentials are correct

### Frontend won't start

**Error: "Command not found: bun"**

- Install Bun: `curl -fsSL https://bun.sh/install | bash`
- Restart your terminal after installation

**Error: "Cannot find module"**

- Run `bun install` in the frontend directory

### Port already in use

**Backend (8000) or Frontend (3000) port busy:**

```bash
# Find what's using the port
lsof -i :8000  # or :3000

# Kill the process
kill -9 <PID>
```

### Spotify Authentication Issues

- Verify redirect URI in Spotify Dashboard matches: `http://127.0.0.1:8000/auth/callback`
- Check that Client ID and Secret are correct in `backend/.env`
- Make sure there are no extra spaces in the .env file

## 📖 Next Steps

Now that everything is running, check out:

- [ROADMAP.md](./ROADMAP.md) - See what features we're building
- [README.md](./README.md) - Full project documentation
- Backend API docs: http://localhost:8000/docs

## 💡 Tips

- Keep both servers running while developing
- Backend auto-reloads on Python file changes
- Frontend auto-reloads on React/TypeScript changes
- Check the terminal output for errors
- Use the browser console for frontend debugging

## 🆘 Need Help?

- Check the [ROADMAP.md](./ROADMAP.md) for current development status
- Review error messages carefully - they usually point to the issue
- Make sure all prerequisites are installed correctly

Happy coding! 🎵✨
