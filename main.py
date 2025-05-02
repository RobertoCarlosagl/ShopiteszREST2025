# This is a sample Python script.
from importlib import reload

# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#from fast api import FastApi
from fastapi import FastAPI
import uvicorn

from dao.database import Conexion
from routers import pedidosRouter, productosRouter, usuariosRouter
#crear una instacia de la clase FastApi
app = FastAPI()
app.include_router(pedidosRouter.router)
app.include_router(productosRouter.router)
app.include_router(usuariosRouter.router)
@app.get("/")
async def home():
    salida={"mensaje": "Bienvenido a la PEDIDOSREST"}
    return salida

@app.on_event("startup")
async def startup():
    print("Conexion con MongoBD")
    conexion=Conexion()
    app.conexion=conexion
    app.db=conexion.getDB()

@app.on_event("shutdown")
async def shutdown():
    print("Cerrando la conexion")
    app.conexion.cerrar()


#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    #print(f'Hi, {name}')  # Press F9 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print_hi('PyCharm')
    uvicorn.run("main:app",host= '127.0.0.1', reload=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


