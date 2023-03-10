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

    
    

    if nombre_tabla != "empleados":
         cursor = engine.cursor()
         for valor in valores:
             valor = tuple (valor.values() )
             cursor.execute(f"INSERT OR REPLACE INTO {nombre_tabla} (id,name) VALUES (?,?)",valor)
             engine.commit()
    
    
    else : 
        cursor = engine.cursor()
        for valor in valores:
            valor = tuple (valor.values() )
            cursor.execute(f"INSERT OR REPLACE INTO {nombre_tabla} (id_empleado,name,datetime,id_departamento,id_job) VALUES (?,?,?,?,?)",valor)
            engine.commit()
    
    cursor.close() 
            

    
    


def insert_log (usuario,estado):
     cursor = engine.cursor()
     fecha = datetime.now().strftime("%Y/%m/%d, %H:%M:%S")
     cursor.execute("INSERT INTO log (usuario,fecha,estado) VALUES (?,?,?)",(usuario,fecha,estado))
     engine.commit()
     cursor.close()



 
