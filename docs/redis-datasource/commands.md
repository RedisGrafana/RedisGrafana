---
hide: toc
---

# Supported Commands

Redis Data Source supports core Redis, Custom and Redis Modules commands.

## Redis (Hashes, Sets, Lists, Strings, Streams, etc.)

| Command                                 | Description                                                                                                            |
| --------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| [CLIENT LIST](redis/CLIENT-LIST.md)     | Returns information and statistics about the client connections server                                                 |
| [CLUSTER INFO](redis/CLUSTER-INFO.md)   | Provides INFO style information about Redis Cluster vital parameters                                                   |
| [CLUSTER NODES](redis/CLUSTER-NODES.md) | Provides current cluster configuration, given by the set of known nodes                                                |
| [GET](redis/GET.md)                     | Returns the value of key                                                                                               |
| [HGET](redis/HGET.md)                   | Returns the value associated with field in the hash stored at key                                                      |
| [HGETALL](redis/HGETALL.md)             | Returns all fields and values of the hash stored at key                                                                |
| [HKEYS](redis/HKEYS.md)                 | Returns all field names in the hash stored at key                                                                      |
| [HLEN](redis/HLEN.md)                   | Returns the number of fields contained in the hash stored at key                                                       |
| [HMGET](redis/HMGET.md)                 | Returns the values associated with the specified fields in the hash stored at key                                      |
| [INFO](redis/INFO.md)                   | Returns information and statistics about the server                                                                    |
| [LLEN](redis/LLEN.md)                   | Returns the length of the list stored at key                                                                           |
| [SCARD](redis/SCARD.md)                 | Returns the set cardinality (number of elements) of the set stored at key                                              |
| [SLOWLOG](redis/SLOWLOG.md)             | Returns the Redis slow queries log                                                                                     |
| [SMEMBERS](redis/SMEMBERS.md)           | Returns all the members of the set value stored at key                                                                 |
| [TTL](redis/TTL.md)                     | Returns the remaining time to live of a key that has a timeout                                                         |
| [TYPE](redis/TYPE.md)                   | Returns the string representation of the type of the value stored at key                                               |
| [XINFO](redis/XINFO.md)                 | Introspection command used in order to retrieve different information about the streams and associated consumer groups |
| [XLEN](redis/XLEN.md)                   | Returns the number of entries inside a stream                                                                          |
| [XRANGE](redis/XRANGE.md)               | Returns the stream entries matching a given range of IDs                                                               |
| [XREVRANGE](redis/XREVRANGE.md)         | Returns the stream entries matching a given range of IDs in reverse order                                              |

## Custom

| Command                    | Description                              |
| -------------------------- | ---------------------------------------- |
| [TMSCAN](custom/TMSCAN.md) | Returns keys with types and memory usage |

## RedisTimeSeries

> [RedisTimeSeries](https://oss.redislabs.com/redistimeseries/) is a Redis Module adding a Time Series data structure to Redis.

| Command                                            | Description                                                    |
| -------------------------------------------------- | -------------------------------------------------------------- |
| [TS.GET](redis-timeseries/TS-GET.md)               | Returns the last sample                                        |
| [TS.INFO](redis-timeseries/TS-INFO.md)             | Returns information and statistics on the time-series          |
| [TS.MRANGE](redis-timeseries/TS-MRANGE.md)         | Query a timestamp range across multiple time-series by filters |
| [TS.QUERYINDEX](redis-timeseries/TS-QUERYINDEX.md) | Query all the keys matching the filter list                    |
| [TS.RANGE](redis-timeseries/TS-RANGE.md)           | Query a range                                                  |

## RedisGears

> [RedisGears](https://oss.redislabs.com/redisgears/) is a serverless engine for transaction, batch and event-driven data processing in Redis.

| Command                                                     | Description                                                 |
| ----------------------------------------------------------- | ----------------------------------------------------------- |
| [RG.DUMPREGISTRATIONS](redis-gears/RG-DUMPREGISTRATIONS.md) | Outputs the list of function registrations                  |
| [RG.PYDUMPREQS](redis-gears/RG-PYDUMPREQS.md)               | Returns a list of all the python requirements available     |
| [RG.PYEXECUTE](redis-gears/RG-PYEXECUTE.md)                 | Executes a Python function                                  |
| [RG.PYSTATS](redis-gears/RG-PYSTATS.md)                     | Returns memory usage statistics from the Python interpreter |

## RedisGraph

> [RedisGraph](https://oss.redislabs.com/redisgraph/) is the first queryable Property Graph database to use sparse matrices to represent the adjacency matrix in graphs and linear algebra to query the graph.

| Command                                       | Description                                                                                           |
| --------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| [GRAPH.EXPLAIN](redis-graph/GRAPH-EXPLAIN.md) | Constructs a query execution plan but does not run it                                                 |
| [GRAPH.PROFILE](redis-graph/GRAPH-PROFILE.md) | Executes a query and produces an execution plan augmented with metrics for each operation's execution |
| [GRAPH.QUERY](redis-graph/GRAPH-QUERY.md)     | Executes the given query against a specified graph                                                    |
| [GRAPH.SLOWLOG](redis-graph/GRAPH-SLOWLOG.md) | Returns a list containing up to 10 of the slowest queries issued against the given graph ID           |

## RediSearch

> [RediSearch](https://oss.redislabs.com/redisearch/) is a source available Secondary Index, Query Engine and Full-Text Search over Redis.

| Command                            | Description                                     |
| ---------------------------------- | ----------------------------------------------- |
| [FT.INFO](redis-search/FT-INFO.md) | Returns information and statistics on the index |
