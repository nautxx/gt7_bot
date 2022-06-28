
# syntax=docker/dockerfile:1

FROM python:3.8

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

ENV PORT=8080

EXPOSE 8080

CMD [ "python", "main.py" ]