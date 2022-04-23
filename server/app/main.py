from fastapi import FastAPI
from .database.engine import Base, engine

from .routers import router

app = FastAPI()

app.include_router(router)

Base.metadata.create_all(bind=engine)


@app.get("/")
async def root():
    return {"message": "Hello World"}
