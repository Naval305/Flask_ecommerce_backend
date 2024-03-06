import json

import pika
from pika.exchange_type import ExchangeType

from app.config.config import (
    rabbitmq_host,
    rabbitmq_password,
    rabbitmq_port,
    rabbitmq_user,
    rabbitmq_token_exchange,
    rabbitmq_token_routing_key,
)


class ConnectUserService:
    def __init__(self) -> None:
        credentials = pika.PlainCredentials(
            username=rabbitmq_user, password=rabbitmq_password
        )
        parameters = pika.ConnectionParameters(
            host=rabbitmq_host, port=rabbitmq_port, credentials=credentials
        )
        self.connection = pika.BlockingConnection(parameters=parameters)
        self.channel = self.connection.channel()

    def publish_token_to_queue(self, token):
        self.channel.exchange_declare(
            exchange=rabbitmq_token_exchange,
            exchange_type=ExchangeType.direct,
            passive=False,
            durable=True,
            auto_delete=False,
        )

        self.channel.basic_publish(
            exchange=rabbitmq_token_exchange,
            routing_key=rabbitmq_token_routing_key,
            body="",
            properties=pika.BasicProperties(
                headers={"Authorization": f"Bearer {token}"}
            ),
        )
        self.connection.close()
