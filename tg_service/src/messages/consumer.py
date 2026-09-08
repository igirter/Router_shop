import json

from src.messages.connector import RabbitMQ


class RabbitConsumer:
    def __init__(self, rabbit: RabbitMQ):
        self.rabbit = rabbit

    async def consume(self, queue_name: str, callback):
        queue = await self.rabbit.channel.get_queue(queue_name)

        async with queue.iterator() as queue_iter:
            async for message in queue_iter:
                async with message.process():
                    data = json.loads(
                        message.body.decode("utf-8")
                    )

                    await callback(data)
