.PHONY: help install setup backend frontend dev clean test

help:
	@echo "🎵 Early Wrapped - Development Commands"
	@echo ""
	@echo "Setup:"
	@echo "  make install    - Install all dependencies (backend + frontend)"
	@echo "  make setup      - Initial project setup"
	@echo ""
	@echo "Development:"
	@echo "  make backend    - Run backend server"
	@echo "  make frontend   - Run frontend dev server"
	@echo "  make dev        - Run both backend and frontend (requires tmux)"
	@echo ""
	@echo "Maintenance:"
	@echo "  make clean      - Clean all build artifacts and caches"
	@echo "  make test       - Run tests"
	@echo ""

install: install-backend install-frontend
	@echo "✅ All dependencies installed!"

install-backend:
	@echo "📦 Installing backend dependencies with uv..."
	cd backend && uv venv && uv pip install -r requirements.txt

install-frontend:
	@echo "📦 Installing frontend dependencies with bun..."
	cd frontend && bun install

setup:
	@echo "🚀 Setting up Early Wrapped..."
	@echo ""
	@echo "Creating environment files..."
	@if [ ! -f backend/.env ]; then \
		cp backend/.env.example backend/.env; \
		echo "✅ Created backend/.env - Please add your Spotify credentials"; \
	else \
		echo "⚠️  backend/.env already exists"; \
	fi
	@if [ ! -f frontend/.env.local ]; then \
		cp frontend/.env.example frontend/.env.local; \
		echo "✅ Created frontend/.env.local"; \
	else \
		echo "⚠️  frontend/.env.local already exists"; \
	fi
	@echo ""
	@echo "Installing dependencies..."
	@make install
	@echo ""
	@echo "✅ Setup complete!"
	@echo ""
	@echo "Next steps:"
	@echo "  1. Add your Spotify credentials to backend/.env"
	@echo "  2. Run 'make dev' to start development servers"

backend:
	@echo "🚀 Starting backend server..."
	cd backend && source .venv/bin/activate && uvicorn app.main:app --reload

frontend:
	@echo "🚀 Starting frontend server..."
	cd frontend && bun dev

dev:
	@echo "🚀 Starting both servers with tmux..."
	@command -v tmux >/dev/null 2>&1 || { echo "❌ tmux is required. Install it first: sudo apt install tmux"; exit 1; }
	tmux new-session -d -s early-wrapped
	tmux send-keys -t early-wrapped "cd backend && source .venv/bin/activate && uvicorn app.main:app --reload" C-m
	tmux split-window -h -t early-wrapped
	tmux send-keys -t early-wrapped "cd frontend && bun dev" C-m
	tmux attach -t early-wrapped

clean:
	@echo "🧹 Cleaning build artifacts..."
	rm -rf backend/.venv
	rm -rf backend/__pycache__
	rm -rf backend/app/__pycache__
	rm -rf backend/*.db
	rm -rf backend/.pytest_cache
	rm -rf frontend/node_modules
	rm -rf frontend/.next
	rm -rf frontend/out
	rm -rf frontend/.turbo
	@echo "✅ Clean complete!"

test:
	@echo "🧪 Running tests..."
	cd backend && source .venv/bin/activate && pytest
	@echo "✅ Tests complete!"
