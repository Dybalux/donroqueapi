from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base,  relationship
from db import engine 
from db import Base

class Productos(Base):
    __tablename__ = "productos"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    precio = Column(Float, nullable=False)
    stock = Column(Float, nullable=False)

from app.ventas.models import Venta
from sqlalchemy.orm import relationship
Productos.ventas = relationship("Venta", back_populates="producto")
Base.metadata.create_all(engine)