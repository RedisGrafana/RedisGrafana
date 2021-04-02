# Variables

Template variables can query command and use other variables as parameters.

![Variables](../images/redis-datasource/variables.png)

## Supported Parameters

Variables will be replaced in the following parameters:

| Parameter | Description  | Command                                  |
| --------- | ------------ | ---------------------------------------- |
| Key       | Key name     | [GET](redis/GET.md), XRANGE, etc.        |
| Query     | CLI query    | Any                                      |
| Field     | Hash Field   | HGET, HMGET                              |
| Filter    | Filter       | TS.MRANGE, TS.QUERYINDEX                 |
| Legend    | Frame's name | [TS.RANGE](redis-timeseries/TS-RANGE.md) |
| Value     | Serie's name | [TS.RANGE](redis-timeseries/TS-RANGE.md) |

## Examples

### How to use SUNION for multi-select variable?

=== "LUA"

    The LUA script should work fine on a single shard deployment:

    ```bash
    eval "return redis.call('sunion',${region:singlequote})" 0
    ```

=== "Redis Gears"

    Another option is to utilize [RedisGears](https://redisgears.io) module:

    --8<-- "includes/redis-datasource/gears-sunion.md"

    To execute the trigger in Grafana:

    ```bash
    RG.TRIGGER SUNION ${region:csv}
    ```

![SUNION Example](../images/redis-datasource/variables-example.png)
