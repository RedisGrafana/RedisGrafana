---
hide: toc
---

# Collecting Grafana Plugins Statistics as RedisTimeSeries and visualizing time-series using Redis plug-ins for Grafana

This project collects plugins statistics from Grafana repository using [RedisTimeSeries](https://oss.redislabs.com/redistimeseries/).

!!! important "GitHub Repository"

    [https://github.com/RedisGrafana/grafana-plugin-stats](https://github.com/RedisGrafana/grafana-plugin-stats)

![How many times Redis Data Source for Grafana was downloaded?](../images/projects/redis-grafana-stats.png)

## Description

!!! quote "How to Use the New Redis Data Source for Grafana Plugin"

    Earlier this month, Redis Labs released the new Redis Data Source for Grafana plugin, which connects the widely used open source application monitoring tool to Redis. To give you an idea of how it all works, let’s take a look at a self-referential example: using the plugin to see how many times it has been downloaded over time. (The Grafana plugin repository itself does not provide such statistics out of the box.).

    Read more at [Redis Labs blog](https://redislabs.com/blog/how-to-use-the-new-redis-data-source-for-grafana-plug-in/).

![Stats](../images/projects/redis-datasource-stats.png)

## Dashboard

A new dashboard for Grafana v8 with Time Series panels was recently added to the project:

![Time Series](../images/projects/redis-plugins.png)
