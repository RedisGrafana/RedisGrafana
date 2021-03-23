# Keys consuming a lot of memory

Do you want to know which keys consume a lot of memory in your Redis database? This panel is based on [TMSCAN](../redis-datasource/TMSCAN.md) to scan keys and sort results based on memory usage in the table format.

!!! note "This panel is a part of [Redis CLI dashboard](../dashboards.md)."

!!! warning "Please use this command in OFF-PEAK as it cause latency increase."

![Keys](https://raw.githubusercontent.com/RedisGrafana/grafana-redis-app/master/src/img/redis-keys-panel.png)

## Options

Interval and count for SCAN command is configurable to keep latency under control.
