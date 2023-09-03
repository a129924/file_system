@echo off

cls
docker build -t my-python-app .
docker run -p 8080:8080 -v D:\code\python\docker_test:/app my-python-app


