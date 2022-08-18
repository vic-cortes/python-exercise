FROM python:3.9.13-slim-bullseye as base

# Local timezone
ENV APP_NAME="python-exercise" \
    TZ="America/Monterrey" \
    PYTHONDONTWRITEBYTECODE=1 \
    BASEPATH=/opt/${APP_NAME}

WORKDIR ${BASEPATH}
COPY poetry.lock .
COPY pyproject.toml .
RUN pip install poetry
# Do not make virtual environments, already in a container
RUN poetry config virtualenvs.create false

FROM base AS production

ENV ENVIRONMENT="prod"
RUN poetry install --no-dev
WORKDIR ${BASEPATH}/src

CMD ["python", "-u", "main.py"]


FROM base AS dev

# Do not make virtual environments, alrady in a container
ENV ENVIRONMENT="dev" \
    PYTHONUNBUFFERED=1 
# Turns off buffering for easier container logging
RUN poetry install
WORKDIR ${BASEPATH}/src

CMD ["python", "-u", "main.py"]
