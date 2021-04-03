# Quickstart

## Install using `grafana-cli`

Use the `grafana-cli` tool to install from the command-line:

=== "Redis Application plug-in and Redis Data Source"

    ```bash
    grafana-cli plugins install redis-app
    ```

=== "Redis Data Source"

    ```bash
    grafana-cli plugins install redis-datasource
    ```

## Run using `Docker`

--8<-- "includes/login-grafana.md"

=== "Redis Application plug-in and Redis Data Source"

    ```bash
    docker run -d -p 3000:3000 --name=grafana -e "GF_INSTALL_PLUGINS=redis-app" grafana/grafana
    ```

=== "Redis Data Source"

    ```bash
    docker run -d -p 3000:3000 --name=grafana -e "GF_INSTALL_PLUGINS=redis-datasource" grafana/grafana
    ```

!!! note "Docker Images"

    Interested in the latest features and updates? Start nightly built [Docker image](development/images.md).

## Install without Internet access

### Redis Data Source

- Download the latest version from [Releases](https://github.com/RedisGrafana/grafana-redis-datasource/releases).
- Unzip an archive to the `plugins/` folder for local Grafana installation or Docker's volume.
- Check permissions for the `redis-datasource` binaries:

!!! important "Permissions"

    Redis Data Source binaries should have executable permissions for Grafana to be able to execute it.

    --8<-- "includes/redis-datasource/binaries.md"

- Check that plug-in was registered:

--8<-- "includes/redis-datasource/grafana-log.md"

### Redis Application plug-in

- Download the latest version from [Releases](https://github.com/RedisGrafana/grafana-redis-app/releases).
- Unzip an archive to the `plugins/` folder for local Grafana installation or Docker's volume.

--8<-- "includes/redis-app/enable.md"

## Configuration

### Redis Data Source

The [Configuration](redis-datasource/configuration.md) page explains how to connect data source to Redis database.

### Redis Application plug-in

The [Overview](redis-app/overview.md) page explains how to add and manage multiple Redis Data Sources.
