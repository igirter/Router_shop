from fastapi import FastAPI

from src.db import Base, engine
from src.routers import router

from contextlib import asynccontextmanager
from src.messages.connector import RabbitMQ
from src.messages.producer import RabbitProducer
from dotenv import load_dotenv
import os
from typing import cast



load_dotenv()

RABBIT_URL = cast(str, os.getenv("RABBIT_URL"))

@asynccontextmanager
async def lifespan(app: FastAPI):
    rabbit = RabbitMQ(RABBIT_URL)
    await rabbit.connect()
    producer = RabbitProducer(rabbit)

    app.state.rabbit = rabbit
    app.state.producer = producer

    yield
    await rabbit.close()

app = FastAPI(lifespan=lifespan)
app.include_router(router, prefix="/api")
Base.metadata.create_all(bind=engine)
