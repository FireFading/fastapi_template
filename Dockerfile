FROM python:buster

WORKDIR /code

RUN apt update

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY ./requirements.txt ./
COPY ./.env /code/
COPY ./alembic.ini ./
COPY ./migrations ./migrations
COPY ./app ./app

RUN pip3 install --upgrade pip --no-cache-dir && pip3 install -r requirements.txt --no-cache-dir

CMD ["alembic", "upgrade", "head"]
