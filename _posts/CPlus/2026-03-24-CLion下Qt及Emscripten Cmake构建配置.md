---
layout: post
title: "CLion下Qt及Emscripten Cmake构建配置"
date: 2026-03-24 00:00:00 +0800
categories: [CPlus]
tags: [cpp, cmake]
---

演示qt webassembly用法

需要加载自定义字体解决Web下面中文显示问题。目前中文可以显示，但是对输入法支持有问题。

# Webassembly功能测试

## CLion下测试

```bash
# 配置了以下cmake参数
-DCMAKE_PREFIX_PATH=~/Qt/6.2.0/macos/lib/cmake
-DCMAKE_TOOLCHAIN_FILE:PATH=~/Qt/6.2.0/wasm_32/lib/cmake/Qt6/qt.toolchain.cmake
# 或指定以下工具链
-DCMAKE_TOOLCHAIN_FILE:PATH=/opt/emsdk/upstream/emscripten/cmake/Modules/Platform/Emscripten.cmake
```

## 启动本机http-server服务

```bash
npm i -g http-server   # 安装工具
http-server --cors   # 在生成的wasm文件所在目录执行命令
```

## 手动进行brotli压缩

验证生成的wasm文件下载时的大小

```bash
npm i -g brotli-cli   # 安装压缩工具
brotli-cli compress qt-wasm.wasm    # 在生成的wasm文件所在目录执行命令
```
