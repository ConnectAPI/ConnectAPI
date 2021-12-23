FROM python:3.10-slim-buster

RUN pip install -r --no-cache-dir requirements.txt

COPY . .

WORKDIR ./src

VOLUME /var/run/docker.sock

CMD ["python", "configure.py"]