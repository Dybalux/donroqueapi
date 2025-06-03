from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import get_db,Base
from .models import Venta
from .schemas import VentaCreate, VentaOut
from typing import List

router = APIRouter(prefix="/forrajeria",tags=["ventas"])

@router.post("/",response_model=VentaOut)
def registrar_venta(venta: VentaCreate, db: Session = Depends(get_db)):
    nueva_venta = Venta(
        **venta.dict() 
    )
    db.add(nueva_venta)
    db.commit()
    db.refresh(nueva_venta)
    return nueva_venta

@router.get("/", response_model=List[VentaOut])
def obtener_ventas(db: Session = Depends(get_db)):
    ventas = db.query(Venta).all()
    return ventas