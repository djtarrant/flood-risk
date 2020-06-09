FROM alpine:latest

RUN apk add --no-cache python3-dev \
    && apk update \
    && apk add py-pip \
    && pip install --upgrade pip

RUN mkdir -p /var/www
RUN mkdir -p /var/www/app
WORKDIR /var/www/app
COPY /app /var/www/app
RUN pip3 --no-cache-dir install -r requirements.txt
EXPOSE 5000

ENTRYPOINT ["python3"]
CMD ["app.py"]