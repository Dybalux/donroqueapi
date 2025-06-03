from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from db import engine,Base

class Venta(Base):
    __tablename__ = "ventas"
    id = Column(Integer, primary_key=True, index=True)
    producto_id = Column(Integer, ForeignKey("productos.id"), nullable=False)
    cantidad = Column(Float, nullable=False)
    total = Column(Float, nullable=False)
    fecha = Column(DateTime, default=datetime.utcnow)

Venta.producto = relationship("Productos", back_populates="ventas")
Base.metadata.create_all(engine)