from db.cliente_db import ClientInDB
from db.cliente_db import update_client, get_client, database_clients
from db.admin_db import AdminInDB
from db.admin_db import get_Admin, update_Admin, database_Admins
from db.compra_db import CompraInDB
from db.compra_db import save_compra, get_compra, database_compras
from db.envio_db import EnvioInDB
from db.envio_db import save_envio, get_envio ,database_envios
from db.producto_db import  ProductInDB
from db.producto_db import get_product, update_product, database_products

from models.admin_models import AdminIn, AdminOut
from models.cliente_models import ClientSearch, ClientIn, ClientOut
from models.compra_models import CompraSearch, CompraIn, CompraOut
from models.producto_models import ProductSearch, ProductIn, ProductOut
from models.envio_models import EnvioSearch, EnvioIn, EnvioOut

import datetime
from fastapi import FastAPI
from fastapi import HTTPException
api = FastAPI()

#Verificar usuario
@api.post("/admin/auth/")
async def auth_admin(admin_in: AdminIn):
    admin_in_db = get_Admin(admin_in.username)
    if admin_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")
    if admin_in_db.password != admin_in.password:
        return {"Usuario o contraseña incorrectos"}
    return {"¡Acceso exitoso! ¡Bienvenido "+admin_in.username+"!"}

#mensaje de bienvenida del usuario
@api.get("/home/{username}")
async def get_username(username: str):
    Admin_in_db = get_Admin(username)
    if Admin_in_db == None:
        raise HTTPException(status_code=404,detail="El usuario no existe")
    Admin_out = AdminOut(**Admin_in_db.dict())
    return {"Bienvenido "+username}

#listar clientes
@api.get("/clients/")
async def get_all_clients():
    return database_clients

#Consultar Cliente
@api.post("/client/search/")
async def search_client(client_search: ClientSearch):
    client_in_db = get_client(client_search.id_cliente)
    if client_in_db == None:
        return {"El cliente no existe"}
    if client_in_db.id_cliente == client_search.id_cliente:
        return client_in_db

#Actualizar Cliente
@api.put("/client/update/")
async def update_client(client_in_db: ClientInDB):
    try:
        if database_clients[client_in_db.id_cliente]:
            database_clients.update({client_in_db.id_cliente:client_in_db})
            return {"El cliente fue actualizado con exito"}
    except:
        return {"El cliente que intenta actualizar no existe"}

#Agregar Cliente
@api.post("/client/new/")
async def add_client(client_in_db: ClientInDB):
    if client_in_db.id_cliente not in database_clients:
        database_clients[client_in_db.id_cliente]=client_in_db
        return {"El cliente fue creado con exito"}
    else:
        return {"El cliente ya existe"}

#Eliminar Cliente
@api.delete("/client/delete/")
async def delete_client(client_in_db: ClientSearch):
    try:
        if database_clients[client_in_db.id_cliente]:
            database_clients.pop(client_in_db.id_cliente)
            return {"El cliente fue borrado con exito"}
    except:
        return {"El cliente que intenta borrar no existe"}

#listar compras
@api.get("/compras/")
async def get_all_compras():
    return database_compras

#Consultar Compra
@api.post("/compra/search/")
async def search_compra(compra_search: CompraSearch):
    compra_in_db = get_compra(compra_search.id_compra)
    if compra_in_db == None:
        return {"La compra no existe"}
    if compra_in_db.id_compra == compra_search.id_compra:
        return compra_in_db

#Agregar Compra
@api.post("/compra/new/")
async def add_comrpa(compra_in: CompraInDB):
    client_in_db = get_client(compra_in.id_cliente)
    product_in_db = get_product(compra_in.id_producto)
    if client_in_db == None:
        raise HTTPException(status_code=404,detail="El Cliente no existe")

    if product_in_db == None:
        raise HTTPException(status_code=404,detail="El Producto no existe")

    if product_in_db.cantidad_disponible == 0 :
        raise HTTPException(status_code=400,detail="El producto está agotado")
    
    product_in_db.cantidad_disponible = product_in_db.cantidad_disponible - 1 
    update_product(product_in_db)
    compra_in_db = CompraInDB(**compra_in.dict())
    compra_in_db = save_compra(compra_in_db)
    compra_out = CompraOut(**compra_in_db.dict())
    return {"La compra fue registrada con exito"}

