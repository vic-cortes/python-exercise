FROM python:3.9

# Local timezone
ENV APP_NAME="python-exercise"
ENV TZ="America/Monterrey"

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

RUN pip install poetry

COPY . ${APP_NAME}
RUN chmod 755 ${APP_NAME}

WORKDIR /${APP_NAME}

# Do not make virtual environments, alrady in a container
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

WORKDIR /${APP_NAME}/src
RUN chmod 777 main.py

CMD ["python", "-u", "main.py"]