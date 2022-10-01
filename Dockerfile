FROM python:3.9

WORKDIR /usr/src/src

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR ../
COPY Pipfile .
COPY Pipfile.lock .
WORKDIR /usr/src/src
COPY src .
WORKDIR ../students_db
COPY students_db .
WORKDIR ../


RUN pip install pipenv
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy --system

EXPOSE 5000

WORKDIR /usr/src/src
CMD ["flask", "--app", "main.py", "run", "--host", "0.0.0.0"]



