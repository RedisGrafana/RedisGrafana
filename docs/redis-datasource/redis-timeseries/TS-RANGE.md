# TS.RANGE

Query a range in forward direction.

!!! info "RedisTimeSeries"

    [https://oss.redislabs.com/redistimeseries/commands/#tsrangetsrevrange](https://oss.redislabs.com/redistimeseries/commands/#tsrangetsrevrange)

![TS.RANGE](../../images/redis-datasource/commands/ts-range.png)

## Parameters

| Parameter                          | Description                                             |
| ---------------------------------- | ------------------------------------------------------- |
| Key                                | Key name                                                |
| Legend                             | Frame's name, will be display for 2 or more Queries     |
| Value                              | Serie's name, will be display in legend                 |
| Aggregation                        | Aggregation type                                        |
| Time Bucket (Aggregation enabled)  | Time bucket for Aggregation in milliseconds             |
| Fill Missing (Aggregation enabled) | If checked, the data source will fill missing intervals |

### Aggregation

| Type           | Description                                    |
| -------------- | ---------------------------------------------- |
| None (default) | No aggregation                                 |
| Avg            | Average                                        |
| Count          | Count number of samples                        |
| Max            | Maximum                                        |
| Min            | Minimum                                        |
| Range          | Diff between maximum and minimum in the bucket |
| Sum            | Summation                                      |

## Streaming

Streaming is supported as **Time Series** and **Data frame**.

!!! important "Value"

    Value should be set to merge streaming results.

## Visualization

Any standard visualization should work.
