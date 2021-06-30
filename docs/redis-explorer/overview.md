# Redis Explorer plugin

The Redis Explorer is a plugin for Grafana that allows connecting to Redis Enterprise software clusters using REST API. It provides application pages to add Redis Data Sources for managed databases and dashboards to see cluster configuration.

## Quickstart

To learn how to install Redis Explorer plugin using `grafana-cli`, run using Docker or manually without Internet access follow the [Quickstart](../quickstart.md) page.

## Enable Plugin

The Redis Explorer plugin is disabled after installation by default. To enable:

- Go to `Configuration` -> `Plugins` and choose Redis Explorer plugin.

![Grafana plugins](../images/select-plugins.png)

- Click **Enable** to add side menu, add Redis Enterprise software data source and import Dashboards.

![Enable Redis Explorer plugin](../images/redis-explorer/enable.png)

## Home

The **Home** page connects to every configured data source and retrieve cluster's name.

!!! important "Loading Time"

    Page load can take a long time if clusters located far away from Grafana or data source can't connect (timeout).

![Manage Redis Data Sources](../images/redis-explorer/home.png)

### Add Redis Enterprise Software Data Source

To add new data source click on **Add Redis Enterprise Software** button and configure data source providing connection details.

### Add Redis databases

To add databases managed by Redis Enterprise cluster as Data Sources click on the **Databases** button.

![Databases](../images/redis-explorer/databases.png)

## Dashboards

Redis Explorer plugin includes predefined dashboards:

- [Enterprise Clusters](dashboards/explorer.md)
- [Cluster Overview](dashboards/overview.md)
- [Cluster Nodes](dashboards/nodes.md)
- [Cluster Databases](dashboards/databases.md)

!!! important "Application Icon"

    All dashboards are accessible from the Application's icon in the left side menu.

![Redis Application plugins](../images/redis-explorer/menu.png)

## Provisioning

To learn how to provision Redis Explorer using YAML config files follow the [Provisioning](provisioning.md) page.
