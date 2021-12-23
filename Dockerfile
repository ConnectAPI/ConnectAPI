FROM python:3.10-slim-buster

COPY . .

RUN pip install -r --no-cache-dir requirements.txt

WORKDIR ./src

VOLUME /var/run/docker.sock

CMD ["python", "configure.py"]