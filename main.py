from fastapi import FastAPI
from pydantic import BaseModel


item_master = {
                1 : "Mango",
                2 : "Apple",
                3 : "Orange",
                4 : "Banana",
                5 : "Guava"
            }


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None




app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items")
async def items():
    return {"Items": f"List of Items{item_master}"}

@app.get("/items/{item_id}")
async def get_item(item_id: int, short: bool):
    if short==False:
        return "This is a Long Description"
    else:
        return {"Item": item_master[item_id]}


@app.post("/items")
async def create_item(item: Item):
    return item
   
