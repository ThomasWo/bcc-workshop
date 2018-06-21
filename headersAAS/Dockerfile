FROM python:alpine
MAINTAINER Thomas Wodarek <thomas.wodarek@gmail.com>

RUN mkdir -p /code
WORKDIR /code

ADD . /code
RUN pip install -r requirements.txt

CMD python app.py
