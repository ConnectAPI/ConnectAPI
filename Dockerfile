FROM python:3.10-slim-buster

COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt --no-cache-dir

COPY . .

WORKDIR ./src

VOLUME /var/run/docker.sock


ENTRYPOINT ["python", "run.py"]