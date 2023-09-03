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
* docker push <映像名稱>：將本地映像上傳到 Docke以下是 Dockerfile 的基本語法和一些常見的指令：

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

## Dockerfile語法
1. 基本語法：
* Dockerfile 是一個純文本文件，每行包含一個 Docker 命令或指令。
* 每個指令都以大寫字母開頭，並以換行符或分號（;）結尾。
* 指令的參數位於指令名稱之後，可以有多個參數，用空格分隔。
2. 常見指令：

* FROM <基礎映像>：指定基礎映像。
* RUN <命令>：在容器內執行命令，用於安裝軟體、設置環境等。
* COPY <來源> <目的地>：將來源檔案/目錄複製到映像內的目的地。
* ADD <來源> <目的地>：類似於 COPY，但還支援解壓縮 URL 和複製遠端檔案。
* WORKDIR <工作目錄>：設定工作目錄，後續的命令將在這個目錄中執行。
* ENV <變數名稱> <值>：設定環境變數。
* EXPOSE <端口>：聲明映像將在哪些端口上聽取。
* CMD <命令>：設定容器啟動時要執行的命令。r 倉庫。


