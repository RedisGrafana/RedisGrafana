---
hide: toc
---

# TS.MRANGE

This command query a timestamp range across multiple time series by a filter.

!!! info "RedisTimeSeries"

    [https://oss.redislabs.com/redistimeseries/commands/#tsmrangetsmrevrange](https://oss.redislabs.com/redistimeseries/commands/#tsmrangetsmrevrange)

![TS.MRANGE](../../images/redis-datasource/commands/ts-mrange.png)

## Parameters

| Parameter                          | Description                                                                                                               |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| Key                                | Key name                                                                                                                  |
| Label Filter                       | [Filters](https://oss.redislabs.com/redistimeseries/commands/#filtering). A minimum of one **l=v** filter must be applied |
| Legend Label                       | Label for Frame's name. Will be displayed for two or more Time-series.                                                    |
| Value Label                        | Label for Serie's name. Will be displayed in the legend                                                                   |
| Aggregation                        | Aggregation type                                                                                                          |
| Time Bucket (Aggregation enabled)  | Time bucket for Aggregation in milliseconds                                                                               |
| Fill Missing (Aggregation enabled) | If checked, the data source will fill missing intervals                                                                   |

!!! note "Labels"

    If **Legend Label** is not provided, series will have all labels returned.

      Labels can be [Transformed](https://grafana.com/docs/grafana/latest/panels/transformations/) if required.

--8<-- "includes/redis-datasource/time-series-aggregation.md"

## Streaming

Streaming supported as **Time Series** and **Data frame**.

!!! important "Value Label"

    Provide the **Value Label** to merge streaming results.

## Visualization

Any standard visualization should work.
