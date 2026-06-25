FROM oven/bun:1-alpine AS base
WORKDIR /usr/src/app

COPY package.json bun.lock bunfig.toml ./
RUN bun install

COPY . .
ARG VITE_API_URL
ENV VITE_API_URL=$VITE_API_URL
RUN bun run build

EXPOSE 3000

ENV PORT=3000
ENV HOST=0.0.0.0
ENV NODE_ENV=production

CMD ["bun", "run", "start"]
