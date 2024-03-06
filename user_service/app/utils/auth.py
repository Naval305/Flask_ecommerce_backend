import pika

from config.config import (
    rabbitmq_host,
    rabbitmq_port,
    rabbitmq_user,
    rabbitmq_password,
    rabbitmq_token_exchange,
    rabbitmq_token_routing_key,
)


class AuthenticateToken:
    def __init__(self) -> None:
        credentials = pika.PlainCredentials(
            username=rabbitmq_user, password=rabbitmq_password
        )
        parameters = pika.ConnectionParameters(
            host=rabbitmq_host, port=rabbitmq_port, credentials=credentials
        )
        self.connection = pika.BlockingConnection(parameters=parameters)
        self.channel = self.connection.channel()

    def publish_toke