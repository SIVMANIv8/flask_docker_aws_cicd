FROM python:3.7.1-alpine

WORKDIR /docker_aws_cicd
COPY .  /docker_aws_cicd
RUN pip install -r requirements.txt
RUN python -m  pytest
CMD ["gunicorn",  "-b", "0.0.0.0:7000", "app:app"]
