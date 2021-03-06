# Developing Redis Data Source

[![Go Report Card](https://goreportcard.com/badge/github.com/RedisGrafana/grafana-redis-datasource)](https://goreportcard.com/report/github.com/RedisGrafana/grafana-redis-datasource)
![CI](https://github.com/RedisGrafana/grafana-redis-datasource/workflows/CI/badge.svg)
[![codecov](https://codecov.io/gh/RedisGrafana/grafana-redis-datasource/branch/master/graph/badge.svg?token=YX7995RPCF)](https://codecov.io/gh/RedisGrafana/grafana-redis-datasource)
[![Language grade: JavaScript](https://img.shields.io/lgtm/grade/javascript/g/RedisGrafana/grafana-redis-datasource.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/RedisGrafana/grafana-redis-datasource/context:javascript)

Developing Redis Data Source involves setting up the development environment (which can be either Linux-based or macOS-based), building and running tests.

## Install Grafana

Grafana can be started in Docker or installed locally:

- Follow [Installation instructions](https://grafana.com/docs/grafana/latest/installation/) to install and start Grafana

- Open Grafana UI in web-browser `http://X.X.X.X:3000`

## Clone repository

```bash
git clone https://github.com/RedisGrafana/grafana-redis-datasource.git
```

## Build

### Frontend

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

### Backend

- Install [Golang](https://golang.org/dl/) for your platform

```bash
yum install go
```

- Install [Grafana plugin SDK for Go](https://grafana.com/docs/grafana/latest/developers/plugins/backend/grafana-plugin-sdk-for-go/) dependency

```bash
go get -u github.com/grafana/grafana-plugin-sdk-go
```

- Install [Mage](https://magefile.org/) (make-like build tool using Go)

```bash
git clone https://github.com/magefile/mage
cd mage
go run bootstrap.go
```

- Build backend binaries for Linux, Windows and MacOS for supported platforms

```bash
yarn build:backend
```

## Start Grafana

=== "Docker Compose"

    --8<-- "includes/docker-prerequisite.md"

    ```bash
    yarn start:dev
    ```

=== "Update local Grafana Configuration"

    Move distribution to Grafana's `plugins/` folder

    ```bash
    mv dist/ /var/lib/grafana/plugins/redis-datasource
    ```

    Add `redis-datasource` to allowed unsigned plugins

    ```bash
    vi /etc/grafana/grafana.ini
    ```

    --8<-- "includes/redis-datasource/grafana-ini.md"

    Restart Grafana and verify that plugin registered

    ```bash
    tail -100 /var/log/grafana/grafana.log
    ```

    --8<-- "includes/redis-datasource/grafana-log.md"

## Configuration

The [Redis Data Source Configuration](../redis-datasource/configuration.md) page explains how to connect data source to Redis database.

## Contact Us

If you have questions, enhancement ideas or running into issues, please open an [issue](https://github.com/RedisGrafana/grafana-redis-datasource/issues/new/choose).
