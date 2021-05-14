```yaml
apiVersion: 1

datasources:
  - name: Sentinel
    type: redis-datasource
    access: proxy
    orgId: 1
    isDefault: true
    version: 1
    url: redis://cluster.remote:8001
    jsonData:
      client: sentinel
      sentinelName: Test@internal
      poolSize: 5
      timeout: 10
      pingInterval: 0
      pipelineWindow: 0
    editable: true
```
