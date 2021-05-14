# Redis Enterprise Software Data Source

Redis Enterprise Software Data Source allows connecting to Redis Enterprise software clusters using REST API.

!!! quote "REST API [Specification](https://storage.googleapis.com/rlecrestapi/rest-html/http_rest_api.html)"

    Redis Labs clusters are a set of nodes, typically two or more, providing database services. Clusters are inherently multi-tenant, and a single cluster can manage multiple databases accessed through individual endpoints.

## Configuration

The [Configuration](configuration.md) page explains how to connect data source to Redis Enterprise software.

![Data Source](../../images/redis-explorer/re-software/config-editor.png)

## Query Editor

1. Choose **Type** to select [Information](info.md) (Alerts, Cluster, License, etc.) or [Metrics](metrics.md)
2. Provide all required parameters, depends on selected **Type**

![Query Editor](../../images/redis-explorer/re-software/query-editor.png)

## Provisioning

Grafana supports managing data sources by [adding one or more YAML config files](https://grafana.com/docs/grafana/latest/administration/provisioning/) in the **provisioning/datasources** directory:

- Each config file can contain a list of datasources that will get added or updated during start up.
- If the data source already exists, then Grafana updates it to match the configuration file.

---8<-- "includes/redis-explorer/re-software/provisioning-yaml.md"
