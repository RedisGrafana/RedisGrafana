# Developing Redis Application plug-in

![CI](https://github.com/RedisGrafana/grafana-redis-app/workflows/CI/badge.svg)
![Docker](https://github.com/RedisGrafana/grafana-redis-app/workflows/Docker/badge.svg)
[![codecov](https://codecov.io/gh/RedisGrafana/grafana-redis-app/branch/master/graph/badge.svg?token=15SIRGU8SX)](https://codecov.io/gh/RedisGrafana/grafana-redis-app)
[![Language grade: JavaScript](https://img.shields.io/lgtm/grade/javascript/g/RedisGrafana/grafana-redis-app.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/RedisGrafana/grafana-redis-app/context:javascript)

Developing Application plug-in involves setting up the development environment (which can be either Linux-based or macOS-based), building and running tests.

## Install Grafana

Grafana can be used in Docker or installed locally:

- Follow [Installation instructions](https://grafana.com/docs/grafana/latest/installation/) to install and start Grafana

- Open Grafana UI in web-browser `http://X.X.X.X:3000`

## Clone repository

```bash
git clone https://github.com/RedisGrafana/grafana-redis-app.git
```

## Build Application

- Install the latest version of Node.js using [Node Version Manager](https://github.com/nvm-sh/nvm) or [download binaries](https://nodejs.org/en/download/)

- Install `yarn` globally

```bash
npm install yarn -g
```

- Install dependencies

```bash
yarn install
```

- Build frontend components

```bash
yarn build
```

## Start Grafana

=== "Docker Compose"

    --8<-- "includes/docker-prerequisite.md"

    ```bash
    yarn start:dev
    ```

    Docker-compose file for Development includes:

    - Service `redis` using [Redismod](https://hub.docker.com/r/redislabs/redismod)
    - Service `grafana` using [Grafana](https://hub.docker.com/r/grafana/grafana) which allow loading unsigned plugins `redis-app` and `redis-datasource`

    !!! summary "Redis Data Source"

        Redis Data Source should be cloned and built following [Instructions](redis-datasource.md).

    --8<-- "includes/redis-app/docker-dev.md"

=== "Update local Grafana Configuration"

    Move distribution to Grafana's `plugins/` folder

    ```bash
    mv dist/ /var/lib/grafana/plugins/redis-app
    ```

    Add `redis-app` to allowed unsigned plugins

    ```bash
    vi /etc/grafana/grafana.ini
    ```

    --8<-- "includes/redis-app/grafana-ini.md"

    Restart and verify that plugin is registered

    ```bash
    tail -100 /var/log/grafana/grafana.log
    ```

## Configuration

The [Overview](../redis-app/overview.md) page explains how to enable plug-in and manage multiple Redis Data Sources.

## Contact Us

If you have questions, enhancement ideas or running into issues, please open an [issue](https://github.com/RedisGrafana/grafana-redis-app/issues/new/choose).
