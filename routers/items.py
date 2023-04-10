from fastapi import APIRouter, Query
from typing import List, Union

router = APIRouter(
    prefix="/items",
    tags=["items"],
    responses={404: {"description": "Not found"}},
)


@router.get("")
async def read_items(q: Union[List[str], None] = Query(default=None)):
    query_items = {"q3": q}
    return query_items
