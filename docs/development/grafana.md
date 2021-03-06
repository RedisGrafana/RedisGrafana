---
hide: toc
---

# Docker Images for Grafana

--8<-- "includes/login-grafana.md"

## Redis Application plugin

![Redis Application plugin](https://github.com/RedisGrafana/grafana-redis-app/workflows/Docker/badge.svg)

The Redis Application is a plugin for Grafana that provides application pages and custom panels for Redis Data Source.

```bash
docker pull ghcr.io/redisgrafana/redis-app:latest && \
docker run -p 3000:3000 --name=redis-app ghcr.io/redisgrafana/redis-app:latest
```

### Master (Main) build

Based on Grafana's Master (Main) branch.

```bash
docker pull ghcr.io/redisgrafana/redis-app:master && \
docker run -p 3000:3000 --name=redis-app ghcr.io/redisgrafana/redis-app:master
```

## Redis Explorer plugin

![Redis Explorer plugin](https://github.com/RedisGrafana/grafana-redis-explorer/workflows/Docker/badge.svg)

The Redis Explorer is a plugin for Grafana that allows users to connect to Redis Enterprise software clusters using REST API and build dashboards to observe their status.

```bash
docker pull ghcr.io/redisgrafana/redis-explorer:latest && \
docker run -p 3000:3000 --name=explorer ghcr.io/redisgrafana/redis-explorer:latest
```

### Master (Main) build

Based on Grafana's Master (Main) branch.

```bash
docker pull ghcr.io/redisgrafana/redis-explorer:master && \
docker run -p 3000:3000 --name=redis-app ghcr.io/redisgrafana/redis-explorer:master
```
