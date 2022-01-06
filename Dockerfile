FROM python:3.10-slim-buster

COPY ./poetry.toml ./poetry.toml
COPY ./pyproject.toml ./pyproject.toml
RUN pip install poetry
RUN poetry install --no-dev

COPY . .

WORKDIR ./cli

VOLUME /var/run/docker.sock


ENTRYPOINT ["python", "run.py"]