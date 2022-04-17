from fastapi import FastAPI
from .database.engine import get_db, Base, engine

app = FastAPI()

Base.metadata.create_all(bind=engine)
get_db()


@app.get("/")
async def root():
    return {"message": "Hello World"}