#Actualizar Compra
@api.put("/compra/update/")
async def update_compra(compra_in_db: CompraInDB):
    try:
        if database_compras[compra_in_db.id_compra]:
            database_compras.update({compra_in_db.id_compra:compra_in_db})
            return {"La compra fue actualizada con exito"}
    except:
        return {"La compra que intenta actualizar no existe"}

#Eliminar Compra
@api.delete("/compra/delete/")
async def delete_compra(compra_in_db: CompraSearch):
    try:
        if database_compras[compra_in_db.id_compra]:
            database_compras.pop(compra_in_db.id_compra)
            return {"La compra fue borrada con exito"}
    except:
        return {"La compra que intenta borrar no existe"}

#listar productos
@api.get("/products/")
async def get_all_products():
    return database_products

#Consultar Producto
@api.post("/product/search/")
async def search_product(product_search: ProductSearch):
    product_in_db = get_product(product_search.id_producto)
    if product_in_db == None:
        return {"El producto no se encuentra en el inventario"}
    if product_in_db.id_producto== product_search.id_producto:
        return product_in_db

#Actualizar Product
@api.put("/product/update/")
async def update_product(product_in_db: ProductInDB):
    try:
        if database_products[product_in_db.id_producto]:
            database_products.update({product_in_db.id_producto:product_in_db})
            return {"El producto fue actualizado con exito"}
    except:
        return {"El producto que intenta actualizar no existe"}

#Agregar Product
@api.post("/product/new/")
async def add_product(product_in_db: ProductInDB):
    if product_in_db.id_producto not in database_products:
        database_products[product_in_db.id_producto]=product_in_db
        return {"El producto fue añadido al inventario"}
    else:
        return {"El producto ya está en el inventario"}

#Eliminar Product
@api.delete("/product/delete/")
async def delete_product(product_in_db: ProductSearch):
    try:
        if database_products[product_in_db.id_producto]:
            database_products.pop(product_in_db.id_producto)
            return {"El producto fue removido del inventario"}
    except:
        return {"El producto que intenta borrar no está en el inventario"}

#listar envios
@api.get("/envios/")
async def get_all_envios():
    return database_envios

#Consultar envios
@api.post("/envio/search/")
async def search_envio(envio_search: EnvioSearch):
    envio_in_db = get_envio(envio_search.id_envio)
    if envio_in_db == None:
        return {"El envio no existe"}
    if envio_in_db.id_envio == envio_search.id_envio:
        return envio_in_db

#Agregar envio
@api.post("/envio/new/")
async def add_envio(envio_in: EnvioInDB):
    compra_in_db = get_compra(envio_in.id_compra)
    if compra_in_db == None:
        raise HTTPException(status_code=404,detail="La compra para este envio no existe")
    
    envio_in_db = EnvioInDB(**envio_in.dict())
    envio_in_db = save_envio(envio_in_db)
    envio_out = EnvioOut(**envio_in_db.dict())
    return {"El envio fue registrado con exito"}

#Actualizar envio
@api.put("/envio/update/")
async def update_envio(envio_in_db: EnvioInDB):
    try:
        if database_envios[envio_in_db.id_envio]:
            database_envios.update({envio_in_db.id_envio:envio_in_db})
            return {"El envio fue actualizado con exito"}
    except:
        return {"El envio que intenta actualizar no existe"}

#Eliminar envio
@api.delete("/envio/delete/")
async def delete_envio(envio_in_db: EnvioSearch):
    try:
        if database_envios[envio_in_db.id_envio]:
            database_envios.pop(envio_in_db.id_envio)
            return {"El envio fue borrado con exito"}
    except:
        return {"El envio que intenta borrar no existe"}