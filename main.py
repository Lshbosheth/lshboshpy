from fastapi import FastAPI
from routers import items, idCard
# app = FastAPI(openapi_prefix="/api/")
app = FastAPI()
app.include_router(items.router)
app.include_router(idCard.router)
