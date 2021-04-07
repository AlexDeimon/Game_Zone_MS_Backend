from typing import Dict
from pydantic import BaseModel #Parametros para definir validación de datos
class AdminInDB(BaseModel):
    username: str
    password: str

#DB ficcticia
database_Admins = Dict[str, AdminInDB]
database_Admins = {                                      #instanciando mediante un diccionario
    "AlexDeimon": AdminInDB(**{"username":"AlexDeimon",
    "password":"1234"
    }),
    "Mystique": AdminInDB(**{"username":"Mystique",
    "password":"5678"
    })
}
#Obtener admin
def get_Admin(username: str):
    if username in database_Admins.keys():
        return database_Admins[username]
    else:
        return None

def update_Admin(Admin_in_db: AdminInDB): #Se recibe un dato admin_in_db de tipo AdminInDB
    database_Admins[Admin_in_db.username] = Admin_in_db
    return Admin_in_db