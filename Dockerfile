FROM alpine:3.11

ADD requirements.txt requirements.txt

RUN apk update
RUN apk add --no-cache gcc g++ python3 python3-dev musl musl-dev postgresql postgresql-dev alpine-sdk linux-headers libffi-dev\
    && pip3 install -U pip \
    && pip3 install -U setuptools \
    && pip3 install -U cython \
    && pip3 install -r requirements.txt \
    && apk del gcc g++ python3-dev musl-dev postgresql-dev alpine-sdk linux-headers libffi-dev

COPY . pokemon/

WORKDIR /pokemon
