# Quickstart

!!! important "Only Grafana 7.1 and later with a new plug-in platform supported."

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

### Redis Application plug-in and Redis Data Source

```bash
docker run -d -p 3000:3000 --name=grafana -e "GF_INSTALL_PLUGINS=redis-app" grafana/grafana
```

### Redis Data Source

```bash
docker run -d -p 3000:3000 --name=grafana -e "GF_INSTALL_PLUGINS=redis-datasource" grafana/grafana
```

## Enable Redis Application plug-in

!!! important "Redis Application plug-in is disabled by default."

Go to `Configuration` -> `Plugins` and enable Redis Application plug-in.

## Configure Redis Data Source

!!! note "The [Configuration](redis-datasource/configuration.md) page explains how to configure Redis Data Source."

Open Grafana in your browser and configure Redis Data Source. You can add as many data sources as you want to support multiple Redis databases.

![Datasource](https://raw.githubusercontent.com/RedisGrafana/grafana-redis-datasource/master/src/img/datasource.png)
