from datetime import datetime
from pydantic import BaseModel
class CompraInDB(BaseModel):
    id_compra: int=0
    id_cliente: str
    id_producto: str
    metodo_pago:str
    fecha_compra: datetime = datetime.now()

database_compras = {}
generator = {"id":0}

def get_compra(id_compra: int):
    if id_compra in database_compras.keys():
        return database_compras[id_compra]
    else:
        return None

def save_compra(compra_in_db: CompraInDB):
    generator["id"] = generator["id"] + 1
    compra_in_db.id_compra = generator["id"]
    database_compras[compra_in_db.id_compra]=compra_in_db
    return compra_in_db