import aio_pika
import json

from src.messages.connector import RabbitMQ


class RabbitProducer:
    def __init__(self, rabbit: RabbitMQ):
        self.rabbit = rabbit

    async def publish(self, queue_name: str, message: dict):
        await self.rabbit.channel.default_exchange.publish(
            aio_pika.Message(
                body=json.dumps(message).encode("utf-8")
            ),
            routing_key=queue_name
        )
