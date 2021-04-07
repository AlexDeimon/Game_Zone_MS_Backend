from typing import Dict
from pydantic import BaseModel

class ClientInDB(BaseModel):
    id_cliente: str
    nombre_cliente: str
    email: str
    telefono: str
    direccion: str

database_clients = Dict[str, ClientInDB]

#Base de datos ficticia
database_clients = {
    "11111": ClientInDB(**{"id_cliente":"11111",
                            "nombre_cliente":"Winston Leonard Spencer Churchill",
                            "email":"winston.churchill@gmail.com",
                            "telefono":"7893214568",
                            "direccion":"Cra 21 No 92-60"}),

    "22222": ClientInDB(**{"id_cliente":"22222",
                            "nombre_cliente":"Dwight David Eisenhower",
                            "email":"david.eisenhower@gmail.com",
                            "telefono":"3578521596",
                            "direccion":"Cra 32 No 20-21"}),

    "33333": ClientInDB(**{"id_cliente":"33333",
                            "nombre_cliente":"Omar Nelson Bradley",
                            "email":"omar.bradley@gmail.com",
                            "telefono":"4863217592",
                            "direccion":"Cra 22 No 26-03"}),

    "44444": ClientInDB(**{"id_cliente":"44444",
                            "nombre_cliente":"Erwin Johannes Eugen Rommel",
                            "email":"erwin.rommel@gmail.com",
                            "telefono":"5987432175",
                            "direccion":"Cra 20 No 21-02"}),

    "55555": ClientInDB(**{"id_cliente":"55555",
                            "nombre_cliente":"Kurt Arthur Benno Student",
                            "email":"kurt.student@gmail.com",
                            "telefono":"3574159845",
                            "direccion":"Cra 21 No 26-03"})
}

def get_client(id_cliente: str):
    if id_cliente in database_clients.keys():
        return database_clients[id_cliente]
    else:
        return None

def update_client(client_in_db: ClientInDB):#Se recibe un dato client_in_db de tipo UserInDB
    database_clients[client_in_db.id_cliente] = client_in_db
    return client_in_db