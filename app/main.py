from typing import Optional
from sqllite_db import sqllite_db
from databases import Database
from fastapi import FastAPI
import uvicorn

database = Database("sqlite:///metroscubicos.sqlite")

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.on_event("startup")
async def database_connect():
    await database.connect()


@app.on_event("shutdown")
async def database_disconnect():
    await database.disconnect()



@app.get("/items/{item_id}")
async def read_item(item_id: int):
    query = "SELECT * FROM ESTATE limit {number}".format(number = item_id)
    results = await database.fetch_all(query=query)
    return results

if __name__== '__main__':
    uvicorn.run(app, port = 8000, host= "0.0.0.0")