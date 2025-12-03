import Link from "next/link";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";

export default function Home() {
  return (
    <div className="min-h-screen bg-accent-yellow p-4 md:p-8">
      <div className="container mx-auto max-w-7xl">
        {/* Hero Section */}
        <div className="text-center mb-16 mt-12">
          <div className="inline-block transform -rotate-2 mb-6">
            <h1 className="text-6xl md:text-9xl font-black bg-spotify-green text-white px-8 py-6 border-[6px] border-black shadow-[12px_12px_0px_0px_rgba(0,0,0,1)]">
              🎵 EARLY
            </h1>
          </div>
          <div className="inline-block transform rotate-1">
            <h1 className="text-6xl md:text-9xl font-black bg-accent-pink text-white px-8 py-6 border-[6px] border-black shadow-[12px_12px_0px_0px_rgba(0,0,0,1)]">
              WRAPPED
            </h1>
          </div>

          <p className="text-2xl md:text-4xl font-black mb-6 mt-12 text-black">
            Your Spotify stats,<br />whenever you want them
          </p>

          <Link href="/auth/login" className="inline-block">
            <Button 
              size="lg"
              className="neu-btn bg-spotify-green hover:bg-spotify-green text-white text-xl md:text-2xl px-12 py-8 h-auto"
            >
              Login with Spotify
            </Button>
          </Link>
        </div>

        {/* Features Grid */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 md:gap-8 mb-16">
          <Card className="neu-card bg-spotify-green transform -rotate-1 border-[4px]">
            <CardContent className="p-8 text-center">
              <div className="text-7xl mb-6">📊</div>
              <h3 className="text-2xl md:text-3xl font-black mb-4 text-white">
                TOP STATS
              </h3>
              <p className="text-white font-bold text-lg">
                View your most played tracks, artists, and genres
              </p>
            </CardContent>
          </Card>

          <Card className="neu-card bg-accent-blue transform rotate-1 border-[4px]">
            <CardContent className="p-8 text-center">
              <div className="text-7xl mb-6">⏰</div>
              <h3 className="text-2xl md:text-3xl font-black mb-4 text-black">
                ANYTIME ACCESS
              </h3>
              <p className="text-black font-bold text-lg">
                Check your stats whenever you want, not just year-end
              </p>
            </CardContent>
          </Card>

          <Card className="neu-card bg-accent-purple transform -rotate-1 border-[4px]">
            <CardContent className="p-8 text-center">
              <div className="text-7xl mb-6">🎨</div>
              <h3 className="text-2xl md:text-3xl font-black mb-4 text-white">
                BEAUTIFUL VIZ
              </h3>
              <p className="text-white font-bold text-lg">
                Gorgeous visualizations of your music taste
              </p>
            </CardContent>
          </Card>
        </div>
      </div>
    </div>
  );
}
