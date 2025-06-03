from pydantic import BaseModel
from typing import Optional

class ProductoCreate(BaseModel):
    nombre: str
    precio: float
    stock: float

class ProductoUpdate(BaseModel):
    nombre: Optional[str] = None
    precio: Optional[float] = None
    stock: Optional[float] = None

class ProductoOut(ProductoCreate):
     id: int

     class Config:
         orm_mode = True