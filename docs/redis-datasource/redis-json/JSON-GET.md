---
hide: toc
---

# JSON.GET

This command returns the value at path in JSON serialized form.

!!! info "RedisJSON"

    [https://oss.redis.com/redisjson/commands/#jsonget](https://oss.redis.com/redisjson/commands/#jsonget)

![TS.GET](../../images/redis-datasource/commands/json-get.png)

## Parameters

| Parameter | Description                                                            |
| --------- | ---------------------------------------------------------------------- |
| Key       | Key name                                                               |
| Path      | Subset of common best practices and resembles JSONPath not by accident |

!!! note "JSONPath"

    RedisJSON decides which syntax to use depending on the first character of the path query. If the query starts with the character $ it is considered as a JSONPath query. Otherwise it is interpreted as a legacy path syntax.

    [Learn more in the documentation](https://oss.redis.com/redisjson/path/).

## Streaming

Streaming supported as **Data frame**.

--8<-- "includes/redis-datasource/visualization-any.md"
