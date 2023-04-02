FROM docker.io/library/debian:bullseye

RUN apt-get update

# buster default is python2
RUN apt-get install -y python3.6

# LaTex
RUN apt-get install -y \
      texlive-science \
      texlive-xetex \
      texlive-publishers

RUN apt-get install -y python3-pip
RUN apt-get install -y git

COPY requirements.txt /opt/apt/requirements.txt
WORKDIR /opt/apt
RUN pip3 install -r requirements.txt

COPY SAMRI/ /opt/apt/SAMRI/
WORKDIR /opt/apt/SAMRI
RUN pip3 install .

COPY LabbookDB/ /opt/apt/LabbookDB/
WORKDIR /opt/apt/LabbookDB/
RUN pip3 install .

COPY . /opfvta
WORKDIR /opfvta
