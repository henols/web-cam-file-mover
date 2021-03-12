FROM alpine:latest

# Install python/pip
ENV PYTHONUNBUFFERED=1

RUN apk add --update --no-cache bash
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools

RUN echo "* * * * * /job.sh; exit 0" | crontab - 
ADD walker.py /
ADD job.sh /
RUN chmod +x /job.sh

CMD [ "crond", "-f"]