from pydantic import BaseModel
from datetime import date

class ProductoBase(BaseModel):
    precio_unidad: float

class ProductoCreate(ProductoBase):
    pass

class Producto(ProductoBase):
    gtin_producto: int

    class Config:
        orm_mode = True

class Cliente(BaseModel):
    gln_cliente: int

    class Config:
        orm_mode = True

class Sucursal(BaseModel):
    gln_sucursal: int
    inventario_id: int
    cliente_id: int

    class Config:
        orm_mode = True

class Inventario(BaseModel):
    id: int
    producto_id: int
    inventario_final: int
    fecha_inventario: date

    class Config:
        orm_mode = True