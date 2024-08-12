from typing import Union
import json
from fastapi import FastAPI
from datos import obtenallproductos,insertanewproducto,actualizainventario,ventasxdia
from pydantic import BaseModel
app = FastAPI()


class Item(BaseModel):


    id: int
    marca: str
    inventario: str
    fecha: str
    producto: str
    nuevo: int
    precio: int


@app.get("/getproductos")
def leerproductos():
    productos = obtenallproductos()
    return productos


@app.post("/insertproducto")
def  insertproductos(id: int,marca:str,producto: str,fecha: str):
    respuesta = insertanewproducto(id,marca,producto,fecha)
    return respuesta


@app.put("/actualizainventario")
def update_item(id: int,marca: str,inventario: str,fecha: str,producto: str,nuevo: int):
    resultado = actualizainventario(id,marca,inventario,fecha,producto, nuevo)
    return resultado



@app.delete("/deleteinventario")
def delete(id: int,marca: str,inventario: str,fecha: str,producto: str,nuevo: int):
    resultado = actualizainventario(id,marca,inventario,fecha,producto, nuevo)
    return resultado


@app.get("/ventas/aldia")
def obtenventas(id: int,marca: str,precio: int,inventario: str,fecha: str,producto: str):
    resultado = ventasxdia(id,marca,producto,precio,inventario,fecha)
    return 'ok'