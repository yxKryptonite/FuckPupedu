<div align=center><img src="assets/icon-transparent.png" height=250></div>

## 简介

北京大学新时代劳动教育理论课自动化脚本

## 使用方法

1. 安装 [Python 3.6+](https://www.python.org/downloads/) 和 [Chrome](https://www.google.cn/intl/zh-CN/chrome/) 浏览器
2. 将本仓库克隆至本地
   
    ```bash
    git clone git@github.com:yxKryptonite/FuckPupedu.git
    cd FuckPupedu
    ```

3. 运行初始化脚本进行依赖安装
   
    ```bash
    sh setup.sh
    ```

4. 在 `config.yml` 中填写 IAAA 学号、密码以及其他可选参数
5. 运行脚本，开启你的赛博劳改之旅

    ```bash
    python main.py -vpn
    ```

## 它能做什么

它可以播放视频、浏览 PPT、记笔记

## 它不能做什么 (你需要做什么)

目前还不能完成每章的测验

(正在佛系开发中...不过这部分手动完成应该很快的罢)

## 使用过程中，需要注意什么

- 建议**夜间插电挂机**使用 (视频总时长超过20小时😴)
- 配合 [`tmux`](https://github.com/tmux/tmux) 使用效果更佳
- 使用时建议关闭网络代理，并保证网络畅通
- 笔记本电脑使用尽量避免合盖，或设置合盖不休眠

## LICENSE

[GPL-3.0](https://github.com/yxKryptonite/FuckPupedu/blob/master/LICENSE)

copyright (c) 2023 [@yxKryptonite](https://github.com/yxKryptonite)