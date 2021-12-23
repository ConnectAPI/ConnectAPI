FROM python:3.10-slim-buster

RUN apt update
RUN apt install curl
RUN curl -L "https://github.com/docker/compose/releases/download/1.27.4/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
RUN chmod +x /usr/local/bin/docker-compose

COPY . .

WORKDIR ./src

VOLUME /var/run/docker.sock

CMD ["python", "configure.py"]