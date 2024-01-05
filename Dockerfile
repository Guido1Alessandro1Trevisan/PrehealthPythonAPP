
FROM python:3.9.17-bookworm

ENV PYTHONUNBUFFERED True

ENV APP_HOME /back-end

COPY .  ./

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app