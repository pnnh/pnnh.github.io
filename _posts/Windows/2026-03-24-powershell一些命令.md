---
layout: post
title: "powershell一些命令"
date: 2026-03-24 00:00:00 +0800
categories: [Windows]
tags: [windows]
---

# PowerShell 常用命令

## 基本操作

### 返回上一个命令的执行状态
```powershell
$?
```

### 清屏
```powershell
Clear-Host
# 或者
cls
```

### 查看命令历史
```powershell
Get-History
```

### 获取命令帮助
```powershell
Get-Help CommandName
Get-Help CommandName -Examples
```

### 修改命令提示符
默认只对当前会话有效
```powershell
function prompt {"PS [$Env:username@$Env:computername] $($PWD.ProviderPath)> "}
```

## 文件操作

### 列出文件和目录
```powershell
Get-ChildItem
# 或者
ls
dir
```

### 列出所有文件（包括隐藏文件）
```powershell
Get-ChildItem -Force
```

### 递归列出所有文件
```powershell
Get-ChildItem -Recurse
```

### 创建单个目录
```powershell
New-Item -Path "C:\path\to\your\directory" -ItemType Directory
```

### 递归创建多级目录
```powershell
New-Item -Path "C:\path\to\your\directory\subdirectory" -ItemType Directory
```

### 检查目录是否存在
```powershell
if (-Not (Test-Path "C:\path\to\your\directory")) {
    New-Item -Path "C:\path\to\your\directory" -ItemType Directory
}
```

### 删除文件
```powershell
Remove-Item -Path "C:\path\to\your\file.txt"
```

### 通配符方式删除多个文件
```powershell
Remove-Item -Path "C:\path\to\your\*.txt"
```

### 删除目录及其内容
```powershell
Remove-Item -Path "C:\path\to\directory" -Recurse
```

### 强制删除（不提示确认）
```powershell
Remove-Item -Path "C:\path\to\file" -Force
```

### 复制文件
```powershell
Copy-Item -Path "C:\source\file.txt" -Destination "C:\destination\file.txt"
```

### 复制文件夹及其内容
```powershell
Copy-Item -Path "C:\source\folder" -Destination "C:\destination\folder" -Recurse
```

### 移动文件夹
```powershell
Move-Item -Path "C:\source\folder" -Destination "C:\destination"
```

### 移动文件夹并重命名
```powershell
Move-Item -Path "C:\source\folder" -Destination "C:\destination\newfoldername"
```

### 移动文件夹里的内容而不是文件夹本身
```powershell
Move-Item -Path "C:\source\folder\*" -Destination "C:\destination"
```

### 重命名文件或文件夹
```powershell
Rename-Item -Path "C:\path\to\oldname.txt" -NewName "newname.txt"
```

### 获取文件内容
```powershell
Get-Content -Path "C:\path\to\file.txt"
```

### 设置文件内容（覆盖）
```powershell
Set-Content -Path "C:\path\to\file.txt" -Value "New content"
```

### 追加文件内容
```powershell
Add-Content -Path "C:\path\to\file.txt" -Value "Additional content"
```

### 搜索文件内容
```powershell
Select-String -Path "C:\path\to\file.txt" -Pattern "search text"
```

### 递归搜索多个文件
```powershell
Get-ChildItem -Path "C:\path" -Recurse | Select-String -Pattern "search text"
```

### 获取文件属性
```powershell
Get-ItemProperty -Path "C:\path\to\file.txt"
```

### 获取文件大小
```powershell
(Get-Item "C:\path\to\file.txt").Length
```

## 压缩与解压

### 解压zip文件到指定路径
```powershell
Expand-Archive -Path "C:\Files\example.zip" -DestinationPath "C:\Files\Extracted"
```

### 压缩文件夹为zip
```powershell
Compress-Archive -Path "C:\path\to\folder" -DestinationPath "C:\path\to\archive.zip"
```

### 压缩多个文件
```powershell
Compress-Archive -Path "C:\file1.txt", "C:\file2.txt" -DestinationPath "C:\archive.zip"
```

### 添加文件到现有zip
```powershell
Compress-Archive -Path "C:\newfile.txt" -Update -DestinationPath "C:\archive.zip"
```

## 网络操作

### 下载并保存文件
```powershell
Invoke-WebRequest -Uri "https://example.com/file.zip" -OutFile "file.zip"
```

