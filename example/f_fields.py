#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @file    : f_fields.py
# @Author  : kiya
# @Time    : 2021/12/28 23:48
from typing import Optional, List, Set
from fastapi import Body, FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

# Set[str] = set() 会去重
class Item(BaseModel):
    name: str
    description: Optional[str] = Field(None, title="the description of the item")
    price: float = Field(None, ge=0, description="The price must be greater than zero")
    tax: Optional[float] = None
    # tags: list = []
    # tags: List[str] = [
    tags: Set[str] = set()

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item=Body(..., embed=True)):
    results = {"item_id": item_id, "item": item}
    return results