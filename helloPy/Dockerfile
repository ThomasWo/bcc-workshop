FROM python:alpine
MAINTAINER Thomas Wodarek <thomas@wodarek.com>

RUN mkdir -p /code
WORKDIR /code

ADD . /code
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "app.py"]
