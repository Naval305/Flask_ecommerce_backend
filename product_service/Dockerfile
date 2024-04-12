FROM python:3.10
ENV PYTHONUNBUFFERED 1
RUN mkdir product_app
WORKDIR /product_app
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT ["sh", "/product_app/docker-entrypoint.sh"]