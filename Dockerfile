FROM python:3.7.1-alpine

WORKDIR /flask_docker_aws_cicd
COPY .  /flask_docker_aws_cicd
RUN pip install -r requirements.txt
RUN python -m  pytest
CMD ["gunicorn",  "-b", "0.0.0.0:7000", "app:app"]
