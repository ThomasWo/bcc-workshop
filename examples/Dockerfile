FROM ubuntu:latest
MAINTAINER Thomas Wodarek <thomas@wodarek.com>
LABEL maintainer="Thomas Wodarek <thomas@wodarek.com>"

USER twodarek # Default is root
ENV APP_IS_CAT "nope"
RUN apt-get update -qq
RUN ["apt-get", "install", "vim", "-y", "-qq"]
RUN ["/bin/bash", "-c", "apt-get", "install", "htop", "-y", "-qq"]
RUN mkdir -p /code
WORKDIR /code
VOLUME /code

ADD startup.sh /code/
ADD https://wodarek.com/psalm22.wav /code/
COPY shutdown.sh /code/
EXPOSE 80   # ONLY TCP
EXPOSE 80/udp

HEALTHCHECK --interval=30s --timeout=30s --start-period=0s --retries=3 \
  CMD curl -f http://localhost/ || exit 1

CMD startup.sh
CMD ["startup.sh"] # Exec form
ENTRYPOINT startup.sh
ENTRYPOINT ["startup.sh"]

