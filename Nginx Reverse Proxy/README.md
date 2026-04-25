# Nginx Reverse Proxy

## Goal

Route all traffic through Nginx instead of exposing services directly.

---

## Architecture

```id="arch1"
        ┌───────────────┐
        │   Browser     │
        │ curl / client │
        └───────┬───────┘
                │
                ▼
        ┌───────────────┐
        │     Nginx     │  (port 80 exposed)
        │ reverse proxy │
        └───────┬───────┘
        /                \
       /                  \
      ▼                    ▼
┌────────────┐     ┌────────────┐
│  Frontend  │     │    API     │
│  (static)  │     │  backend   │
└────────────┘     └────────────┘
```

---

## How it works

* Nginx listens on port 80
* Requests to `/` → forwarded to frontend service
* Requests to `/api` → forwarded to API service
* Only Nginx is exposed to the host
* All other services run internally in Docker networks

---

## nginx.conf

```nginx id="nginxconf1"
events {}

http {
    # rate limit: 10 requests per second per IP
    limit_req_zone $binary_remote_addr zone=api_limit:10m rate=10r/s;

    server {
        listen 80;

        location / {
            proxy_pass http://frontend:80;
        }

        location /api/ {
            limit_req zone=api_limit burst=20 nodelay;
            proxy_pass http://api:5000/;
        }
    }
}
```

---

## Docker Compose Rules

* Only Nginx exposes a port:

```id="compose1"
ports:
  - "80:80"
```

* No other service has a `ports` section

---

## Multi-stage builds

### Frontend (example)

```dockerfile id="frontend1"
FROM node:18 AS build
WORKDIR /app
COPY package.json .
RUN npm install
COPY . .
RUN npm run build

FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html
```

---

### API (example)

```dockerfile id="api1"
FROM python:3.10-slim AS base
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

FROM base
COPY app.py .
CMD ["python", "app.py"]
```

---

## Testing

### API through Nginx

```bash id="test1"
curl http://localhost/api/items
```

Expected: response from API

---

### Frontend through Nginx

```bash id="test2"
curl http://localhost/
```

Expected: frontend HTML

---

## Rate Limiting

* `/api` limited to **10 requests per second per IP**
* Burst allowed: 20
* Excess requests return **429 Too Many Requests**

---

## Checkpoint

* `curl /api/...` → reaches API ✅
* `curl /` → reaches frontend ✅
* Only Nginx exposed → ✅
* Rate limiting active → ✅

---

## Summary

* Nginx acts as a single entry point
* Services are isolated and not directly exposed
* Reverse proxy routing works correctly
* Basic rate limiting added for API protection

---
