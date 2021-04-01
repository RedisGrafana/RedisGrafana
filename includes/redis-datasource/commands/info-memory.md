```json
{
  "__inputs": [
    {
      "name": "DS_REDIS",
      "label": "Redis",
      "description": "",
      "type": "datasource",
      "pluginId": "redis-datasource",
      "pluginName": "Redis"
    }
  ],
  "__requires": [
    {
      "type": "panel",
      "id": "bargauge",
      "name": "Bar gauge",
      "version": ""
    },
    {
      "type": "grafana",
      "id": "grafana",
      "name": "Grafana",
      "version": "7.5.1"
    },
    {
      "type": "datasource",
      "id": "redis-datasource",
      "name": "Redis",
      "version": "1.3.1"
    }
  ],
  "annotations": {
    "list": [
      {
        "builtIn": 1,
        "datasource": "-- Grafana --",
        "enable": true,
        "hide": true,
        "iconColor": "rgba(0, 211, 255, 1)",
        "name": "Annotations & Alerts",
        "type": "dashboard"
      }
    ]
  },
  "editable": true,
  "gnetId": null,
  "graphTooltip": 0,
  "id": null,
  "links": [],
  "panels": [
    {
      "datasource": "${DS_REDIS}",
      "fieldConfig": {
        "defaults": {
          "mappings": [],
          "min": 0,
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "dark-green",
                "value": null
              }
            ]
          },
          "unit": "decbytes"
        },
        "overrides": [
          {
            "matcher": {
              "id": "byName",
              "options": "Used Memory"
            },
            "properties": [
              {
                "id": "decimals",
                "value": 2
              }
            ]
          },
          {
            "matcher": {
              "id": "byName",
              "options": "Used Memory, Peak"
            },
            "properties": [
              {
                "id": "decimals",
                "value": 2
              }
            ]
          },
          {
            "matcher": {
              "id": "byName",
              "options": "Used Memory, LUA"
            },
            "properties": [
              {
                "id": "decimals",
                "value": 2
              }
            ]
          },
          {
            "matcher": {
              "id": "byName",
              "options": "Memory Limit"
            },
            "properties": [
              {
                "id": "decimals",
                "value": 2
              }
            ]
          },
          {
            "matcher": {
              "id": "byName",
              "options": "Total System Memory"
            },
            "properties": [
              {
                "id": "decimals",
                "value": 2
              }
            ]
          }
        ]
      },
      "gridPos": {
        "h": 13,
        "w": 14,
        "x": 0,
        "y": 0
      },
      "id": 2,
      "options": {
        "displayMode": "lcd",
        "orientation": "horizontal",
        "reduceOptions": {
          "calcs": ["mean"],
          "fields": "/.*/",
          "values": true
        },
        "showUnfilled": true,
        "text": {}
      },
      "pluginVersion": "7.5.1",
      "scopedVars": {
        "redis": {
          "selected": true,
          "text": "Redis",
          "value": "Redis"
        }
      },
      "targets": [
        {
          "command": "info",
          "query": "",
          "refId": "A",
          "section": "memory",
          "streaming": true,
          "streamingDataType": "DataFrame",
          "type": "command"
        }
      ],
      "timeFrom": null,
      "timeShift": null,
      "title": "Memory",
      "transformations": [
        {
          "id": "filterFieldsByName",
          "options": {
            "include": {
              "names": [
                "used_memory",
                "used_memory_peak",
                "total_system_memory",
                "maxmemory",
                "used_memory_lua"
              ]
            }
          }
        },
        {
          "id": "organize",
          "options": {
            "excludeByName": {},
            "indexByName": {
              "maxmemory": 3,
              "total_system_memory": 4,
              "used_memory": 0,
              "used_memory_lua": 2,
              "used_memory_peak": 1
            },
            "renameByName": {
              "maxmemory": "Memory Limit",
              "total_system_memory": "Total System Memory",
              "used_memory": "Used Memory",
              "used_memory_lua": "Used Memory, LUA",
              "used_memory_peak": "Used Memory, Peak"
            }
          }
        }
      ],
      "type": "bargauge"
    }
  ],
  "schemaVersion": 27,
  "style": "dark",
  "tags": [],
  "templating": {
    "list": []
  },
  "time": {
    "from": "now-5m",
    "to": "now"
  },
  "timepicker": {},
  "timezone": "",
  "title": "Info Memory",
  "uid": "cPXyod_Gk",
  "version": 1
}
```
