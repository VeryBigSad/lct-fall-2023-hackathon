FROM python:3.11.5-slim-bookworm

WORKDIR /app
ENV PYTHONUNBUFFERED=1
COPY requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /app

COPY docker-entrypoint.sh docker-entrypoint.sh
RUN chmod +x docker-entrypoint.sh

ENTRYPOINT ["sh", "./docker-entrypoint.sh"]