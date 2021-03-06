---
hide: toc
---

# GRAPH.QUERY

This command executes the given query against a specified graph.

!!! info "RedisGraph"

    [https://oss.redis.com/redisgraph/commands/#graphquery](https://oss.redis.com/redisgraph/commands/#graphquery)

--8<-- "includes/ds-timeout.md"

![GRAPH.QUERY](../../images/redis-datasource/commands/graph-query.png)

## Parameters

| Parameter | Description                                                                                                                                       |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| Key       | RedisGraph key                                                                                                                                    |
| Cypher    | The [syntax is based on Cypher](https://oss.redis.com/redisgraph/commands/#query-language), and only a subset of the language currently supported |

## Data Frames

| Name     | Description                                                                                                                      |
| -------- | -------------------------------------------------------------------------------------------------------------------------------- |
| nodes    | Nodes in the [Node Graph panel](https://grafana.com/docs/grafana/latest/panels/visualizations/node-graph/)'s format, if returned |
| edges    | Edges in the [Node Graph panel](https://grafana.com/docs/grafana/latest/panels/visualizations/node-graph/)'s format, if returned |
| data     | Formatted data returned by the query                                                                                             |
| metadata | Metadata related to the query execution                                                                                          |

![GRAPH.QUERY data](../../images/redis-datasource/commands/graph-query-data.png)

## Streaming

Streaming is not supported.

## Visualization

- Node Graph ([Grafana 7.4+](https://grafana.com/docs/grafana/latest/whatsnew/whats-new-in-v7-4/))
