## Healthcheck Design

- interval: 30s → avoids excessive checks
- timeout: 5s → fail fast if service is stuck
- retries: 3 → tolerate temporary hiccups
- start_period: 10–20s → gives containers time to boot
