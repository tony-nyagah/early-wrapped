import Link from "next/link";

export default function Home() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-primary via-secondary to-neutral">
      <div className="hero min-h-screen">
        <div className="hero-content text-center">
          <div className="max-w-2xl">
            <h1 className="text-6xl font-bold mb-4 text-white">
              🎵 Early Wrapped
            </h1>
            <p className="text-2xl mb-8 text-gray-200">
              Your Spotify stats, anytime you want them
            </p>
            <p className="text-lg mb-12 text-gray-300 max-w-xl mx-auto">
              Why wait until December? View your listening statistics, top
              tracks, favorite artists, and music insights whenever you like!
            </p>

            <Link
              href="/auth/login"
              className="btn btn-primary btn-lg text-white gap-2 hover:btn-accent"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                className="h-6 w-6"
                viewBox="0 0 24 24"
                fill="currentColor"
              >
                <path d="M12 0C5.4 0 0 5.4 0 12s5.4 12 12 12 12-5.4 12-12S18.66 0 12 0zm5.521 17.34c-.24.359-.66.48-1.021.24-2.82-1.74-6.36-2.101-10.561-1.141-.418.122-.779-.179-.899-.539-.12-.421.18-.78.54-.9 4.56-1.021 8.52-.6 11.64 1.32.42.18.479.659.301 1.02zm1.44-3.3c-.301.42-.841.6-1.262.3-3.239-1.98-8.159-2.58-11.939-1.38-.479.12-1.02-.12-1.14-.6-.12-.48.12-1.021.6-1.141C9.6 9.9 15 10.561 18.72 12.84c.361.181.54.78.241 1.2zm.12-3.36C15.24 8.4 8.82 8.16 5.16 9.301c-.6.179-1.2-.181-1.38-.721-.18-.601.18-1.2.72-1.381 4.26-1.26 11.28-1.02 15.721 1.621.539.3.719 1.02.419 1.56-.299.421-1.02.599-1.559.3z" />
              </svg>
              Login with Spotify
            </Link>

            <div className="mt-16 grid grid-cols-1 md:grid-cols-3 gap-8 text-left">
              <div className="card bg-base-300 shadow-xl">
                <div className="card-body">
                  <h3 className="card-title text-primary">📊 Top Stats</h3>
                  <p className="text-gray-300">
                    View your most played tracks, artists, and genres
                  </p>
                </div>
              </div>

              <div className="card bg-base-300 shadow-xl">
                <div className="card-body">
                  <h3 className="card-title text-primary">⏰ Anytime Access</h3>
                  <p className="text-gray-300">
                    Check your stats whenever you want, not just year-end
                  </p>
                </div>
              </div>

              <div className="card bg-base-300 shadow-xl">
                <div className="card-body">
                  <h3 className="card-title text-primary">🎨 Beautiful Viz</h3>
                  <p className="text-gray-300">
                    Gorgeous visualizations of your music taste
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
