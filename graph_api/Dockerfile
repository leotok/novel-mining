FROM python:3.6-slim

RUN python3.6 -m pip install pip --upgrade

WORKDIR /app
ADD graph_api/requirements.txt requirements.txt

RUN pip3.6 install pip --upgrade && \
    pip3.6 install -r requirements.txt

ADD . .

ENV LC_ALL=C.UTF-8 LANG=C.UTF-8 PYTHONPATH=/app

ENV WORKERS=2
ENV LOGLEVEL=info

EXPOSE 8000

CMD gunicorn --reload -t 30 -w ${WORKERS} --log-level ${LOGLEVEL} --worker-class gevent --bind 0.0.0.0:8000 graph_api.app:api
