#!/usr/bin/env python
# -*- coding:UTF-8 -*-

"""
@author:huiling.chen
@file: f_request_body.py 
@time: 2021/12/27 15:39 
"""
from typing import Optional, List
from fastapi import FastAPI, Query
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Optional[str] = "An optional description"
    price: float
    tax: Optional[float] = None


app = FastAPI()


# @app.post("/items/{id}")
# async def creat_item(id: str, item: Item):
#     print(item.name.capitalize())
#     return item


# """
# {
#   "name": "kiya",
#   "description": "string....",
#   "price": 698.5,
#   "tax": 98.6
# }
# """

# Request body + path + query parameters
# @app.post("/items/{id}")
# async def create_item(id, item: Item, q: Optional[str] = None):
#     print(dir(item))
#     item_dict = {'item_id': id, "item_dic": item.dict()}
#     if item.tax:
#         price_with_tax = item.price + item.tax
#         item_dict.update({"price_with_tax": price_with_tax})
#     if q:
#         item_dict.update({"q": q})
#     return item_dict


# Additional validation（校验）
# @app.get("/items/")
# async def read_items(q: Optional[str] = Query(None, max_length=10)):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

# Query(None, max_length=10)  限制长度为10


# Add regular expressions --> 添加正则表达式
# @app.get("/items/")
# async def read_items(q: Optional[str] = Query(None, max_length=10, min_length=1, regex="^[A-z0-9]")):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

#  set default parameters
# @app.get("/items/")
# async def read_items(q: Optional[str] = Query("this is default", max_length=10, min_length=1, regex="^[A-z0-9]")):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

# Make it required
# @app.get("/items")
# async def read_items(q: str = Query(..., min_length= 3)):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

# Query parameter list / multiple values
# @app.get("/items/")
# async def read_items(q: Optional[List[str]] = Query(None)):
#     query_items = {"q": q}
#     return query_items

# http://127.0.0.1:8000/items/?q=22,22
# """{
# "q": [
# "22,22"
# ]
# }"""

# Query parameter list / multiple values with defaults
# @app.get("/items/")
# async def read_items(q: List[str] = Query(["Foo", "Bar"])):
#     query_items = {"q": q}
#     return query_items

# Using list
# @app.get("/items/")
# async def read_items(q: list = Query([])):
#     query_item = {"q": q}
#     return query_item


# Declare more metadata (申明更多元数据) deprecated（弃用）
# @app.get("/items/")
# async def read_items(q: Optional[str] = Query(None, min_length=3, title="6666666666", deprecated=True,
#                                               alias="item-query", description="Query string for the items")):
#     results = {"item": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results
