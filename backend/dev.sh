#!/bin/bash

# Early Wrapped Backend Development Server
# This script sets up and runs the FastAPI development server

set -e

echo "🎵 Starting Early Wrapped Backend..."

# Check if .env file exists
if [ ! -f .env ]; then
    echo "⚠️  No .env file found. Creating from .env.example..."
    if [ -f .env.example ]; then
        cp .env.example .env
        echo "✅ Created .env file. Please update it with your Spotify credentials!"
        echo "   Get them from: https://developer.spotify.com/dashboard"
        exit 1
    else
        echo "❌ .env.example not found!"
        exit 1
    fi
fi

# Check if virtual environment exists
if [ ! -d ".venv" ]; then
    echo "📦 Creating virtual environment with uv..."
    uv venv
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source .venv/bin/activate

# Install/update dependencies
echo "📥 Installing dependencies..."
uv pip install -r requirements.txt

# Run the development server
echo "🚀 Starting FastAPI server on http://localhost:8000"
echo "📚 API docs available at http://localhost:8000/docs"
echo ""
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
