```yaml
version: "3.4"

services:
  redis:
    container_name: redis
    image: ghcr.io/redisgrafana/redis-opencv:latest
    ports:
      - 6379:6379

  grafana:
    container_name: grafana
    image: ghcr.io/redisgrafana/redis-app:latest
    ports:
      - "3000:3000"
    environment:
      - GF_AUTH_ANONYMOUS_ORG_ROLE=Admin
      - GF_AUTH_ANONYMOUS_ENABLED=true
      - GF_AUTH_BASIC_ENABLED=false
      - GF_ENABLE_GZIP=true
      - GF_USERS_DEFAULT_THEME=light
    volumes:
      - ./provisioning:/etc/grafana/provisioning
      - ./dashboards:/var/lib/grafana/dashboards
```
