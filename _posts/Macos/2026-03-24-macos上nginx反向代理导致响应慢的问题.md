---
layout: post
title: "macos上nginx反向代理导致响应慢的问题"
date: 2026-03-24 00:00:00 +0800
categories: [Macos]
tags: [macos]
---

尝试在本地修改/etc/hosts，将huable.local指向127.0.0.1

通过mkcert生成本地证书并信任

通过nginx反向代理到本地的127.0.0.1地址（不是localhost）

之后通过curl访问https://huable.local/xxx地址，响应很慢超过5秒以上
但是直接访问127.0.0.1/xxx响应就非常快

经过搜索和尝试发现，需要在/etc/hosts中将huable.local的ipv6地址也加上
即同时配置ipv4和ipv6
127.0.0.1 huable.local
::1 huable.local

可能是因为在域名解析时会尝试对huable.local进行dns解析，看是否存在ipv6地址
如果不存在则退回到ipv4地址，这样增加了响应时间
