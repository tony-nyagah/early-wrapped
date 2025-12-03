import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Early Wrapped - Your Spotify Stats Anytime",
  description:
    "View your Spotify listening statistics anytime, not just at year-end!",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" data-theme="spotify">
      <body className="antialiased">{children}</body>
    </html>
  );
}
