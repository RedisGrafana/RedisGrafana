---
hide: toc
---

# Configuration

You can add as many data sources as you want to support multiple Redis Enterprise clusters.

![Data Source](../../images/redis-explorer/re-software/config-editor.png)

## Cluster URL

Specify `host:port` address to Redis Enterprise software REST API interface. Port 9443 is [recommended](https://docs.redislabs.com/latest/rs/administering/designing-production/networking/port-configurations/) to use for REST API traffic.

## User

Username to authenticate. Ability to see metrics, configuration and logs depends on the [role](https://docs.redislabs.com/latest/rs/security/admin-console-security/user-security/).

## Password

!!! important "Security"

    Passwords are kept in the Grafana security database and not accessible to users.

Password for the provided **User**.

## Skip Verify

If checked, the server's certificate will not be checked for validity. Should be enabled for Self-Signed certificates.
