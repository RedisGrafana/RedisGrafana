# TMSCAN

Returns keys with types and memory usage.

!!! warning "Latency"

    Please use this command in OFF-PEAK as it cause latency increase.

!!! note "Custom Command"

    This command was introduced for [Redis Latency panel](../../redis-app/redis-latency-panel.md) and is not a part of Redis server.

This custom command is based on [SCAN](https://redis.io/commands/scan) and [MEMORY USAGE](https://redis.io/commands/memory-usage) commands.
