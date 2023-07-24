---
hide: toc
---

# JSON.GET

This command returns the value at path in JSON serialized form.

!!! info "RedisJSON"

    [https://redis.io/commands/json.get/](https://redis.io/commands/json.get/)

![JSON.GET](../../images/redis-datasource/commands/json-get.png)

## Parameters

| Parameter | Description                                                            |
| --------- | ---------------------------------------------------------------------- |
| Key       | Key name                                                               |
| Path      | Subset of common best practices and resembles JSONPath not by accident |

--8<-- "includes/redis-datasource/json-path.md"

## Streaming

Streaming supported as **Data frame**.

--8<-- "includes/redis-datasource/visualization-any.md"
