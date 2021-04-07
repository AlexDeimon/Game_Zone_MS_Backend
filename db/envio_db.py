from pydantic import BaseModel
class EnvioInDB(BaseModel):
    id_envio: int=0
    id_compra: int
    fecha_envio: str
    fecha_recibido: str

database_envios = {}

generator = {"id":0}

def get_envio(id_envio: str):
    if id_envio in database_envios.keys():
        return database_envios[id_envio]
    else:
        return None

def save_envio(envio_in_db: EnvioInDB):
    generator["id"] = generator["id"] + 1
    envio_in_db.id_envio = generator["id"]
    database_envios[envio_in_db.id_envio]=envio_in_db
    return envio_in_db