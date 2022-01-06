FROM python:3.10-slim-buster

COPY ./poetry.toml ./poetry.toml
COPY ./pyproject.toml ./pyproject.toml
RUN pip install poetry
RUN poetry install

COPY . .

WORKDIR ./src

VOLUME /var/run/docker.sock


ENTRYPOINT ["python", "run.py"]