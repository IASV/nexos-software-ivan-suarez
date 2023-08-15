from sqlalchemy import Column, ForeignKey, Integer, Float, Date
from sqlalchemy.orm import relationship

from .database import Base


class Producto(Base):
    __tablename__ = "producto"

    gtin_producto = Column(Integer, primary_key=True)
    precio_unidad = Column(Float, index=True)


class Cliente(Base):
    __tablename__ = "cliente"

    gln_cliente = Column(Integer, primary_key=True)


class Sucursal(Base):
    __tablename__ = "sucursal"

    gln_sucursal = Column(Integer, primary_key=True)
    inventario_id = Column(Integer, ForeignKey("Inventario.id"))
    cliente_id = Column(Integer, ForeignKey("Cliente.gln_cliente"))


class Inventario(Base):
    __tablename__ = "Inventario"

    id = Column(Integer, primary_key=True, index=True)
    producto_id = Column(Integer, ForeignKey("producto.GLN_Producto"))
    inventario_final = Column(Integer, index=True)
    fecha_inventario = Column(Date, index=True)
