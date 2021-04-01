# TMSCAN

Returns keys with types and memory usage.

!!! info "Custom Command"

    This command was introduced for [Redis Latency panel](../../redis-app/redis-latency-panel.md) and is not a part of Redis server.

!!! warning "Latency"

    Please use this command in OFF-PEAK as it cause latency increase.

This custom command is based on [SCAN](https://redis.io/commands/scan) and [MEMORY USAGE](https://redis.io/commands/memory-usage) commands.

> SCAN is a cursor based iterator. This means that at every call of the command, the server returns an updated cursor that the user needs to use as the cursor argument in the next call.

Found results and Cursor returns in separate frames.

## Parameters

| Parameter     | Description                                                                                                             |
| ------------- | ----------------------------------------------------------------------------------------------------------------------- |
| Size          | Calculate top keys in the results                                                                                       |
| Cursor        | Iterator for SCAN command                                                                                               |
| Match pattern | Patter for SCAN command                                                                                                 |
| Count         | The amount of work that should be done at every call in order to retrieve elements from the collection for SCAN command |
| Samples       | Number of sampled nested values                                                                                         |

## Streaming

Streaming is not supported.

## Visualization

- Table
