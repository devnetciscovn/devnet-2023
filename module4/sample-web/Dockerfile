FROM ubuntu
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update
RUN apt-get install -y python3 python3-pip python3-flask
COPY app.py /app.py
COPY templates /templates
COPY static /static
RUN export FLASK_APP=app.py
CMD flask run --host=0.0.0.0
