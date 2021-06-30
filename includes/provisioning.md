Grafana supports managing data sources by adding one or more YAML config files in the `provisioning/datasources` folder:

- Each config file can contain a list of apps that will be updated during start up.
- Grafana updates each app to match the configuration file.
- It is possible to use environment variable interpolation.

Follow [Provisioning Grafana](https://grafana.com/docs/grafana/latest/administration/provisioning/) in documentation for examples.
