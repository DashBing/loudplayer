# loudplayer
### *不会停下的播放器*
### *本项目仅供娱乐，基于本项目修改的任何其他项目，所造成的任何严重后果，本项目以及所有贡献者不承担责任*
### 本项目由Python3.11环境下编写，资源在该环境下编译
[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg?style=flat)](http://choosealicense.com/licenses/mit/)
### 说明文档语言仅支持简体中文

# 项目链接
[Github](https://github.com/DashBing/loudplayer/ "Github")
<br><br>
[Kgithub](https://kgithub.com/DashBing/loudplayer/)：国内Github镜像站，可能会有延迟，推送请使用Github链接推送

# 从源码构建
### 注意：本项目并非跨平台，仅支持在Windows平台下运行
## 准备工作
+ 安装git和make (方法自行百度)
+ 安装Python(3.9版本或者3.11版本皆可)
+ 从源码仓库克隆源代码
```
git clone git@github.com:DashBing/phap.git
```
#### 或者
```
git clone https://github.com/DashBing/phap.git
```
### 国内网比较差可以尝试：
```
git clone https://kgithub.com/DashBing/phap.git
```

## 初始化打包环境
### 注意，如果你已经安装nuitka了请不要使用以下命令
```
make init
```
#### 或者
#### 尝试手动安装以下包:
+ nuitka

## 构建项目
```
make build
```
