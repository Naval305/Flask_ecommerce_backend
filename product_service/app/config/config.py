import os

from dotenv import load_dotenv


load_dotenv()

db_name = os.getenv("DB_NAME")
db_host = os.getenv("DB_HOST")
db_port = int(os.getenv("DB_PORT"))

rabbitmq_host = os.getenv("RABBITMQ_HOST")
rabbitmq_port = os.getenv("RABBITMQ_PORT")
rabbitmq_user = os.getenv("RABBITMQ_USER")
rabbitmq_password = os.getenv("RABBITMQ_PASSWORD")
rabbitmq_token_exchange = os.getenv("RABBITMQ_TOKEN_EXCHANGE")
rabbitmq_token_routing_key = os.getenv("RABBITMQ_TOKEN_ROUTING_KEY")