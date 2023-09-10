FROM python:slim

ENV PYTHONUNBUFFERED 1

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY only_friends only_friends
COPY waitlist waitlist
WORKDIR /only_friends