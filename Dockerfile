FROM ubuntu:18.04

RUN apt-get update -y
RUN apt-get install -y python3-pip

COPY . /usr/local/2019-paper-bloch-point-stability/
WORKDIR /usr/local/2019-paper-bloch-point-stability
RUN python3 -m pip install numpy matplotlib seaborn

# Commands to make Binder work.
RUN python3 -m pip install --no-cache-dir notebook==5.*
ENV NB_USER binderuser
ENV NB_UID 1000
ENV HOME /home/${NB_USER}

RUN adduser --disabled-password \
    --gecos "Default user" \
    --uid ${NB_UID} \
    ${NB_USER}

COPY . ${HOME}
USER root
RUN chown -R ${NB_UID} ${HOME}
RUN chown -R ${NB_UID} /usr/local/2019-paper-bloch-point-stability
USER ${NB_USER}