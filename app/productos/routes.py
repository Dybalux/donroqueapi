from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .models import Productos
from .schemas import ProductoCreate, ProductoUpdate, ProductoOut
from db import get_db,Base
from typing import List

router = APIRouter(prefix="/forrajeria", tags=["Productos"])

@router.post("/crearproducto")
def crear_producto(producto: ProductoCreate, db: Session = Depends(get_db)):
    nuevo_producto = Productos(
        nombre=producto.nombre,
        precio=producto.precio,
        stock=producto.stock,
    )
    db.add(nuevo_producto)
    db.commit()
    db.refresh(nuevo_producto)
    return {"mensaje": "Producto creado exitosamente", "producto_id": nuevo_producto.id}

@router.put("/producto/{producto_id}")
def actualizar_producto(producto_id: int, producto: ProductoUpdate, db: Session = Depends(get_db)):
    producto_db = db.query(Productos).filter(Productos.id == producto_id).first()
    if not producto_db:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    # Actualiza solo los campos que vienen en el request (no None)
    if producto.nombre is not None:
        producto_db.nombre = producto.nombre
    if producto.precio is not None:
        producto_db.precio = producto.precio
    if producto.stock is not None:
        producto_db.stock = producto.stock

    db.commit()
    db.refresh(producto_db)

    return {"mensaje": "Producto actualizado exitosamente", "producto": producto_db}
@router.delete("/producto/{producto_id}")
def eliminar_producto(producto_id: int, db: Session = Depends(get_db)):
    producto_db = db.query(Productos).filter(Productos.id == producto_id).first()
    if not producto_db:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    db.delete(producto_db)
    db.commit()
    
    return {"mensaje": f"Producto con ID {producto_id} eliminado exitosamente"}

@router.get("/productos", response_model=List[ProductoCreate])
def obtener_productos(db: Session = Depends(get_db)):
    productos = db.query(Productos).all()
    return productos

@router.get("/producto/{producto_id}", response_model=ProductoOut)
def obtener_producto_por_id(producto_id: int, db: Session = Depends(get_db)):
    producto = db.query(Productos).filter(Productos.id == producto_id).first()
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto