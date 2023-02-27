from utilities.conexion.connection import engine
from utilities.models.TABLES import TABLES_TO_CREATE
import pandas as pd




def crear_tablas ():

    cursor = engine.cursor() 
    for tabla in TABLES_TO_CREATE.values():
            cursor.execute(tabla)
    cursor.close()
            
def cargar_tabla (nombre_tabla:str, valores : list):

    df = pd.DataFrame(valores).set_index("id")
    df.to_sql (nombre_tabla,con=engine,if_exists='append')

 
