FROM python:3.10
ENV PYTHONUNBUFFERED 1
RUN mkdir docker_app
WORKDIR /docker_app
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT ["sh", "/docker_app/docker-entrypoint.sh"]