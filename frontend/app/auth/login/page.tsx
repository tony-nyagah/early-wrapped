"use client";

import { useEffect } from "react";

export default function LoginPage() {
  useEffect(() => {
    // Redirect to backend login endpoint
    // Use 127.0.0.1 to match backend domain for cookies
    window.location.href = "http://127.0.0.1:8000/auth/login";
  }, []);

  return (
    <div className="min-h-screen flex items-center justify-center bg-base-100">
      <div className="text-center">
        <div className="loading loading-spinner loading-lg text-primary"></div>
        <p className="mt-4 text-lg">Redirecting to Spotify...</p>
      </div>
    </div>
  );
}
