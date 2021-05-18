---
hide: toc
---

# GRAPH.PROFILE

This command executes a query and produces an execution plan augmented with metrics for each operation's execution.

!!! info "RedisGraph"

    [https://oss.redislabs.com/redisgraph/commands/#graphprofile](https://oss.redislabs.com/redisgraph/commands/#graphprofile)

--8<-- "includes/ds-timeout.md"

![GRAPH.QUERY](../../images/redis-datasource/commands/graph-profile.png)

## Parameters

| Parameter | Description                                                                                                                                           |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| Key       | RedisGraph key                                                                                                                                        |
| Cypher    | The [syntax is based on Cypher](https://oss.redislabs.com/redisgraph/commands/#query-language), and only a subset of the language currently supported |

## Streaming

Streaming supported as **Data frame**.

## Visualization

- Table
