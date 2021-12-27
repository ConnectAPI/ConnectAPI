FROM python:3.10-slim-buster

COPY . .

RUN pip install -r requirements.txt --no-cache-dir

WORKDIR ./src

VOLUME /var/run/docker.sock


ENTRYPOINT ["python", "run.py"]