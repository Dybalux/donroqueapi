from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.productos.models import Productos
from db import get_db
from app.productos.routes import router as productos_router
from app.ventas.routes import router as ventas_router

app = FastAPI(
    title="Don Roque Forrajeria API",
    docs_url="/documentacion",
    redoc_url=None,
    openapi_url="/openapi.json"
)

app.include_router(productos_router)
app.include_router(ventas_router)