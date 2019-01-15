FROM python:3

WORKDIR /app

COPY src /app/

RUN pip3 install -r requirements.txt

ENV FLASK_APP=/app/main.py

ENTRYPOINT ["flask", "run"]