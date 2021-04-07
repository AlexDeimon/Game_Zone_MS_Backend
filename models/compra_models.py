from pydantic import BaseModel
from datetime import datetime
#Definición de los modelos de estado
class CompraIn(BaseModel):#Estado para autenticado
    id_cliente: str
    id_producto: str
    metodo_pago:str

class CompraSearch(BaseModel):#Estado para consulta
    id_compra: int

class CompraOut(BaseModel):
    id_compra: int
    id_cliente: str
    id_producto: str
    metodo_pago:str
    fecha_compra: datetime