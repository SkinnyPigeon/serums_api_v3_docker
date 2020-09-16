FROM skinnypigeon/serums-start:latest

RUN apt-get update -y \
    && apt-get install -y 