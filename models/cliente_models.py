from pydantic import BaseModel
class ClientIn(BaseModel):#Estado para autenticado
    id_cliente: str
    nombre_cliente: str

class ClientSearch(BaseModel):#Estado para consulta
    id_cliente: str

class ClientOut(BaseModel):
    id_cliente: str
    nombre_cliente: str
    email: str
    telefono: str
    direccion: str