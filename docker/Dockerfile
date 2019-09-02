FROM ubuntu:16.04

RUN apt update && apt install -y git python3-pip

RUN pip3 install gunicorn flask flask_restful

LABEL build="190902a"

RUN git clone https://github.com/Utrum/python-OP_RETURN.git

RUN mkdir /conf \
    && mv /python-OP_RETURN/user_defined.py.example \
    /python-OP_RETURN/user_defined.py

RUN useradd gunicorn

COPY entrypoint.sh /

ENTRYPOINT /entrypoint.sh

