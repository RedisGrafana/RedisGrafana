---
hide: toc
---

# XREVRANGE

This command returns the stream entries matching a given range of IDs in reverse order.

!!! info "Redis Core"

    [https://redis.io/commands/XREVRANGE](https://redis.io/commands/XREVRANGE)

![XREVRANGE](../../images/redis-datasource/commands/xrevrange.png)

!!! note "$time"

    Column **$time** was added in Redis Data Source 1.4.0 based on the $streamId.

## Parameters

| Parameter | Description       | Default     |
| --------- | ----------------- | ----------- |
| Key       | Key name          |             |
| End       | Range end         | + (maximum) |
| Start     | Range start       | - (minimum) |
| Count     | Number of entries |             |

## Streaming

Streaming supported as **Data frame**.

!!! important "Time series"

    Streaming as Time series will return only the last line.

--8<-- "includes/redis-datasource/visualization-any.md"
