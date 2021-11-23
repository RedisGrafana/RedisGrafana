---
hide: toc
---

# Docker Images for Redis

## Redis-Prophet for Time series forecasting

[![Docker](https://github.com/RedisGrafana/redis-finance-prophet/actions/workflows/docker.yml/badge.svg)](https://github.com/RedisGrafana/redis-finance-prophet/actions/workflows/docker.yml)

The Redis-Prophet Docker image is based on the latest version of RedisTimeSeries, RedisGears with Prophet pre-installed and can be used for any time series forecasting project.

```bash
docker pull ghcr.io/redisgrafana/redis-prophet:latest && \
docker run -p 6379:6379 --name=redis-prophet ghcr.io/redisgrafana/redis-prophet:latest
```

## Redis-OpenCV for Real-time computer vision

[![Docker](https://github.com/RedisGrafana/redis-camera-ai/actions/workflows/docker.yml/badge.svg)](https://github.com/RedisGrafana/redis-camera-ai/actions/workflows/docker.yml)

The Redis-OpenCV Docker image is based on the latest version of RedisTimeSeries, RedisGears with OpenCV pre-installed, RedisAI and can be used for any real-time computer vision projects.

```bash
docker pull ghcr.io/redisgrafana/redis-opencv:latest && \
docker run -p 6379:6379 --name=redis-opencv ghcr.io/redisgrafana/redis-opencv:latest
```

## Redis-JSG for Search and Graph JSON data

[![Docker](https://github.com/RedisGrafana/grafana-plugin-stats/actions/workflows/docker.yml/badge.svg)](https://github.com/RedisGrafana/grafana-plugin-stats/actions/workflows/docker.yml)

The Redis-JSG Docker image is based on the latest version of RedisJSON, RediSearch, RedisGraph and RedisGears.

```bash
docker pull ghcr.io/redisgrafana/redis-jsg:latest && \
docker run -p 6379:6379 --name=redis-opencv ghcr.io/redisgrafana/redis-jsg:latest
```
