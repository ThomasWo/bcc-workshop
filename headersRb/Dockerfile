FROM ruby:2.3.3

MAINTAINER Thomas Wodarek <thomas@wodarek.com>

ENV RACK_ENV production
ENV MAIN_APP_FILE web.rb
RUN apt-get update
RUN apt-get install build-essential libmysqlclient-dev -y

RUN echo "Starting your CN quic sinatra build."
RUN mkdir -p /code
WORKDIR /code

ADD Gemfile /code/
RUN bundler install

ADD startup.sh /code/
ADD web.rb /code/

ENTRYPOINT ["/code/startup.sh"]
