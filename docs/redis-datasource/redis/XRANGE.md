---
hide: toc
---

# XRANGE

This command returns the stream entries matching a given range of IDs.

!!! info "Redis Core"

    [https://redis.io/commands/XRANGE](https://redis.io/commands/XRANGE)

![XRANGE](../../images/redis-datasource/commands/xrange.png)

!!! note "$time"

    Column **$time** was added in Redis Data Source 1.4.0 based on the $streamId.

!!! important "Since 2.0.0"

    XRANGE command based on the selected time range if Start/End is not specified. Use '-' as Start and '+' as end to display all results.

## Parameters

| Parameter | Description       | Default    |
| --------- | ----------------- | ---------- |
| Key       | Key name          |            |
| Start     | Range start       | time range |
| End       | Range end         | time range |
| Count     | Number of entries |            |

## Streaming

Streaming supported as **Data frame**.

!!! important "Time series"

    Streaming as Time series will return only the last line.

--8<-- "includes/redis-datasource/visualization-any.md"
