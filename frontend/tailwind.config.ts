import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [require("daisyui")],
  daisyui: {
    themes: [
      {
        spotify: {
          primary: "#1DB954",
          secondary: "#191414",
          accent: "#1ed760",
          neutral: "#282828",
          "base-100": "#121212",
          "base-200": "#191414",
          "base-300": "#282828",
          info: "#3abff8",
          success: "#1DB954",
          warning: "#fbbd23",
          error: "#f87272",
        },
      },
      "dark",
      "light",
    ],
  },
};

export default config;
