---
layout: post
title: "macOS下nginx操作"
date: 2026-03-24 00:00:00 +0800
categories: [Macos]
tags: [macos]
---

适用于M1系统

配置文件位于以下路径
```bash
vim /opt/homebrew/etc/nginx/nginx.conf
```

重启nginx服务
```bash
brew services restart nginx
```

查看错误日志

```bash
tail -f /opt/homebrew/var/log/nginx/error.log
```
