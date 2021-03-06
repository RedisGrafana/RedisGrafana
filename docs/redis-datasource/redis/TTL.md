---
hide: toc
---

# TTL

This command returns the remaining time to live of a key that has a timeout.

!!! info "Redis Core"

    [https://redis.io/commands/TTL](https://redis.io/commands/TTL)

![TTL](../../images/redis-datasource/commands/ttl.png)

## Parameters

| Parameter | Description |
| --------- | ----------- |
| Key       | Key name    |

--8<-- "includes/redis-datasource/streaming-any.md"

--8<-- "includes/redis-datasource/visualization-any.md"

!!! example "The Clock is Ticking"

    TTL can be used to display countdown until the event.

    ![Countdown](../../images/showcase/ttl.png)
