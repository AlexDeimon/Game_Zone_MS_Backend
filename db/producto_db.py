from typing import Dict
from pydantic import BaseModel
class ProductInDB(BaseModel):
    id_producto: str
    nombre_producto: str
    precio: int
    cantidad_disponible: int
database_products = Dict[str, ProductInDB]
#Base de datos ficticia
database_products = {
    "XBXGM023": ProductInDB(**{"id_producto":"XBXGM023",
                            "nombre_producto":"Call of duty Cold war",
                            "precio":249900,
                            "cantidad_disponible":25 }),

    "RPCMA042": ProductInDB(**{"id_producto":"RPCMA042",
                            "nombre_producto":"Camisa Star Wars Jedy",
                            "precio":14900,
                            "cantidad_disponible":34 }),

    "SG026": ProductInDB(**{"id_producto":"SG026",
                            "nombre_producto":"Silla Gamer Black Red",
                            "precio":51900,
                            "cantidad_disponible":55 }),

    "ACG003": ProductInDB(**{"id_producto":"ACG003",
                            "nombre_producto":"Collar Gears of war",
                            "precio":5900,
                            "cantidad_disponible":120 }),

    "CFP020": ProductInDB(**{"id_producto":"CFP020",
                            "nombre_producto":"FunkoPop Marcus Fenix",
                            "precio":8900,
                            "cantidad_disponible":70 })                                             
}

def get_product(id_producto: str):
    if id_producto in database_products.keys():
        return database_products[id_producto]
    else:
        return None

def update_product(product_in_db: ProductInDB): 
    database_products[product_in_db.codigo_product] = product_in_db
    return product_in_db
