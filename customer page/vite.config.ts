import { defineConfig } from "vite";
import { tanstackStart } from "@tanstack/react-start/plugin/vite";
import tsConfigPaths from "vite-tsconfig-paths";
import tailwindcss from "@tailwindcss/vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [
    tanstackStart({ server: { entry: "server" } }),
    react(),
    tailwindcss(),
    tsConfigPaths(),
  ],
  server: {
    hmr: {
      host: "careers.khalti.com",
      protocol: "wss",
      clientPort: 443,
    },
    allowedHosts: ["careers.khalti.com", "recruiters.khalti.com"],
    watch: {
      ignored: ["**/*"],
    },
    proxy: {
      "/api": {
        target: process.env.API_INTERNAL_URL,
        changeOrigin: true,
      },
      "/static": {
        target: process.env.API_INTERNAL_URL,
        changeOrigin: true,
      },
    },
  },
});
