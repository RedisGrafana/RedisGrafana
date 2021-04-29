```yaml
apiVersion: 1

datasources:
  - name: Redis Enterprise
    type: redis-enterprise-software-datasource
    access: proxy
    orgId: 1
    isDefault: true
    version: 1
    url: redis://cluster.remote:9443
    basicAuth: true
    basicAuthUser: re@localhost.io
    basicAuthPassword: 123
    jsonData:
      host: "https://cluster.remote:9443"
      tlsSkipVerify: true
    secureJsonFields:
      basicAuthPassword: true
    editable: true
```
