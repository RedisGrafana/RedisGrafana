# Redis Application plug-in

![Release](https://img.shields.io/github/v/release/redisgrafana/grafana-redis-app.svg) [![Plugin Downloads](https://img.shields.io/badge/dynamic/json?color=green&label=downloads&query=%24.downloads&url=https%3A%2F%2Fgrafana.com%2Fapi%2Fplugins%2Fredis-app)](https://grafana.com/grafana/plugins/redis-app)
[![Docker](https://github.com/RedisGrafana/grafana-redis-app/workflows/Docker/badge.svg)](https://github.com/orgs/RedisGrafana/packages/container/package/redis-app)

The Redis Application is a plug-in for Grafana that provides application pages and custom panels for Redis Data Source. The [Home](#home) page helps to manage Redis Data Sources and provides quick access to dashboards.

## Enable Plug-in

The Redis Application plug-in is disabled after installation by default. To enable:

- Go to `Configuration` -> `Plugins` and choose Redis Application plug-in.

![Grafana plug-ins](../images/redis-app/grafana-plugins.png)

- Click **Enable** to add side menu, Custom panels and import Dashboards.

![Enable Redis Application plug-in](../images/redis-app/enable.png)

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

## Privisioning

Grafana supports managing plugins in Grafana by [adding one or more YAML config files](https://grafana.com/docs/grafana/latest/administration/provisioning/) in the **provisioning/plugins** directory:

- Each config file can contain a list of apps that will be updated during start up.
- Grafana updates each app to match the configuration file.

---8<-- "includes/redis-app/provisioning-yaml.md"
