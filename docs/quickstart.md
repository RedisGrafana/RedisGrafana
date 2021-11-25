# Quickstart

## Architecture

The Redis plugins for Grafana consists of Redis Data Source, Redis Application and Redis Explorer.

![Architecture](/images/redis-plugins.png)

## Install using `grafana-cli`

Use the `grafana-cli` tool to install from the command line:

### Redis Application plugin and Redis Data Source

```bash
grafana-cli plugins install redis-app
```

### Redis Explorer plugin

!!! important "Dependencies"

    Redis Application plugin and Redis Data Source will be auto-installed as dependencies.

```bash
grafana-cli plugins install redis-explorer-app
```

### Redis Data Source

```bash
grafana-cli plugins install redis-datasource
```

## Run using `Docker`

--8<-- "includes/login-grafana.md"

--8<-- "includes/docker-background.md"

### Redis Application plugin and Redis Data Source

```bash
docker run -p 3000:3000 --name=grafana -e "GF_INSTALL_PLUGINS=redis-app" grafana/grafana
```

### Redis Data Source

```bash
docker run -p 3000:3000 --name=grafana -e "GF_INSTALL_PLUGINS=redis-datasource" grafana/grafana
```

### Redis Explorer

```bash
docker run -p 3000:3000 --name=grafana -e "GF_INSTALL_PLUGINS=redis-explorer-app" grafana/grafana
```

## Docker Images

Are you interested in the latest features and updates? Start nightly built [Docker image](development/images.md).

## Install without Internet access

### Redis Data Source

- Download the latest version from the [Releases](https://github.com/RedisGrafana/grafana-redis-datasource/releases).
- Unzip an archive to the `plugins/` folder for local Grafana installation or Docker's volume.
- Check permissions for the `redis-datasource` binaries:

--8<-- "includes/redis-datasource/permissions.md"

- Check that plugin was registered:

--8<-- "includes/redis-datasource/grafana-log.md"

### Redis Application plugin

- Download the latest version from the [Releases](https://github.com/RedisGrafana/grafana-redis-app/releases).
- Unzip an archive to the `plugins/` folder for local Grafana installation or Docker's volume.

### Redis Explorer plugin

!!! important "Dependencies"

    Redis Explorer plugin requires Redis Data Source and Redis Application plugin.

- Download the latest version from the [Releases](https://github.com/RedisGrafana/grafana-redis-explorer/releases).
- Unzip an archive to the `plugins/` folder for local Grafana installation or Docker's volume.

## Configuration

### Redis Data Source

The [Configuration](redis-datasource/configuration.md) page explains how to connect the data source to the Redis database.

### Redis Application plugin

The [Overview](redis-app/overview.md) page explains how to enable plugin and manage Redis Data Sources.

### Redis Explorer plugin

The [Overview](redis-explorer/overview.md) page explains how to enable plugin and manage Redis Enterprise Software Data Sources.

## Learn more

Please look at [Learn More](learn-more.md) page to read recent blog posts and view video presentations from the conferences.
