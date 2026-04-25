# Docker

Hands-on Docker exercises covering containerization, networking, orchestration, logging, and production deployment patterns. Each task builds on the previous one.

---

## BLOCK 1 — Containers & Images

### D1 — Containerize a Web App
Build a production Dockerfile for a Node.js or Python app.
- Use slim base image
- Run as non-root user
- Add HEALTHCHECK endpoint
- Use .dockerignore
- Support ENV-based port config
- (Optional) multi-stage build

---

### D2 — Image Layers & Caching
Optimize Docker build performance.
- Order Dockerfile for caching (deps first, code later)
- Use build args + LABEL (version, maintainer, build date)
- Tag image (latest + versioned)
- Push to registry
- Verify cache reuse on rebuild

---

### D3 — Environment & Secrets
Handle config safely.
- Use environment variables for config
- Add .env.example (no real secrets)
- Run with --env-file
- Explain ARG vs ENV
- (Optional) Docker secrets demo

---

## BLOCK 2 — Docker Compose

### D4 — Multi-Container App
Compose API + Postgres.
- Named volume for DB persistence
- DB healthcheck + depends_on
- Use .env for credentials
- Expose only API port
- (Optional) Adminer/pgAdmin

---

### D5 — Nginx Reverse Proxy
Central entry point via Nginx.
- Nginx proxies / → frontend, /api → backend
- Only Nginx exposes port 80
- Multi-stage builds for services
- (Optional) rate limiting

---

### D6 — Networking & Isolation
Secure internal service communication.
- frontend-net and backend-net
- nginx bridges both networks
- backend-net set to internal: true
- verify frontend cannot reach DB
- inspect networks

---

## BLOCK 3 — Production Patterns

### D7 — Logging & Observability
Centralized logging system.
- JSON structured logs
- Docker logging driver (json-file limits)
- Loki + Grafana setup
- override file for dev logging
- (Optional) error filters + alerts

---

### D8 — Health Checks & Restart Policies
Make system self-healing.
- restart: unless-stopped
- proper HEALTHCHECK in Dockerfiles
- tuned intervals/retries/start_period
- simulate crashes and observe restart behavior
- script to monitor containers

## Rules
- Never commit secrets (.env, keys)
- Always use .env.example
- Keep images minimal
- Use proper Docker layering
- Prefer internal networking over exposed services