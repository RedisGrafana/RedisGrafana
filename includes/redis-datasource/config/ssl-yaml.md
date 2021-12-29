```yaml
apiVersion: 1

datasources:
  - name: Redis
    type: redis-datasource
    access: proxy
    orgId: 1
    version: 1
    url: redis://redis.default.svc.cluster.local:6379
    editable: true
    jsonData:
      client: standalone
      tlsAuth: true
      tlsSkipVerify: true
    secureJsonData:
      password: $PASSWORD
      tlsCACert: "-----BEGIN CERTIFICATE-----"
      tlsClientCert: "-----BEGIN CERTIFICATE-----"
      tlsClientKey: "-----BEGIN RSA PRIVATE KEY-----"
```
