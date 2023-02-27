from utilities.conexion.connection import engine
from sqlalchemy.sql import text
from utilities.conexion.connection import async_session




tabla_departamento = """
                    

                    CREATE TABLE  IF NOT EXISTS public.departamento (
                    
                    	id int,
                    	nombre_departamento varchar (30)

                    )
                    
                    
                    
                """

tabla_job = """
                    


                   
                    CREATE TABLE  IF NOT EXISTS public.job (
                    
                    	id int,
                    	nombre_job varchar (30)

                    )
                    
                    
                    
                    
                """
tabla_empleados = """
                    

                    CREATE TABLE IF NOT EXISTS public.empleados (

                        id_empleado int,
                        name Varchar(30),
                        datetime varchar(30),
                        id_departamento int,
                        id_job int
                    )
                    
               
                """

tabla_users = """
                    
                    

                    CREATE TABLE IF NOT EXISTS public.users (
                        email Varchar(30),
                        password varchar(100)
                    )
                    
            """


tabla_log = """
                    

                    CREATE TABLE IF  NOT EXISTS public.log (
                        fecha Varchar(30),
                        usuario varchar(100),
                        hora varchar (30),
                        estado varchar (30)
                    )
                    

                """

lista_tablas = [tabla_departamento,tabla_empleados,tabla_job,tabla_users,tabla_log]


async def crear_tablas ():

    async with async_session() as session:
        for tabla in lista_tablas:

            await session.execute(text(tabla))
            await session.commit()
    

async def cargar_tabla (nombre_tabla:str, valores : list):

    async with async_session() as session:

        for elemento in valores : 

            id = elemento["id"]
            name = elemento["name"]
            date = elemento["datetime"]
            departamento_id = elemento["departamento_id"]
            job_ib = elemento["job_id"]

            insert = f"""
                INSERT INTO {nombre_tabla}
                
                (id_empleado,name,datetime,id_departamento,id_job)
                
                VALUES 
                
                ({id}, \'{name}\',\'{date}\',{departamento_id},{job_ib})


            """

            await session.execute(text(insert))
            await session.commit()





"""
def crear_tablas ():
    conexion_db = engine.connect().execution_options(autocommit = True)    

    for tabla in lista_tablas:

        conexion_db.execute(text(tabla))
    
    conexion_db.close()

def cargar_tabla (nombre_tabla : str , valores : list):

   
    conexion = engine.connect().execution_options(autocommit = True)

    for elemento in valores :

        id_job = elemento["id"]
        name_job = elemento["name_job"]
        insert = f"""
        #        INSERT INTO {nombre_tabla}
        #        (id,nombre_job)
        #        
        #        VALUES ({id_job}, \'{name_job}\')


        #    """
        
        
        #conexion.execute(text (insert))
    
    
    #conexion.close()

 
