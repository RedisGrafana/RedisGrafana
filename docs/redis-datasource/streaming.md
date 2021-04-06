---
hide: toc
---

# Streaming Data Source

Redis Data Source supports Streaming. Please take a look at the [specific command](commands.md) for details.

!!! note "A dot in the top right corner"

    Since Grafana 7.4 a dot in the top right corner means that Streaming is enabled.

![Streaming](../images/redis-datasource/commands/info-ops-sec.png)

## Parameters

| Parameter | Description                                                              | Default     |
| --------- | ------------------------------------------------------------------------ | ----------- |
| Interval  | Streaming interval in milliseconds                                       | 1000 ms     |
| Capacity  | Values will be constantly added and will never exceed the given capacity | 1000 ms     |
| Data type | Streaming data supported as Time series and Data frames                  | Time series |

## Time series

When selected, `time` field will be added or replaced to allow visualize values using Graph or Time Series (Grafana 7.4+) panels.

!!! important "Multi-line results"

    If the command returns more than one line, the last line of data will be returned.

![XLEN](../images/redis-datasource/commands/xlen.png)

## Data frame

When selected, data will be refreshed as is.

![RG.DUMPREGISTRATIONS](../images/redis-datasource/commands/rg-dumpregistrations.png)
