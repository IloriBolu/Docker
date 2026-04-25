FROM node:20-slim AS builder

WORKDIR /app

COPY package*.json ./
RUN npm install --omit=dev

COPY . .

FROM node:20-slim

WORKDIR /app

RUN useradd -m otheruser

COPY --from=builder /app /app

ENV PORT=3000

EXPOSE ${PORT}

USER otheruser

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
  CMD curl -f http://localhost:${PORT}/healthz || exit 1

CMD ["node", "server.js"]