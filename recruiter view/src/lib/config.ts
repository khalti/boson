const isServer = typeof window === "undefined";
export const API_BASE = isServer
  ? (typeof process !== "undefined" && process.env ? process.env.API_URL : undefined)
  : import.meta.env.VITE_API_URL;

if (!API_BASE) {
  throw new Error("API_BASE environment variable (API_URL or VITE_API_URL) is not defined!");
}
