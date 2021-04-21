---
hide: toc
---

# Docker Images

Interested in the latest features and updates? Start nightly built Docker image. Supported platforms are:

- Linux/amd64
- Linux/arm64
- Linux/arm

!!! important "Unstable"

    Images built from the main branch and recommended for Testing new features and bugfixes only.

![Nightly built Docker images](../images/development/docker.png)

## Grafana

--8<-- "includes/login-grafana.md"

### Redis Application plug-in

![Redis Application plug-in](https://github.com/RedisGrafana/grafana-redis-app/workflows/Docker/badge.svg)

The Redis Application is a plug-in for Grafana that provides application pages and custom panels for Redis Data Source.

```bash
docker run -p 3000:3000 --name=redis-app ghcr.io/redisgrafana/redis-app:latest
```

??? bug "Master build"

    Special build based on the Grafana's Master branch.

    ```bash
    docker run -p 3000:3000 --name=redis-app ghcr.io/redisgrafana/redis-app:master
    ```

### Redis Explorer plug-in

![Redis Explorer plug-in](https://github.com/RedisGrafana/grafana-redis-explorer/workflows/Docker/badge.svg)

The Redis Explorer is a plug-in for Grafana that allows users to connect to Redis Enterprise software clusters using REST API and build dashboards to observe their status.

```bash
docker run -p 3000:3000 --name=explorer ghcr.io/redisgrafana/redis-explorer:latest
```

??? bug "Master build"

    Special build based on the Grafana's Master branch.

    ```bash
    docker run -p 3000:3000 --name=redis-app ghcr.io/redisgrafana/redis-explorer:master
    ```

## Redis

### Redis-Prophet

[![Docker](https://github.com/RedisGrafana/redis-finance-prophet/actions/workflows/docker.yml/badge.svg)](https://github.com/RedisGrafana/redis-finance-prophet/actions/workflows/docker.yml)

The Redis-Prophet Docker image based on the latest version of RedisTimeSeries, RedisGears with Prophet pre-installed and can be used for any project for time series forecasting.

```bash
$ docker run -p 6379:6379 --name=redis-prophet ghcr.io/redisgrafana/redis-prophet:latest
```
