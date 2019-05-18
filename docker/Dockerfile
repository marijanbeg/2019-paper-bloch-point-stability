FROM ubuntu:18.04

RUN apt-get update -y
RUN apt-get install -y git python3-pip curl
RUN python3 -m pip install --upgrade pip nbval numpy matplotlib==3.0.3 seaborn

COPY . /usr/local/joommfutil/
WORKDIR /usr/local/joommfutil
