from dotenv import load_dotenv
import os
import asyncio
from typing import cast

from aiogram import Bot, Dispatcher

from services import message_service
from telegram import sender

from aiogram.filters import Command
from aiogram.types import Message
from services import user_service
from database.db import SessionLocal
from database.db import engine, Base

from messages.connector import RabbitMQ
from messages.consumer import RabbitConsumer

load_dotenv()

TOKEN = cast(str, os.getenv("TOKEN"))
RABBIT_URL = cast(str, os.getenv("RABBIT_URL"))

bot = Bot(TOKEN)
dp = Dispatcher()


s = {
    "full_name": "Игорь",
    "phone": "89999999999",
    "email": "igir@mail.ru",
    "address": "Челябинск Яркая 13",
    "items": [
        {
            "product_name": "Роутер",
            "count": 1,
            "price": 2000
        },
        {
            "product_name": "Роутер2",
            "count": 2,
            "price": 4000
        }
    ]
}

@dp.message(Command("start"))
async def start(message: Message):
    telegram_id = message.from_user.id

    db = SessionLocal()

    try:
        user = user_service.create_user(
            telegram_id,
            db
        )

        print(user)

    finally:
        db.close()

async def send_message_all_subscribers(s: str):

    db = SessionLocal()

    try:
        users = user_service.get_all_subscribers(db)

        for user in users:
            await sender.send_message(
                bot,
                user.tg_id,
                s
            )

    finally:
        db.close()


async def handle_order(data):
    print("ПОЛУЧЕН ЗАКАЗ:", data)

    message = message_service.format_message(data)

    await send_message_all_subscribers(message)

async def main():
    Base.metadata.create_all(bind=engine)

    rabbit = RabbitMQ(RABBIT_URL)
    await rabbit.connect()

    consumer = RabbitConsumer(rabbit)

    await asyncio.gather(
        consumer.consume("new_order", handle_order),
        dp.start_polling(bot),
    )


if __name__ == "__main__":
    asyncio.run(main())
