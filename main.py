from fastapi import FastAPI
from routers import items, idCard, dbtest
import os

mode = os.environ.get('mode')

if mode == 'prod':
    app = FastAPI(openapi_prefix="/api/")
else:
    app = FastAPI()
app.include_router(items.router)
app.include_router(idCard.router)
app.include_router(dbtest.router)
