# Command Latency (Graph and Table)

Redis is often used in the context of demanding use cases, where it serves a large number of queries per second per instance, and at the same time, there are very strict latency requirements both for the average response time and for the worst case latency.

!!! note "This panel is a part of [Redis CLI dashboard](dashboards.md)."

This panel provides commands's latency based on [INFO COMMANDSTATS](../redis-datasource/INFO.md). Information is provide in Graph and table views.

## Graph view

![Latency-Graph](https://raw.githubusercontent.com/RedisGrafana/grafana-redis-app/master/src/img/redis-latency-panel-graph.png)

## Table view

![Latency-Table](https://raw.githubusercontent.com/RedisGrafana/grafana-redis-app/master/src/img/redis-latency-panel-table.png)
