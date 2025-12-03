"use client";

import Link from "next/link";
import { useSearchParams } from "next/navigation";

export default function AuthErrorPage() {
  const searchParams = useSearchParams();
  const error = searchParams.get("error") || "Unknown error occurred";

  return (
    <div className="min-h-screen flex items-center justify-center bg-base-100">
      <div className="card w-96 bg-base-300 shadow-xl">
        <div className="card-body text-center">
          <h2 className="card-title text-error justify-center">
            Authentication Failed
          </h2>
          <p className="text-gray-300">{error}</p>
          <div className="card-actions justify-center mt-4">
            <Link href="/" className="btn btn-primary">
              Back to Home
            </Link>
            <Link href="/auth/login" className="btn btn-outline btn-primary">
              Try Again
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
}
