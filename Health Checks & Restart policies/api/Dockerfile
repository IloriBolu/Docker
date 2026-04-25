FROM python:3.10-slim

WORKDIR /app
COPY app.py .

RUN pip install flask

# Healthcheck → hits the API itself
HEALTHCHECK --interval=30s --timeout=5s --retries=3 --start-period=10s \
  CMD curl -f http://localhost:5000/ || exit 1

CMD ["python", "app.py"]