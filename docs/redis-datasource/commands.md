# Redis Data Source supports

## Redis Commands (Hashes, Sets, Lists, Strings, Streams, etc.)

- CLIENT LIST - Returns information and statistics about the client connections server
- CLUSTER INFO - Provides INFO style information about Redis Cluster vital parameters
- CLUSTER NODES - Provides current cluster configuration, given by the set of known nodes
- GET - Returns the value of key
- HGET - Returns the value associated with field in the hash stored at key
- HGETALL - Returns all fields and values of the hash stored at key
- HKEYS - Returns all field names in the hash stored at key
- HLEN - Returns the number of fields contained in the hash stored at key
- HMGET - Returns the values associated with the specified fields in the hash stored at key
- [INFO](INFO.md) - Returns information and statistics about the server
- LLEN - Returns the length of the list stored at key
- TMSCAN (SCAN with Type and Memory Usage) - Returns keys with types and memory usage (CAUSE LATENCY)
- SCARD - Returns the set cardinality (number of elements) of the set stored at key
- SLOWLOG GET - Returns the Redis slow queries log
- SMEMBERS - Returns all the members of the set value stored at key
- TTL - Returns the string representation of the type of the value stored at key
- TYPE - Returns the string representation of the type of the value stored at key
- XINFO STREAM - Returns general information about the stream stored at the specified key
- XLEN - Returns the number of entries inside a stream
- XRANGE - Returns the stream entries matching a given range of IDs
- XREVRANGE - Returns the stream entries matching a given range of IDs in reverse order

## RedisTimeSeries (Time Series data structure)

- TS.GET - Returns the last sample
- TS.INFO - Returns information and statistics on the time-series
- TS.MRANGE - Query a timestamp range across multiple time-series by filters
- TS.QUERYINDEX - Query all the keys matching the filter list
- [TS.RANGE](TS-RANGE.md) - Query a range

## RedisGears (Dynamic framework for data processing)

- RG.DUMPREGISTRATIONS - Outputs the list of function registrations
- RG.PYSTATS - Returns memory usage statistics from the Python interpreter

## RedisGraph (Graph database)

- GRAPH.QUERY - Executes the given query against a specified graph
- GRAPH.SLOWLOG - Returns a list containing up to 10 of the slowest queries issued against the given graph ID

## RediSearch (Secondary Index & Query Engine)

- FT.INFO - Returns information and statistics on the index
