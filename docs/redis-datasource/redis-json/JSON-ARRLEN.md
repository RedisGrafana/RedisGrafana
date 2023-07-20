---
hide: toc
---

# JSON.ARRLEN

This command returns the length of the JSON Array at path in key.

!!! info "RedisJSON"

    [https://redis.io/commands/json.arrlen/](https://redis.io/commands/json.arrlen/)

![JSON.ARRLEN](../../images/redis-datasource/commands/json-arrlen.png)

## Parameters

| Parameter | Description                                                            |
| --------- | ---------------------------------------------------------------------- |
| Key       | Key name                                                               |
| Path      | Subset of common best practices and resembles JSONPath not by accident |

--8<-- "includes/redis-datasource/json-path.md"

--8<-- "includes/redis-datasource/streaming-any.md"

--8<-- "includes/redis-datasource/visualization-any.md"
