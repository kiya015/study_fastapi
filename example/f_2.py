#!/usr/bin/env python
# -*- coding:UTF-8 -*-

"""
@author:huiling.chen
@file: f_2.py
@time: 2021/12/19 15:15 
"""
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None


@app.get("/")
def read_root():
    return {"Hello": "world"}


@app.get("/item/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_id": item_id, "Item": item}


"""
请求：http://127.0.0.1:8000/items/5'返回结果如下:
{
  "item_id": 9,
  "Item": {
    "name": "kiya",
    "price": 3000000,
    "is_offer": true
  }
}
"""
