"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import { auth, user } from "@/lib/api";
import Link from "next/link";

interface UserProfile {
  id: string;
  display_name: string;
  email: string;
  country: string;
  images: Array<{ url: string }>;
}

interface Track {
  id: string;
  name: string;
  artists: Array<{ name: string }>;
  album: {
    name: string;
    images: Array<{ url: string }>;
  };
}

interface Artist {
  id: string;
  name: string;
  genres: string[];
  images: Array<{ url: string }>;
}

export default function DashboardPage() {
  const router = useRouter();
  const [loading, setLoading] = useState(true);
  const [profile, setProfile] = useState<UserProfile | null>(null);
  const [topTracks, setTopTracks] = useState<Track[]>([]);
  const [topArtists, setTopArtists] = useState<Artist[]>([]);
  const [timeRange, setTimeRange] = useState<
    "short_term" | "medium_term" | "long_term"
  >("medium_term");

  useEffect(() => {
    loadUserData();
  }, []);

  useEffect(() => {
    if (profile) {
      loadTopData();
    }
  }, [timeRange, profile]);

  async function loadUserData() {
    try {
      // Check auth
      const authStatus = await auth.checkAuth();
      if (!authStatus.authenticated) {
        router.push("/auth/login");
        return;
      }

      // Load profile
      const profileData = await auth.getCurrentUser();
      setProfile(profileData);

      // Load top tracks and artists
      await loadTopData();
    } catch (error) {
      console.error("Error loading user data:", error);
      router.push("/auth/login");
    } finally {
      setLoading(false);
    }
  }

  async function loadTopData() {
    try {
      const [tracksData, artistsData] = await Promise.all([
        user.getTopTracks({ time_range: timeRange, limit: 5 }),
        user.getTopArtists({ time_range: timeRange, limit: 5 }),
      ]);

      setTopTracks(tracksData.items || []);
      setTopArtists(artistsData.items || []);
    } catch (error) {
      console.error("Error loading top data:", error);
    }
  }

  async function handleLogout() {
    try {
      await auth.logout();
      router.push("/");
    } catch (error) {
      console.error("Logout error:", error);
    }
  }

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-base-100">
        <div className="text-center">
          <div className="loading loading-spinner loading-lg text-primary"></div>
          <p className="mt-4 text-lg">Loading your stats...</p>
        </div>
      </div>
    );
  }

  const timeRangeLabels = {
    short_term: "Last 4 Weeks",
    medium_term: "Last 6 Months",
    long_term: "All Time",
  };

  return (
    <div className="min-h-screen bg-base-100">
      {/* Navigation */}
      <div className="navbar bg-base-300 shadow-lg">
        <div className="flex-1">
          <Link href="/" className="btn btn-ghost text-xl">
            🎵 Early Wrapped
          </Link>
        </div>
        <div className="flex-none gap-2">
          <div className="dropdown dropdown-end">
            <label tabIndex={0} className="btn btn-ghost btn-circle avatar">
              <div className="w-10 rounded-full">
                {profile?.images?.[0]?.url ? (
                  <img src={profile.images[0].url} alt={profile.display_name} />
                ) : (
                  <div className="bg-primary flex items-center justify-center h-full">
                    {profile?.display_name?.[0] || "?"}
                  </div>
                )}
              </div>
            </label>
            <ul
              tabIndex={0}
              className="mt-3 z-[1] p-2 shadow menu menu-sm dropdown-content bg-base-300 rounded-box w-52"
            >
              <li className="menu-title">
                <span>{profile?.display_name}</span>
              </li>
              <li>
                <button onClick={handleLogout} className="text-error">
                  Logout
                </button>
              </li>
            </ul>
          </div>
        </div>
      </div>

      <div className="container mx-auto p-8">
        {/* Welcome Section */}
        <div className="mb-8">
          <h1 className="text-4xl font-bold mb-2">
            Welcome back, {profile?.display_name}! 👋
          </h1>
          <p className="text-gray-400">Here's what you've been listening to</p>
        </div>

        {/* Time Range Selector */}
        <div className="tabs tabs-boxed mb-8 bg-base-300 w-fit">
          {(
            Object.keys(timeRangeLabels) as Array<keyof typeof timeRangeLabels>
          ).map((range) => (
            <button
              key={range}
              className={`tab ${timeRange === range ? "tab-active" : ""}`}
              onClick={() => setTimeRange(range)}
            >
              {timeRangeLabels[range]}
            </button>
          ))}
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
          {/* Top Tracks */}
          <div className="card bg-base-300 shadow-xl">
            <div className="card-body">
              <h2 className="card-title text-2xl mb-4">🎵 Your Top Tracks</h2>
              <div className="space-y-4">
                {topTracks.map((track, index) => (
                  <div
                    key={track.id}
                    className="flex items-center gap-4 p-3 bg-base-100 rounded-lg hover:bg-base-200 transition"
                  >
                    <span className="text-2xl font-bold text-primary w-8">
                      {index + 1}
                    </span>
                    {track.album.images[0] && (
                      <img
                        src={track.album.images[0].url}
                        alt={track.name}
                        className="w-16 h-16 rounded"
                      />
                    )}
                    <div className="flex-1 min-w-0">
                      <p className="font-semibold truncate">{track.name}</p>
                      <p className="text-sm text-gray-400 truncate">
                        {track.artists.map((a) => a.name).join(", ")}
                      </p>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </div>

          {/* Top Artists */}
          <div className="card bg-base-300 shadow-xl">
            <div className="card-body">
              <h2 className="card-title text-2xl mb-4">🎤 Your Top Artists</h2>
              <div className="space-y-4">
                {topArtists.map((artist, index) => (
                  <div
                    key={artist.id}
                    className="flex items-center gap-4 p-3 bg-base-100 rounded-lg hover:bg-base-200 transition"
                  >
                    <span className="text-2xl font-bold text-primary w-8">
                      {index + 1}
                    </span>
                    {artist.images[0] && (
                      <img
                        src={artist.images[0].url}
                        alt={artist.name}
                        className="w-16 h-16 rounded-full"
                      />
                    )}
                    <div className="flex-1 min-w-0">
                      <p className="font-semibold truncate">{artist.name}</p>
                      <p className="text-sm text-gray-400 truncate">
                        {artist.genres.slice(0, 3).join(", ")}
                      </p>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
