from fastapi import FastAPI, Query, Path
from enum import Enum
from typing import List, Union
from pydantic import BaseModel
app = FastAPI(openapi_url="/openapi.json")


@app.get("/items/")
async def read_items(q: Union[List[str], None] = Query(default=None)):
    query_items = {"q3": q}
    return query_items
