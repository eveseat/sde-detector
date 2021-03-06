FROM python:3.9-alpine

LABEL maintainer="Leon Jacobs <leonja511@gmail.com>"

WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "main.py"]
