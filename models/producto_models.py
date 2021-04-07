from pydantic import BaseModel

class ProductIn(BaseModel):
    id_producto: str

class ProductSearch(BaseModel):
    id_producto: str

class ProductOut(BaseModel):
    id_producto: str
    nombre_producto: str
    precio: int
    cantidad_disponible: int