from dotenv import load_dotenv
import os
import asyncio
from typing import cast

from aiogram import Bot, Dispatcher

from services import message_service
from telegram import sender


load_dotenv()

TOKEN = cast(str, os.getenv("TOKEN"))

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


async def main():
    message = message_service.format_message(s)

    await sender.send_message(
        bot,
        1130300286,
        message
    )


if __name__ == "__main__":
    asyncio.run(main())
