# syntax=docker/dockerfile:1

FROM python:3.8.3-alpine

WORKDIR /flaskProject2

ADD . /flaskProject2

RUN pip install -r requirements.txt

CMD ["python","app.py"]