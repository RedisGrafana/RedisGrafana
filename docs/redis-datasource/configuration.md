# Redis Data Source configuration

Data Source can connect to any Redis database On-Premises or in the Cloud. You can add as many data sources as you want to support multiple Redis databases.

![Datasource](../images/redis-datasource/config-editor.png)

Redis accepts clients connections on the configured [listening TCP port](#standalone) and the [Unix socket](#unix-socket) if enabled. [Cluster](#cluster) is a distributed implementation of OSS Redis and [Sentinel](#sentinel) provides high availability.

!!! tip "Redis Application plug-in"

    Redis Application plug-in helps to manage multiple [Redis Data Sources](../redis-app/datasources.md) and provides [Custom panels](../redis-app/panels.md).

## Main configuration

### Address

Specify `host:port` address or a URI to connect to Redis. Please use `/db-number` or `?db=db-number` to specify the logical database number as defined in the [Schema](https://www.iana.org/assignments/uri-schemes/prov/redis):

```bash
redis://redis-server:6379/0
```

#### Cluster

In Cluster mode **Address** can contain multiple values (`host:port` address or a URI) with comma.

#### Sentinel

In Sentinel mode **Address** can contain multiple values (`host:port` address or a URI) with comma. **Master Name** is required to connect to Sentinel.

![Sentinel configuration](../images/redis-datasource/sentinel.png)

#### Unix socket

In Unix socket mode **Address** should contain path to the socket file.

### ACL

Available since [Redis 6.0](https://redis.io/topics/acl) and allows to specify **Username** to authenticate.

![ACL enabled](../images/redis-datasource/acl.png)

### Password

!!! important "Security"

    Passwords are kept in the Grafana security database and not accessible to users.

When specified AUTH command will be used to authenticate with the provided password.

### Pool Size

Data source will keep open at least the given number of connections to the Redis instance at the provided **Address**. The recommended size of the pool is 5 and can be increased if dashboards have a lot of panels and multiple users.

## Advanced configuration

### Timeout

Sets the duration in seconds for connect, read and write timeouts. Default value is 10 seconds.

### Ping Interval

Specifies the interval in seconds at which a ping event happens. A shorter interval means connections are pinged more frequently, but also means more traffic with the server. If interval is zero then ping will be disabled. Default value is 0.

### Pipeline Window

Sets the duration in microseconds after which internal pipelines will be flushed. If window is zero then implicit pipelining will be disabled. Default value is 0.

## SSL/TLS

To support SSL/TLS authentication enable it and provide all required parameters.

![TLS enabled](../images/redis-datasource/tls.png)

### Skip Verify

If checked, the server's certificate will not be checked for validity. Should be enabled for Self-Signed certificates.

### Client Certificate and Key

!!! important "Security"

    Client certificates and keys are kept in the Grafana security database and not accessible to users.

Client Certificate and Key should be provided when client authentication is enforced.

### Certification Authority

Provide certificate to validate server's certificate or enable **Skip Verify**.

## Known issues

### Plugin health check failed

Redis Data Source binaries should have executable permissions for Grafana to be able to execute it. Check out [Quickstart](../quickstart.md#install-without-internet-access) page for more information.

### `Redis_datasource_darwin_amd64` cannot be opened because the developer cannot be verified

Go to `System Preferences` > `Security & Privacy` and set to allow `redis-datasource_darwin_amd64`.
