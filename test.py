from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str = None  
    price: float
    tax: float = None  

items: dict[int, Item] = {}

@app.delete("/delete/{item_id}")
async def delete_item_by_id(item_id: int):
    removed_item = items.pop(item_id, None)
    if removed_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return { 'details' : f"Item with ID {item_id}"}

@app.delete("/delete")
async def delete_all_items():
    items.clear()
    return { 'details' :"All items have been cleared"}
