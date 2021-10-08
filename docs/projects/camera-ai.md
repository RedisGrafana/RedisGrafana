---
hide: toc
---

# Analyzing camera feed using RedisAI, OpenCV, and Redis plugins for Grafana

This project demonstrates how to analyze camera feed stored as [Redis Streams](https://redis.io/topics/streams-intro) using serverless engine [RedisGears](https://oss.redis.com/redisgears/), [RedisAI](https://redisai.io/) and display analyzed frames with metrics in Grafana.

!!! important "GitHub Repository"

    [https://github.com/RedisGrafana/redis-camera-ai](https://github.com/RedisGrafana/redis-camera-ai)

![Camera AI](../images/projects/redis-camera-ai.png)

## Description

!!! quote "Analyzing camera feed using RedisAI, OpenCV, and Redis plugins for Grafana"

    Two years ago, Redis published an article "My Other Stack Is RedisEdge" introducing real-time video analysis in Redis. Since then, we introduced Redis plugins for Grafana to visualize RedisTimeSeries directly without adapters for Prometheus. Also, a recently developed Image panel can display analyzed with AI encoded image on the dashboard, eliminating the Video server.

    Read more at [Volkov Labs blog](https://volkovlabs.com/analyzing-camera-feed-in-real-time-using-redisai-opencv-python-and-redis-plugins-for-grafana-1c23ef0a042c).

![Camera AI](../images/projects/batman-ai.gif)

## Dashboard

Camera dashboard with image panel and two most important metrics: Frames Queue and recognized people in the frame.

![Camera AI](../images/projects/camera-ai-batman.jpg)

Camera processing dashboard with panels vizualizing Frames Queue, Processing Queue, Profile and allows to monitor and update RegisGears script on monitoring workstation.

![Camera AI](../images/projects/camera-ai.png)
