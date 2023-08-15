from sqlalchemy.orm import Session
from . import models, schemas


def create_producto(db: Session, producto: schemas.Producto):
    db_producto = models.Producto(
        gtin_producto=producto.gtin_producto, precio_unidad=producto.precio_unidad
    )
    db.add(db_producto)
    db.commit()
    db.refresh(db_producto)
    return db_producto


def create_cliente(db: Session, cliente: schemas.Cliente):
    db_cliente = models.Cliente(gtin_cliente=cliente.gln_cliente)
    db.add(db_cliente)
    db.commit()
    db.refresh(db_cliente)
    return db_cliente
