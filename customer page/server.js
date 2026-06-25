import serverHandler from "./dist/server/server.js";
import { join } from "path";
import { statSync } from "fs";

Bun.serve({
  port: process.env.PORT || 3000,
  hostname: process.env.HOST || "0.0.0.0",
  async fetch(req) {
    const url = new URL(req.url);
    const filePath = join(process.cwd(), "dist/client", decodeURIComponent(url.pathname));
    
    try {
      if (statSync(filePath).isFile()) {
        return new Response(Bun.file(filePath));
      }
    } catch (e) {
      // Not a static file, let it fall through to SSR
    }
    
    // Pass to TanStack Start SSR handler
    return serverHandler.fetch(req);
  }
});

console.log(`Server listening on ${process.env.HOST || "0.0.0.0"}:${process.env.PORT || 3000}`);
