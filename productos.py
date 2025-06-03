from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base
from db import engine 
Base = declarative_base()

class Productos(Base):
    __tablename__="productos"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    precio = Column(Float, nullable=False)
    stock = Column(Float, nullable=False)

Base.metadata.create_all(engine)