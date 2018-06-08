FROM ubuntu:latest
MAINTAINER liuyang19900520 "liuyang19900520@hotmail.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
COPY . /config.py
WORKDIR /config.py
COPY . /requirements.txt
WORKDIR /requirements.txt
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]