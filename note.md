---
title: Docker筆記
date: 2023/09/02
---

# Docker筆記

## Docker cli語法
1. 容器管理：

* docker run <映像名稱>：從映像創建並啟動容器。
* docker ps：列出正在運行的容器。
* docker stop <容器ID>：停止運行中的容器。
* docker start <容器ID>：啟動已停止的容器。
* docker restart <容器ID>：重新啟動容器。
* docker rm <容器ID>：刪除容器。
2. 映像管理：

* docker images：列出所有本機映像。
* docker pull <映像名稱>：從 Docker 倉庫下載映像。
* docker build -t <映像名稱>:<標籤> <Dockerfile路徑>：從 Dockerfile 建立映像。
* docker push <映像名稱>：將本地映像上傳到 Docker 倉庫。

3. 資料卷和網路：

* docker volume ls：列出所有資料卷。
* docker volume create <資料卷名稱>：創建一個新的資料卷。
* docker network ls：列出所有網路。
* docker network create <網路名稱>：創建一個新的網路。

4. 其他：

* docker exec -it <容器ID> <命令>：在運行中的容器內執行命令。
* docker logs <容器ID>：查看容器的日誌。
* docker inspect <容器ID或映像名稱>：檢查容器或映像的詳細信息。
* docker-compose up：使用 Docker Compose 啟動多個容器（需要 * docker-compose.yml 文件）。