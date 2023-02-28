from utilities.conexion.connection import engine
from utilities.models.TABLES import TABLES_TO_CREATE
import pandas as pd
from datetime import datetime




def crear_tablas ():

    cursor = engine.cursor() 
    for tabla in TABLES_TO_CREATE.values():
            cursor.execute(tabla)
    cursor.close()
            
def cargar_tabla (nombre_tabla:str, valores : list):

    valor = lambda x : "id" if nombre_tabla!= "empleados" else "id_empleado"
    df = pd.DataFrame(valores).set_index(valor(nombre_tabla))
    print (df.head())
    df.to_sql (nombre_tabla,con=engine,if_exists="replace")


def insert_log (usuario,estado):
     cursor = engine.cursor()
     fecha = datetime.now().strftime("%Y/%m/%d, %H:%M:%S")
     cursor.execute("INSERT INTO log (usuario,fecha,estado) VALUES (?,?,?)",(usuario,fecha,estado))
     engine.commit()
     cursor.close()



 
