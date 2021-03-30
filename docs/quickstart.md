# Quickstart

## Install using `grafana-cli`

Use the `grafana-cli` tool to install from the commandline.

### Redis Application plug-in and Redis Data Source

```bash
grafana-cli plugins install redis-app
```

### Redis Data Source

```bash
grafana-cli plugins install redis-datasource
```

## Run using `Docker`

!!! note "Username and password to login to Grafana is `admin`/`admin`."

### Redis Application plug-in and Redis Data Source

```bash
docker run -d -p 3000:3000 --name=grafana -e "GF_INSTALL_PLUGINS=redis-app" grafana/grafana
```

### Redis Data Source

```bash
docker run -d -p 3000:3000 --name=grafana -e "GF_INSTALL_PLUGINS=redis-datasource" grafana/grafana
```

## Install without Internet access

### Redis Data Source

- Download the latest version from [Releases](https://github.com/RedisGrafana/grafana-redis-datasource/releases).
- Unzip archive to `plugins/` folder for local Grafana installation or Docker plug-ins volume.
- Check permissions for `redis-datasource` binaries:

!!! important "Redis Data Source binaries should have executable permissions for Grafana to be able to execute it!"

```
{{ include('redis-datasource/binaries.txt')}}
```

- Check that plug-in was registered:

```
{{ include('redis-datasource/grafana.log') }}
```

### Redis Application plug-in

- Download the latest version from [Releases](https://github.com/RedisGrafana/grafana-redis-app/releases).
- Unzip archive to `plugins/` folder for local Grafana installation or Docker plug-ins volume.

## Enable Redis Application plug-in

!!! note "Redis Application plug-in is disabled by default."

Go to `Configuration` -> `Plugins` and choose Redis Application plug-in.

![Grafana plug-ins](images/grafana-plugins-app.png)

Click **Enable** to add side menu, [Custom panels](redis-app/panels.md) and import [Dashboards](redis-app/dashboards.md).

![Enable Redis Application plug-in](images/redis-app-enable.png)

## Configuration

### Redis Data Source

The [Redis Data Source Configuration](redis-datasource/configuration.md) page explains how to connect data source to Redis database.
