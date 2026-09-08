import aio_pika

class RabbitMQ:
    def __init__(self, address: str):
       self.address = address
       self.connection = None
       self.channel = None

    async def connect(self):
        self.connection = await aio_pika.connect_robust(self.address)
        self.channel = await self.connection.channel()
        await self.channel.declare_queue(
            "new_order",
            durable=True
        )

    async def close(self):
        if self.connection:
            await self.connection.close()