### 测试网络连接
```powershell
Test-Connection -ComputerName google.com -Count 4
```

### 测试端口连接
```powershell
Test-NetConnection -ComputerName example.com -Port 80
```

### 查看网络配置
```powershell
Get-NetIPAddress
```

### 查看网络适配器
```powershell
Get-NetAdapter
```

### 刷新DNS缓存
```powershell
Clear-DnsClientCache
```

### 查看DNS缓存
```powershell
Get-DnsClientCache
```

## 进程与服务

### 查看所有进程
```powershell
Get-Process
```

### 查看特定进程
```powershell
Get-Process -Name "processname"
```

### 停止进程
```powershell
Stop-Process -Name "processname"
Stop-Process -Id 1234
```

### 强制停止进程
```powershell
Stop-Process -Name "processname" -Force
```

### 查看所有服务
```powershell
Get-Service
```

### 查看特定服务
```powershell
Get-Service -Name "ServiceName"
```

### 启动服务
```powershell
Start-Service -Name "ServiceName"
```

### 停止服务
```powershell
Stop-Service -Name "ServiceName"
```

### 重启服务
```powershell
Restart-Service -Name "ServiceName"
```

## 系统信息

### 查看系统信息
```powershell
Get-ComputerInfo
```

### 查看操作系统版本
```powershell
Get-CimInstance Win32_OperatingSystem
```

### 查看CPU信息
```powershell
Get-CimInstance Win32_Processor
```

### 查看内存信息
```powershell
Get-CimInstance Win32_PhysicalMemory
```

### 查看磁盘信息
```powershell
Get-PSDrive
# 或者
Get-Disk
```

### 查看磁盘空间
```powershell
Get-Volume
```

### 查看当前用户
```powershell
$env:USERNAME
```

### 查看计算机名
```powershell
$env:COMPUTERNAME
```

## 环境变量

### 查看所有环境变量
```powershell
Get-ChildItem Env:
```

### 查看特定环境变量
```powershell
$env:PATH
$env:USERPROFILE
```

### 设置环境变量（当前会话）
```powershell
$env:MY_VARIABLE = "value"
```

### 设置用户级环境变量（永久）
```powershell
[Environment]::SetEnvironmentVariable("MY_VARIABLE", "value", "User")
```

### 设置系统级环境变量（永久）
```powershell
[Environment]::SetEnvironmentVariable("MY_VARIABLE", "value", "Machine")
```

### 删除环境变量
```powershell
Remove-Item Env:\MY_VARIABLE
```

## 软件安装

### 以静默方式安装msi安装包
```powershell
msiexec /i example.msi /quiet
```

### 以静默方式安装exe安装包
```powershell
Start-Process -FilePath "C:\path\to\your\example.exe" -ArgumentList "/silent" -NoNewWindow -Wait
```

### 卸载msi安装包
```powershell
msiexec /x example.msi /quiet
```

## 用户与权限

### 以管理员身份运行命令
```powershell
Start-Process powershell -Verb RunAs
```

### 查看当前用户权限
```powershell
whoami /priv
```

### 查看本地用户
```powershell
Get-LocalUser
```

### 查看本地组
```powershell
Get-LocalGroup
```

## 日期与时间

### 获取当前日期时间
```powershell
Get-Date
```

### 格式化日期
```powershell
Get-Date -Format "yyyy-MM-dd HH:mm:ss"
```

### 获取特定格式的日期
```powershell
Get-Date -Format "yyyyMMdd"
```

## 其它实用命令

### 查看PowerShell版本
```powershell
$PSVersionTable
```

### 计算命令执行时间
```powershell
Measure-Command { Your-Command }
```

### 创建符号链接
```powershell
New-Item -ItemType SymbolicLink -Path "C:\link" -Target "C:\original"
```

### 查找命令
```powershell
Get-Command *keyword*
```

### 查看别名
```powershell
Get-Alias
```

### 设置别名
```powershell
Set-Alias -Name ll -Value Get-ChildItem
```

### 输出到文件
```powershell
Get-Process | Out-File -FilePath "C:\processes.txt"
```

### 排序输出
```powershell
Get-Process | Sort-Object CPU -Descending
```

### 筛选输出
```powershell
Get-Process | Where-Object {$_.CPU -gt 10}
```

### 选择特定属性
```powershell
Get-Process | Select-Object Name, CPU, Memory
```
