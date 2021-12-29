---
hide: toc
---

# Provisioning

Grafana supports managing data sources by adding one or more YAML config files in the `provisioning/datasources` folder:

- Each config file can contain a list of data sources that will be updated during start up.
- Grafana updates each data source to match the configuration file.
- It is possible to use environment variable interpolation.

Follow [Provisioning Grafana](https://grafana.com/docs/grafana/latest/administration/provisioning/) in documentation for examples.

## Standalone

---8<-- "includes/redis-datasource/config/standalone-yaml.md"

## Sentinel

---8<-- "includes/redis-datasource/config/sentinel-yaml.md"

## Standalone with SSL enabled

---8<-- "includes/redis-datasource/config/ssl-yaml.md"
