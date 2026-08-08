from fastapi import FastAPI
from db import engine, Base
from routers import router


app = FastAPI()
app.include_router(router, prefix="/api")
Base.metadata.create_all(bind=engine)
