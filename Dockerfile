FROM python:3.10-slim-buster

COPY . .

RUN pip install -r requirements.txt --no-cache-dir

RUN mkdir /usr/data

WORKDIR ./src

VOLUME /var/run/docker.sock
VOLUME /usr/data


CMD ["python", "configure.py"]