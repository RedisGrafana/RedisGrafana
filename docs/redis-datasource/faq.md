---
hide: toc
---

# FAQ

## Plugin health check failed

--8<-- "includes/redis-datasource/permissions.md"

## The developer cannot be verified on MacOS

If `Redis_datasource_darwin_amd64` cannot be opened because the developer cannot be verified on MacOS:

- Go to `System Preferences` > `Security & Privacy`
- Set to allow `redis-datasource_darwin_amd64`.

## Cluster Mode

All Redis Cluster nodes should be available from the Grafana instance when Data Source is set to the `Cluster` type in the [Configuration](../configuration).

![CLUSTER-INFO](../../images/showcase/redis-cluster.png)
