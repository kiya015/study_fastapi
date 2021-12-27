#!/usr/bin/env python
# -*- coding:UTF-8 -*-

"""
@author:huiling.chen
@file: f_path.py
@time: 2021/12/20 20:51 
"""


from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()
# fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

#可选参数
# @app.get("/items/")
# async def read_item(skip: int = 0, limit: int = 10):
#     return fake_items_db[skip: skip + limit]

# 查询参数类型转换
# @app.get("/items/{item_id}")
# async def read_item(item_id: str, q: Optional[str] = None, short: bool =False):
#     item = {"item_id": item_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update({
#             "description": "This is an amazing item that has a long description"
#         })
#     return item

# 多个路径和查询参数
# @app.get("/users/{user_id}/items/{item_id}")
# async def read_item(user_id: int, item_id: str, q: Optional[str] = None, short: bool = False):
#     item = {"item_id": item_id, "owner_id": user_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update({
#             "description": "This is an amazing item that has a long description"
#         })
#     return item


# 必需查询参数
# @app.get("/items/{item_id}")
# async def read_user_item(item_id: str, needy: str):
#     item = {"item_id": item_id, "needy": needy}
#     return item


# 默认(skip) + 必填(needy) + 可选(q)
# @app.get("/items/{item_id}")
# async def read_user_item(item_id: str, needy: str, skip: str = "test", q: Optional[str] = None):
#     item = {"item_id": item_id, "needy": needy, "skip": skip, "q": q}
#     return item

# 请求体
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


@app.post("/items")
async def create_item(item: Item):
    return item