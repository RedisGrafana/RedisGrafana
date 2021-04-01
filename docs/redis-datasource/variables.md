# Variables

Template variables can query command and use other variables as parameters.

![Variables](../images/redis-datasource/variables.png)

## How to use SUNION for multi-select variable?

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
