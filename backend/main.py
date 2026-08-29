from fastapi import FastAPI
from src.db import engine, Base
from src.routers import router


app = FastAPI()
app.include_router(router, prefix="/api")
Base.metadata.create_all(bind=engine)
