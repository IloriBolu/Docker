# Image Layers & Caching

## Goal

Understand how Docker layer caching works and optimize the Dockerfile for faster rebuilds.

---

## Project Structure

```
.
├── Dockerfile
├── requirements.txt
├── app.py
└── package.json (if using Node instead of Python)
```

---

## 🐳 Optimized Dockerfile

```dockerfile
FROM python:3.10-slim

# Build arguments
ARG VERSION=1.0.0
ARG BUILD_DATE
ARG MAINTAINER="Boluwatife"

# Metadata
LABEL version=$VERSION \
      maintainer=$MAINTAINER \
      build_date=$BUILD_DATE

WORKDIR /app

# Copy dependencies FIRST (for caching)
COPY requirements.txt .

RUN pip install -r requirements.txt

# Copy source code AFTER dependencies
COPY app.py .

CMD ["python", "app.py"]
```

---

## Why this works

Docker builds images in layers. By copying `requirements.txt` before the source code:

* Dependencies are installed only when `requirements.txt` changes
* Code changes do NOT invalidate dependency layers
* This makes rebuilds much faster

---

## Build Process

### First build

```bash
docker build \
  --build-arg VERSION=1.0.0 \
  --build-arg BUILD_DATE=$(date -u +%Y-%m-%dT%H:%M:%SZ) \
  -t myapp:1.0.0 \
  -t myapp:latest .
```

---

### Second build (should use cache)

```bash
docker build \
  --build-arg VERSION=1.0.0 \
  --build-arg BUILD_DATE=$(date -u +%Y-%m-%dT%H:%M:%SZ) \
  -t myapp:1.0.0 \
  -t myapp:latest .
```

Expected output:

```
CACHED [2/4] COPY requirements.txt
CACHED [3/4] RUN pip install -r requirements.txt
```

---

## Image Tagging

Two tags are used:

* `myapp:1.0.0` → specific version
* `myapp:latest` → most recent build

---

## Push to Registry

### Docker Hub

```bash
docker tag myapp:1.0.0 <your-username>/myapp:1.0.0
docker tag myapp:latest <your-username>/myapp:latest

docker push <your-username>/myapp:1.0.0
docker push <your-username>/myapp:latest
```

---

## Cache Validation (Checkpoint)

1. Build the image
2. Modify ONLY `app.py`
3. Rebuild

Expected:

* `COPY requirements.txt` →  CACHED
* `RUN pip install` → CACHED
* `COPY app.py` → rebuilt

This proves caching is working correctly.

---

## Challenge (Build Args)

Instead of hardcoding version:

```bash
docker build --build-arg VERSION=2.0.0 ...
```

This allows dynamic versioning without editing the Dockerfile.

---

## Summary

* Docker layers were reordered for maximum cache reuse
* Build args used for dynamic metadata
* Image tagged with semantic version + latest
* Cache verified by modifying only source code

---
