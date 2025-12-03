"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import api from "@/lib/api";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";

interface Track {
  id: string;
  name: string;
  artists: { name: string }[];
  album: {
    images: { url: string }[];
  };
  external_urls: {
    spotify: string;
  };
}

interface Artist {
  id: string;
  name: string;
  images: { url: string }[];
  external_urls: {
    spotify: string;
  };
  genres: string[];
}

export default function Dashboard() {
  const router = useRouter();
  const [timeRange, setTimeRange] = useState<
    "short_term" | "medium_term" | "long_term"
  >("medium_term");
  const [topTracks, setTopTracks] = useState<Track[]>([]);
  const [topArtists, setTopArtists] = useState<Artist[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    checkAuthAndLoadData();
  }, []);

  useEffect(() => {
    if (!loading) {
      loadTopData();
    }
  }, [timeRange]);

  const checkAuthAndLoadData = async () => {
    try {
      console.log("Checking authentication...");
      const authResponse = await api.auth.checkAuth();
      console.log("Auth response:", authResponse);

      if (!authResponse.authenticated) {
        console.log("Not authenticated, redirecting to login");
        router.push("/auth/login");
        return;
      }

      console.log("Authenticated, loading top data");
      await loadTopData();
    } catch (err) {
      console.error("Auth check error:", err);
      setError("Failed to authenticate");
      router.push("/auth/login");
    }
  };

  const loadTopData = async () => {
    try {
      setLoading(true);
      setError(null);

      console.log(`Loading top tracks for time range: ${timeRange}`);
      const tracksResponse = await api.user.getTopTracks({
        limit: 10,
        time_range: timeRange,
      });
      console.log("Tracks response:", tracksResponse);
      // Backend returns {success: true, data: [...]}
      setTopTracks(tracksResponse?.data || tracksResponse?.items || []);

      console.log(`Loading top artists for time range: ${timeRange}`);
      const artistsResponse = await api.user.getTopArtists({
        limit: 10,
        time_range: timeRange,
      });
      console.log("Artists response:", artistsResponse);
      // Backend returns {success: true, data: [...]}
      setTopArtists(artistsResponse?.data || artistsResponse?.items || []);

      setLoading(false);
    } catch (err) {
      console.error("Error loading data:", err);
      setError("Failed to load data");
      setLoading(false);
    }
  };

  const timeRangeLabels = {
    short_term: "LAST 4 WEEKS",
    medium_term: "LAST 6 MONTHS",
    long_term: "ALL TIME",
  };

  if (loading) {
    return (
      <div className="min-h-screen bg-accent-yellow flex items-center justify-center p-4">
        <Card className="neu-card bg-white border-[6px]">
          <CardContent className="p-12 text-center">
            <div className="text-6xl mb-4">⏳</div>
            <p className="text-2xl font-black">LOADING YOUR STATS...</p>
          </CardContent>
        </Card>
      </div>
    );
  }

  if (error) {
    return (
      <div className="min-h-screen bg-accent-pink flex items-center justify-center p-4">
        <Card className="neu-card bg-white border-[6px] max-w-md">
          <CardContent className="p-8 text-center">
            <div className="text-6xl mb-4">⚠️</div>
            <p className="text-2xl font-black text-red-600">{error}</p>
          </CardContent>
        </Card>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-accent-yellow p-4 md:p-8">
      <div className="container mx-auto max-w-7xl">
        <div className="mb-8">
          <div className="inline-block transform -rotate-1 mb-6">
            <h1 className="text-4xl md:text-6xl font-black bg-spotify-green text-white px-8 py-4 border-[6px] border-black shadow-[8px_8px_0px_0px_rgba(0,0,0,1)]">
              🎵 YOUR MUSIC STATS
            </h1>
          </div>

          {/* Time Range Selector */}
          <div className="flex flex-wrap gap-4 mb-6">
            {(["short_term", "medium_term", "long_term"] as const).map(
              (range) => (
                <Button
                  key={range}
                  onClick={() => setTimeRange(range)}
                  variant={timeRange === range ? "default" : "outline"}
                  className={`neu-btn font-black text-lg ${
                    timeRange === range
                      ? "bg-spotify-green hover:bg-spotify-green text-white"
                      : "bg-white hover:bg-white text-black"
                  }`}
                >
                  {timeRangeLabels[range]}
                </Button>
              )
            )}
          </div>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 md:gap-8">
          {/* Top Tracks */}
          <Card className="neu-card bg-white border-4 transform -rotate-1">
            <CardHeader>
              <CardTitle className="text-3xl md:text-4xl font-black">
                TOP TRACKS 📀
              </CardTitle>
            </CardHeader>
            <CardContent>
              <div className="space-y-3">
                {topTracks && topTracks.length > 0 ? (
                  topTracks.map((track, index) => (
                    <a
                      key={track.id}
                      href={track.external_urls.spotify}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="flex items-center gap-4 p-4 bg-accent-blue border-[3px] border-black shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] hover:translate-x-1 hover:translate-y-1 hover:shadow-[2px_2px_0px_0px_rgba(0,0,0,1)] transition-all"
                    >
                      <div className="text-2xl font-black w-8 shrink-0">
                        {index + 1}
                      </div>
                      <img
                        src={track.album.images[0]?.url}
                        alt={track.name}
                        className="w-16 h-16 border-[3px] border-black shrink-0"
                      />
                      <div className="flex-1 min-w-0">
                        <div className="font-black truncate text-lg">
                          {track.name}
                        </div>
                        <div className="font-bold text-sm truncate opacity-80">
                          {track.artists.map((a) => a.name).join(", ")}
                        </div>
                      </div>
                    </a>
                  ))
                ) : (
                  <p className="text-center py-8 text-lg font-bold">
                    No tracks found
                  </p>
                )}
              </div>
            </CardContent>
          </Card>

          {/* Top Artists */}
          <Card className="neu-card bg-white border-4 transform rotate-1">
            <CardHeader>
              <CardTitle className="text-3xl md:text-4xl font-black">
                TOP ARTISTS 🎤
              </CardTitle>
            </CardHeader>
            <CardContent>
              <div className="space-y-3">
                {topArtists && topArtists.length > 0 ? (
                  topArtists.map((artist, index) => (
                    <a
                      key={artist.id}
                      href={artist.external_urls.spotify}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="flex items-center gap-4 p-4 bg-accent-purple border-[3px] border-black shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] hover:translate-x-1 hover:translate-y-1 hover:shadow-[2px_2px_0px_0px_rgba(0,0,0,1)] transition-all"
                    >
                      <div className="text-2xl font-black text-white w-8 shrink-0">
                        {index + 1}
                      </div>
                      <img
                        src={artist.images[0]?.url}
                        alt={artist.name}
                        className="w-16 h-16 border-[3px] border-black shrink-0"
                      />
                      <div className="flex-1 min-w-0">
                        <div className="font-black text-white truncate text-lg">
                          {artist.name}
                        </div>
                        <div className="font-bold text-sm text-white truncate opacity-80">
                          {artist.genres.slice(0, 3).join(", ")}
                        </div>
                      </div>
                    </a>
                  ))
                ) : (
                  <p className="text-center py-8 text-lg font-bold text-white">
                    No artists found
                  </p>
                )}
              </div>
            </CardContent>
          </Card>
        </div>
      </div>
    </div>
  );
}
