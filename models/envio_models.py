from pydantic import BaseModel
#Definición de los modelos de estado
class EnvioIn(BaseModel):#Estado para autenticado
    id_compra: int
    fecha_envio: str
    fecha_recibido: str
    
class EnvioSearch(BaseModel):#Estado para consulta
    id_envio: int

class EnvioOut(BaseModel):
    id_envio: int
    id_compra: int
    fecha_envio: str
    fecha_recibido: str
