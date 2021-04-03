# Redis Application plug-in

![Release](https://img.shields.io/github/v/release/redisgrafana/grafana-redis-app.svg) [![Plugin Downloads](https://img.shields.io/badge/dynamic/json?color=green&label=downloads&query=%24.downloads&url=https%3A%2F%2Fgrafana.com%2Fapi%2Fplugins%2Fredis-app)](https://grafana.com/grafana/plugins/redis-app)
[![Docker](https://github.com/RedisGrafana/grafana-redis-app/workflows/Docker/badge.svg)](https://github.com/orgs/RedisGrafana/packages/container/package/redis-app)

The Redis Application is a plug-in for Grafana that provides application pages and custom panels for Redis Data Source.

Plug-in's **Home** page helps to manage Redis Data Sources and provides quick access to dashboards.

## Home

The **Home** page connects to every configured data source and checks available Redis Modules using the `command` command.

!!! important "Loading Time"

    Page load can take a long time if data sources located far away from Grafana or Redis Data Source can't connect to the database.

![Manage Redis Data Sources](../images/redis-app/home.png)

### Add Redis Data Source

To add Redis Data Source click on **Add Redis Data Source** and configure data source following [Configuration](../redis-datasource/configuration.md) page.

## Dashboards

Redis Application plug-in includes predefined dashboards:

- [CLI (Command Line Interface)](dashboards/cli.md)
- [Redis Overview](dashboards/overview.md)
- [RedisGears](dashboards/redis-gears.md)

!!! important "Application Icon"

    All dashboards are accessible from the Application's icon in the left side menu.

![Redis Application plug-ins](../images/redis-app/menu.png)

## Custom panels

Redis Application plug-in provides custom panels for Redis Data Source:

- [Command line interface (CLI)](panels/redis-cli-panel.md)
- [Command Latency](panels/redis-latency-panel.md)
- [Keys consuming a lot of memory](panels/redis-keys-panel.md)
- [RedisGears Script Editor](panels/redis-gears-panel.md)
