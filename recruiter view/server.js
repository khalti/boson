import serverHandler from "./dist/server/server.js";
import { join } from "path";
import { statSync } from "fs";

const API_INTERNAL_URL = process.env.API_INTERNAL_URL || "http://khalti-careers-api:8000";

Bun.serve({
  port: process.env.PORT || 3001,
  hostname: process.env.HOST || "0.0.0.0",
  async fetch(req) {
    const url = new URL(req.url);

    if (url.pathname.startsWith("/api") || url.pathname.startsWith("/static")) {
      const target = new URL(url.pathname + url.search, API_INTERNAL_URL);
      return fetch(target.toString(), {
        method: req.method,
        headers: req.headers,
        body: req.method !== "GET" && req.method !== "HEAD" ? req.body : undefined,
      });
    }

    const filePath = join(process.cwd(), "dist/client", decodeURIComponent(url.pathname));
    try {
      if (statSync(filePath).isFile()) {
        return new Response(Bun.file(filePath));
      }
    } catch (e) {
      // Not a static file, fall through to SSR
    }

    return serverHandler.fetch(req);
  }
});

console.log(`Server listening on ${process.env.HOST || "0.0.0.0"}:${process.env.PORT || 3001}`);
