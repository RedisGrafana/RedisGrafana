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
      "type": "grafana",
      "id": "grafana",
      "name": "Grafana",
      "version": "7.5.2"
    },
    {
      "type": "datasource",
      "id": "redis-datasource",
      "name": "Redis",
      "version": "1.4.0"
    },
    {
      "type": "panel",
      "id": "table",
      "name": "Table",
      "version": ""
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
          "custom": {
            "align": null,
            "filterable": false
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              }
            ]
          }
        },
        "overrides": [
          {
            "matcher": {
              "id": "byName",
              "options": "id"
            },
            "properties": [
              {
                "id": "custom.width",
                "value": 176
              }
            ]
          },
          {
            "matcher": {
              "id": "byName",
              "options": "PD"
            },
            "properties": [
              {
                "id": "custom.width",
                "value": 242
              }
            ]
          },
          {
            "matcher": {
              "id": "byName",
              "options": "Triggered"
            },
            "properties": [
              {
                "id": "custom.width",
                "value": 90
              }
            ]
          },
          {
            "matcher": {
              "id": "byName",
              "options": "Mode"
            },
            "properties": [
              {
                "id": "custom.width",
                "value": 92
              }
            ]
          },
          {
            "matcher": {
              "id": "byName",
              "options": "Success"
            },
            "properties": [
              {
                "id": "custom.width",
                "value": 88
              }
            ]
          },
          {
            "matcher": {
              "id": "byName",
              "options": "Failures"
            },
            "properties": [
              {
                "id": "custom.width",
                "value": 84
              }
            ]
          },
          {
            "matcher": {
              "id": "byName",
              "options": "Aborted"
            },
            "properties": [
              {
                "id": "custom.width",
                "value": 89
              }
            ]
          },
          {
            "matcher": {
              "id": "byName",
              "options": "Status"
            },
            "properties": [
              {
                "id": "custom.width",
                "value": 94
              }
            ]
          },
          {
            "matcher": {
              "id": "byName",
              "options": "Reader"
            },
            "properties": [
              {
                "id": "custom.width",
                "value": 154
              }
            ]
          },
          {
            "matcher": {
              "id": "byName",
              "options": "Args"
            },
            "properties": [
              {
                "id": "custom.width",
                "value": 147
              }
            ]
          }
        ]
      },
      "gridPos": {
        "h": 9,
        "w": 14,
        "x": 0,
        "y": 0
      },
      "id": 2,
      "options": {
        "showHeader": true,
        "sortBy": []
      },
      "pluginVersion": "7.5.2",
      "targets": [
        {
          "command": "rg.dumpregistrations",
          "query": "",
          "refId": "A",
          "streaming": true,
          "streamingDataType": "DataFrame",
          "type": "gears"
        }
      ],
      "timeFrom": null,
      "timeShift": null,
      "title": "Registrations",
      "transformations": [
        {
          "id": "organize",
          "options": {
            "excludeByName": {
              "PD": true,
              "desc": true,
              "id": true
            },
            "indexByName": {
              "PD": 4,
              "args": 1,
              "desc": 3,
              "id": 2,
              "lastError": 10,
              "mode": 5,
              "numAborted": 9,
              "numFailures": 8,
              "numSuccess": 7,
              "numTriggered": 6,
              "reader": 0,
              "status": 11
            },
            "renameByName": {
              "args": "Args",
              "lastError": "Last Error",
              "mode": "Mode",
              "numAborted": "Aborted",
              "numFailures": "Failures",
              "numSuccess": "Success",
              "numTriggered": "Triggered",
              "reader": "Reader",
              "status": "Status"
            }
          }
        }
      ],
      "type": "table"
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
  "title": "RedisGears Registations",
  "uid": "VFOV_vlMz",
  "version": 1
}
```
