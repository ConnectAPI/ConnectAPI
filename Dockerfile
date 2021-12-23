FROM python:3.10-slim-buster

RUN sudo curl -L "https://github.com/docker/compose/releases/download/1.27.4/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
RUN sudo chmod +x /usr/local/bin/docker-compose

COPY . .

WORKDIR ./src

VOLUME /var/run/docker.sock

CMD ["python", "configure.py"]