from typing import Optional
from sqllite_db import sqllite_db

from fastapi import FastAPI
import uvicorn

app = FastAPI()
db = sqllite_db() 
conn = db.get_connection()



@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.on_event("shutdown")
def database_disconnect():
    conn.close()


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    query = "SELECT * FROM ESTATE limit = {number}".format(number = item_id)
    c = conn.cursor()
    results = await c.fetch_all(query= query)
    return results

if __name__== '__main__':
    uvicorn.run(app, port = 8000, host= "0.0.0.0")