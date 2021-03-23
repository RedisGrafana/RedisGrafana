# Developing Redis Data Source for Grafana

Developing Redis Data Source involves setting up the development environment (which can be either Linux-based or macOS-based), building and running tests.

## Install Grafana

!!! important "Grafana can be used in Docker or installed locally"

- Follow [Installation](https://grafana.com/docs/grafana/latest/installation/) to install and start Grafana

- Open Grafana in web-browser `http://X.X.X.X:3000`

## Clone repository

```bash
git clone https://github.com/RedisGrafana/grafana-redis-datasource.git
```

## Build Data Source Frontend

- Install the latest version of Node.js using [Node Version Manager](https://github.com/nvm-sh/nvm)

- Install `yarn` globally

```bash
npm install yarn -g
```

- Install dependencies

```bash
yarn install
```

- Build Data Source

```bash
yarn build
```

## Build Data Source Backend

- Install Golang

```bash
yum install go
```

- Install [Grafana plugin SDK for Go](https://grafana.com/docs/grafana/latest/developers/plugins/backend/grafana-plugin-sdk-for-go/) dependency

```bash
go get -u github.com/grafana/grafana-plugin-sdk-go
```

- Install mage (make-like build tool using Go)

```bash
git clone https://github.com/magefile/mage
cd mage
go run bootstrap.go
```

- Build backend binaries for Linux, Windows and MacOS for ARM and AMD64 platforms

```bash
yarn build:backend
```

## Update local Grafana Configuration

- Move distribution to Grafana's `plugins/` folder

```bash
mv dist/ /var/lib/grafana/plugins/redis-datasource
```

- Add `redis-datasource` to allowed unsigned plugins

```bash
vi /etc/grafana/grafana.ini
```

```
{{ include('redis-datasource-grafana.ini') }}
```

- Verify that plugin registered

```bash
tail -100 /var/log/grafana/grafana.log
```

```
{{ include('redis-datasource-grafana.log') }}
```

## Start using Docker Compose

!!! important "Docker Compose should be pre-installed following [documentation](https://docs.docker.com/compose/install/)"

```
yarn start:dev
```

## Configure Redis Data Source

!!! note "The [Configuration](../redis-datasource/configuration.md) page explains how to configure Redis Data Source"

![Data Source](https://raw.githubusercontent.com/RedisGrafana/grafana-redis-datasource/master/src/img/datasource.png)

!!! note "If you have questions, enhancement ideas or running into issues, please open an [issue](https://github.com/RedisGrafana/grafana-redis-datasource/issues/new/choose)"
