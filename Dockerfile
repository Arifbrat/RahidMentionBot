FROM nikolaik/python-nodejs:python3.9-nodejs18
FROM debian:latest
FROM python:3.9.6-slim-buster
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get -qq update -y && apt-get -qq upgrade -y
RUN apt update && apt upgrade -y
RUN apt install git curl python3-pip -y
RUN apt install python -y
RUN pip3 install -U pip
RUN apt-get -qq install -y \
    git \
    curl \
    wget \
    ffmpeg \
    opus-tools

RUN pip install telethon
RUN pip3 install requirements.txt
RUN chmod a+x start
CMD ["./start"]
