TABLES_TO_CREATE = {

    "tabla_departamento" : """
                    
                    CREATE TABLE  IF NOT EXISTS departamento (
                    
                    	id int,
                    	name_department varchar (30)

                    )
            
                """,
    
    "tabla_job" : """
                
                    CREATE TABLE  IF NOT EXISTS job (
                    
                    	id int,
                    	name_job varchar (30)

                    )
                    
                """,
    
    "tabla_empleados" : """
                    

                    CREATE TABLE IF NOT EXISTS empleados (

                        id_empleado int,
                        name Varchar(30),
                        datetime varchar(30),
                        id_departamento int,
                        id_job int
                    )
                    
               
                """,
    
    "tabla_users" : """

                    CREATE TABLE IF NOT EXISTS users (
                        email Varchar(30),
                        password varchar(100)
                    )
                    
            """,
    
    "tabla_log" : """

                    CREATE TABLE IF  NOT EXISTS log (
                        fecha Varchar(30),
                        usuario varchar(100),
                        hora varchar (30),
                        estado varchar (30)
                    )
            
                """

}