---
hide: toc
---

# INFO

This command returns information and statistics about the server.

!!! info "Redis Core"

    [https://redis.io/commands/INFO](https://redis.io/commands/INFO)

![INFO](../../images/redis-datasource/commands/info-ops-sec.png)

## Parameters

| Parameter | Description            |
| --------- | ---------------------- |
| Section   | Section of information |

## Sections

| Section                  | Description                                | Streaming                   | Visualization                                                               |
| ------------------------ | ------------------------------------------ | --------------------------- | --------------------------------------------------------------------------- |
| Server                   | General information about the Redis server | Yes                         | Any                                                                         |
| Clients                  | Client connections                         | Yes                         | Any                                                                         |
| Memory                   | Memory consumption related information     | Yes                         | Any                                                                         |
| Persistence              | RDB and AOF related information            | Yes                         | Any                                                                         |
| Stats                    | General statistics                         | Yes                         | Any, [Command Latency](../../redis-app/panels/redis-latency-panel.md) panel |
| Replication              | Master/replica replication information     | Yes                         | Any                                                                         |
| CPU                      | CPU consumption statistics                 | Yes                         | Any                                                                         |
| Command Stats            | Redis command statistics                   | Number of calls per command | Any                                                                         |
| Cluster                  | Redis Cluster                              | Yes                         | Any                                                                         |
| Modules (not supported)  | Modules                                    | -                           | -                                                                           |
| Keyspace (not supported) | Database related statistics                | -                           | -                                                                           |
| Error Stats              | Redis error statistics (Redis 6.2)         | Yes                         | Any                                                                         |

!!! note "Command Latency"

    To see Latency per command based on **Command Stats**, take a look at [Command Latency](../../redis-app/panels/redis-latency-panel.md) panel.

### Memory

![INFO](../../images/redis-datasource/commands/info-memory.png)

## Streaming

Streaming supported as **Time Series** and **Data frame** for the most sections. Check **Streaming** column for specific section.

## Visualization

Any standard visualization should work. Check **Visualization** column for specific section.

## Dashboards

- [Redis CLI](../../../redis-app/dashboards/#cli-command-line-interface) includes Graph, [Command Latency](../../redis-app/panels/redis-latency-panel.md) panels using this command.
- [Redis Overview](../../../redis-app/dashboards/#redis-overview) includes Stats, Bar gauge, Table panels using this command.
