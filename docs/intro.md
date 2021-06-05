---
hide: toc
---

# Introduction

The Redis plugins for Grafana allow users to connect to the Redis databases and build dashboards in Grafana to observe and interact with Redis and Application data.

!!! important "Requirements"

    Only **Grafana 7.1+** with a new Backend plugin platform supports Redis plugins.

<img class="sandwich" title="Plugins" src="/images/redis-table.png">

## Where Next?

- The [Quickstart](quickstart.md) is the recommended starting point.
- The [Learn more](learn-more.md) page consists of links to the recent blog posts and video presentations.
- The [Commands](redis-datasource/commands.md) reference all supported commands in the Redis Data Source.
- The [Redis Application plugin](redis-app/overview.md) page provides information about the Application pages, dashboards, and custom panels.
- The [Redis Explorer plugin](redis-explorer/overview.md) page offers information about the Explorer pages, dashboards, and Redis Enterprise Software data source.
- The [Timeline](timeline.md) page lists all significant dates and plans in the plugin's development.
- The **Development** section has more details on the developing plugins and nightly build docker images.

## Grafana Repository

Plugins are registered in the [Grafana repository](https://grafana.com/grafana/plugins/) and available to [Grafana](https://grafana.com/), [Grafana Enterprise](https://grafana.com/products/enterprise/), and [Grafana Cloud](https://grafana.com/products/cloud/).

| Plugin                                                                           | Description                                                            | Repository                                                                          |
| -------------------------------------------------------------------------------- | ---------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| [Redis Data Source](https://grafana.com/grafana/plugins/redis-datasource/)       | Allows connecting to any Redis database On-Premises or in the Cloud    | [grafana-redis-datasoure](https://github.com/RedisGrafana/grafana-redis-datasource) |
| [Redis Application plugin](https://grafana.com/grafana/plugins/redis-app/)       | Provides Application pages and custom panels for Redis Data Source     | [grafana-redis-app](https://github.com/RedisGrafana/grafana-redis-app)              |
| [Redis Explorer plugin](https://grafana.com/grafana/plugins/redis-explorer-app/) | Allows connecting to Redis Enterprise software clusters using REST API | [grafana-redis-explorer](https://github.com/RedisGrafana/grafana-redis-explorer)    |

## Projects

Projects demonstrate compelling use cases that help you start using plugins.

| Projects                                          | Description                                                                                     |
| ------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| [Plugins Statistics](projects/grafana-stats.md)   | Collecting Grafana Plugins Statistics as RedisTimeSeries and visualizing time-series in Grafana |
| [Pop-up Store](projects/pop-up-store.md)          | Pop-up store demo using RedisTimeSeries, RedisGears and Redis Data Source                       |
| [Forecasting Stocks](projects/finance-prophet.md) | Forecasting Stocks and Crypto prices using Redis, Prophet and Grafana                           |
| [Camera feed with AI](projects/camera-ai.md)      | Analyzing camera feed using RedisAI, OpenCV and Grafana                                         |

## Contact Us

!!! tip "Contribute"

    To contribute your project or propose Documentation updates, open an [issue](https://github.com/RedisGrafana/redisgrafana/issues/new/choose).

If you have questions, feedback, or want to report an issue, here's where you can get in touch:

- [Redis Data Source](https://github.com/RedisGrafana/grafana-redis-datasource/issues/new/choose)
- [Redis Application plugin](https://github.com/RedisGrafana/grafana-redis-app/issues/new/choose)
- [Redis Explorer plugin](https://github.com/RedisGrafana/grafana-redis-explorer/issues/new/choose)
