# Redis Explorer plug-in

![Release](https://img.shields.io/github/v/release/redisgrafana/grafana-redis-explorer.svg) [![Docker](https://github.com/RedisGrafana/grafana-redis-explorer/workflows/Docker/badge.svg)](https://github.com/orgs/RedisGrafana/packages/container/package/redis-explorer)

The Redis Explorer is a plug-in for Grafana that allows to connect to Redis Enterprise software clusters using REST API. It provides application pages to add Redis Data Sources for managed databases and dashboards to see cluster configuration.

## Enable Plug-in

The Redis Explorer plug-in is disabled after installation by default. To enable:

- Go to `Configuration` -> `Plugins` and choose Redis Explorer plug-in.

![Grafana plug-ins](../images/redis-explorer/grafana-plugins.png)

- Click **Enable** to add side menu, add Redis Enterprise software data source and import Dashboards.

![Enable Redis Explorer plug-in](../images/redis-explorer/enable.png)

## Home

The **Home** page connects to every configured data source and retrieve cluster's name.

!!! important "Loading Time"

    Page load can take a long time if clusters located far away from Grafana or data source can't connect (timeout).

![Manage Redis Data Sources](../images/redis-explorer/home.png)

### Add Redis Enterprise Software Data Source

To add data source click on **Add Redis Enterprise Software** and configure data source providing connection details.

## Dashboards

Redis Explorer plug-in includes predefined dashboards:

- Enterprise Clusters
- Cluster Overview
- Cluster Nodes
- Cluster Databases

!!! important "Application Icon"

    All dashboards are accessible from the Application's icon in the left side menu.

![Redis Application plug-ins](../images/redis-explorer/menu.png)

## Privisioning

Grafana supports managing plugins in Grafana by [adding one or more YAML config files](https://grafana.com/docs/grafana/latest/administration/provisioning/) in the **provisioning/plugins** directory:

- Each config file can contain a list of apps that will be updated during start up.
- Grafana updates each app to match the configuration file.

---8<-- "includes/redis-explorer/provisioning-yaml.md"
