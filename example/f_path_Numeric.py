#!/usr/bin/env python
# -*- coding:UTF-8 -*-

"""
@author:huiling.chen
@file: f_path_Numeric.py
@time: 2021/12/28 15:17 
"""
from fastapi import FastAPI, Path, Body
from pydantic import BaseModel
from typing import Optional


app = FastAPI()


# @app.get("/items/{item_id}")
# async def read_items(q: str, item_id: int = Path(..., title="The ID of the item to get")):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results


# gt: greater than  大于
# ge: greater than or equal 大于等于
# lt: less than 小于
# le: less than or equal 小于等于
# @app.get("/items/{items_id}")
# async def read_items(*, items_id: int = Path(..., title="the id of the items to get", ge=2, le=20), q: str):
#     results = {"item_id": items_id}
#     if q:
#         results.update({"q": q})
#     return results

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


class User(BaseModel):
    username: str
    full_name: Optional[str] = None


# Multiple body parameters¶
# *: * 后的参数都应为关键字参数
# item 对类Item, user 对User
# @app.put("/items/{items_id}")
# async def read_items(*, items_id: int = Path(..., title="the id of the items to get", ge=2, le=20),
#                      q: Optional[str] = None, item: Optional[Item] = None,
#                      user: User):
#     results = {"item_id": items_id}
#     if q:
#         results.update({"q": q})
#     if item:
#         results.update({"item": item})
#     if user:
#         results.update({"user": user})
#     return results
