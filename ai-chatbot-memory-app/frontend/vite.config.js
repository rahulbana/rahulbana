// ---------------------------------------------------------------------------
// Name:     Rahul Singh Bana
// Email:    bana.saa@gmail.com
// LinkedIn: https://www.linkedin.com/in/rahulsinghbana
// Repo:     https://github.com/rahulbana/rahulbana
// ---------------------------------------------------------------------------
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

// The dev server proxies /api requests to the FastAPI backend on :8000.
export default defineConfig({
  plugins: [react()],
  server: {
    port: 5173,
    proxy: {
      "/api": {
        target: "http://localhost:8000",
        changeOrigin: true,
      },
    },
  },
});
