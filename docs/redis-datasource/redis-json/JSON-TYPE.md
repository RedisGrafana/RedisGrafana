---
hide: toc
---

# JSON.TYPE

This command returns the type of JSON value at path.

!!! info "RedisJSON"

    [https://oss.redis.com/redisjson/commands/#jsontype](https://oss.redis.com/redisjson/commands/#jsontype)

![JSON.TYPE](../../images/redis-datasource/commands/json-type.png)

## Parameters

| Parameter | Description                                                            |
| --------- | ---------------------------------------------------------------------- |
| Key       | Key name                                                               |
| Path      | Subset of common best practices and resembles JSONPath not by accident |

--8<-- "includes/redis-datasource/json-path.md"

--8<-- "includes/redis-datasource/streaming-any.md"

--8<-- "includes/redis-datasource/visualization-any.md"
