FROM ubuntu:latest

# 更新套件並安裝Python3
RUN apt-get update && \
    apt-get install -y python3 && \
    apt-get install -y python3-pip

RUN pip3 install flask[async]

# 建立工作目錄並複製程式碼
WORKDIR /app
COPY app.py /app/
COPY lib /app/lib/

CMD [ "python3", "app.py" ]
