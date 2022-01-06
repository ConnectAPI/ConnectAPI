FROM python:3.10-slim-buster

RUN pip install poetry
COPY ./poetry.toml ./poetry.toml
COPY ./pyproject.toml ./pyproject.toml
RUN poetry install --no-dev

COPY . .

WORKDIR ./cli

VOLUME /var/run/docker.sock


ENTRYPOINT ["python", "run.py"]