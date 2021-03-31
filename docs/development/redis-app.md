# Developing Redis Application plug-in for Grafana

![CI](https://github.com/RedisGrafana/grafana-redis-app/workflows/CI/badge.svg)
![Docker](https://github.com/RedisGrafana/grafana-redis-app/workflows/Docker/badge.svg)
[![codecov](https://codecov.io/gh/RedisGrafana/grafana-redis-app/branch/master/graph/badge.svg?token=15SIRGU8SX)](https://codecov.io/gh/RedisGrafana/grafana-redis-app)

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

    !!! important "Prerequisite"

        Docker Compose should be pre-installed following [documentation](https://docs.docker.com/compose/install/).

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

## Enable Redis Application plug-in

Redis Application plug-in is disabled by default. To enable:

- Go to `Configuration` -> `Plugins` and choose Redis Application plug-in.

![Grafana plug-ins](../images/redis-app/grafana-plugins.png)

- Click **Enable** to add side menu, [Custom panels](../redis-app/panels.md) and import [Dashboards](../redis-app/dashboards.md).

![Enable Redis Application plug-in](../images/redis-app/enable.png)

## Contact Us

If you have questions, enhancement ideas or running into issues, please open an [issue](https://github.com/RedisGrafana/grafana-redis-app/issues/new/choose).
