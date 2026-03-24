---
layout: post
title: "docker本地MySQL启动语句"
date: 2026-03-24 00:00:00 +0800
categories: [Docker]
tags: [docker, container]
---

```bash
docker run -p 3306:3306 --name mysql -e MYSQL_ROOT_PASSWORD=root -d mysql:latest
```
