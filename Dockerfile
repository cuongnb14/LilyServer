# Author: Cuong Nguyen
#
# Build: docker build -t cuongnb14/lily_api:0.1 .
# Run: docker run -d -p 8080:8080 --name lily_api cuongnb14/lily_api:0.1
#

FROM ubuntu:16.04
MAINTAINER Cuong Nguyen "cuongnb14@gmail.com"


ENV DB_NAME oxwall
ENV DB_USER root
ENV DB_PASS root
ENV DB_HOST 172.17.0.1
ENV DB_PORT 3306

ENV ES_HOST 172.17.0.1
ENV ES_PORT 9200


RUN apt-get update -qq

RUN DEBIAN_FRONTEND=noninteractive apt-get install -y python3 python3-pip build-essential python3-dev git

RUN DEBIAN_FRONTEND=noninteractive apt-get install -y libmysqlclient-dev \
        libxml2-dev libxslt1-dev

RUN DEBIAN_FRONTEND=noninteractive apt-get install -y libssl-dev libffi-dev

RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements/ requirements/
RUN pip3 install -r requirements/local.txt
RUN pip3 install -r requirements/production.txt

WORKDIR /
RUN pip3 install -e "git+https://github.com/tranhuucuong91/Py3kAiml.git#egg=pyaiml"

WORKDIR /usr/src/app
COPY . /usr/src/app

EXPOSE 8000

ENV C_FORCE_ROOT="true"
CMD /usr/local/bin/gunicorn config.wsgi:application -w 2 -b :8000

