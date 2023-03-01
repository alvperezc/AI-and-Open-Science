FROM ubuntu:lunar

MAINTAINER a.pcaceres@alumnos.upm.es

COPY ./textextraction /ExtractText

RUN apt-get update && apt-get install 

RUN apt-get install python3.10 -y 

RUN apt-get install wget -y

RUN wget https://bootstrap.pypa.io/get-pip.py

RUN python3.10 get-pip.py

RUN pip install poetry

WORKDIR /ExtractText/

EXPOSE 8070

RUN poetry install

