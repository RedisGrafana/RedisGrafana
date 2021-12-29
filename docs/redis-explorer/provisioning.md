---
hide: toc
---

# Provisioning

Grafana supports managing data sources and applications by adding one or more YAML config files in the `provisioning/datasources` and `provisioning/plugins` folder:

- Each config file can contain a list of data sources or applications that will be updated during start up.
- Grafana updates each data source and application to match the configuration file.
- It is possible to use environment variable interpolation.

## Redis Explorer

---8<-- "includes/redis-explorer/provisioning-yaml.md"

## Redis Enteprise Software Data Source

---8<-- "includes/redis-explorer/re-software/provisioning-yaml.md"

## Redis Data Source

To learn how to provision Redis Data Source using YAML config files follow the [Redis Data Source provisioning](../redis-datasource/provisioning.md) page.
