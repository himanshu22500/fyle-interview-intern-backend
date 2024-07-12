FROM python:3.8

WORKDIR /app

ADD . /app

RUN pip install --no-cache-dir -r requirements.txt

ENV FLASK_APP=core/server.py

RUN flask db upgrade -d core/migrations/

EXPOSE 7755

CMD ["bash", "run.sh"]