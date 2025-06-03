from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class VentaCreate(BaseModel):
    producto_id: int
    cantidad: int
    total: float

class VentaOut(VentaCreate):
    id: int
    fecha: datetime

    class Config:
        orm_mode = True