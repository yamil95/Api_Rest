TABLES_TO_CREATE = {

    "tabla_departamento" : """
                    
                    CREATE TABLE  IF NOT EXISTS departamento (
                    
                    	id int PRIMARY KEY,
                    	name varchar (30)

                    )
            
                """,
    
    "tabla_job" : """
                
                    CREATE TABLE  IF NOT EXISTS job (
                    
                    	id int PRIMARY KEY,
                    	name varchar (30)

                    )
                    
                """,
    
    "tabla_empleados" : """
                    

                    CREATE TABLE IF NOT EXISTS empleados (

                        id_empleado int PRIMARY KEY,
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
                        usuario varchar(100),
                        fecha Varchar(30),
                        estado varchar (30)
                    )
            
                """

}