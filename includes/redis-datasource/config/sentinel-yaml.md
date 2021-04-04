```yaml
apiVersion: 1

datasources:
  - name: Sentinel
    type: redis-datasource
    access: proxy
    orgId: 1
    isDefault: true
    version: 1
    url: redis://host.docker.internal:6379
    jsonData:
      client: sentinel
      sentinelName: Test
      poolSize: 5
      timeout: 10
      pingInterval: 0
      pipelineWindow: 0
    editable: true
```
