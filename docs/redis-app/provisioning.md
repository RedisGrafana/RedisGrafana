---
hide: toc
---

# Provisioning

Grafana supports managing applications by adding one or more YAML config files in the `provisioning/plugins` folder:

- Each config file can contain a list of applications that will be updated during start up.
- Grafana updates each application to match the configuration file.
- It is possible to use environment variable interpolation.

Follow [Provisioning Grafana](https://grafana.com/docs/grafana/latest/administration/provisioning/) in documentation for examples.

## Redis Application

---8<-- "includes/redis-app/provisioning-yaml.md"

## Redis Data Source

To learn how to provision Redis Data Source using YAML config files follow the [Redis Data Source provisioning](../redis-datasource/provisioning.md) page.
