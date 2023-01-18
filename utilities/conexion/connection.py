from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
import os

server = os.getenv("server") #'yamilpsg.postgres.database.azure.com'#"servidoryamil.database.windows.net"
database = os.getenv("database")  #'yamilpruebas' #"yamildb"
username =  os.getenv ("user")#'yamil_ps@yamilpsg'#"rootyamil"
password = os.getenv("password") #"Yferru9259"

""" 
driver = '{ODBC Driver 17 for SQL Server}'

odbc_str = 'DRIVER='+driver+';SERVER='+server+';PORT=1433;UID='+username+';DATABASE='+ database + ';PWD='+ password
connect_str = 'mssql+pyodbc:///?odbc_connect='+ odbc_str
engine = create_engine(connect_str,pool_size=5, pool_recycle=3600)

"""

DATABASE_URL = f"postgresql+asyncpg://{username}:{password}@{server}:5432/{database}"



engine = create_async_engine(DATABASE_URL, echo=True)
async_session = sessionmaker( engine, class_=AsyncSession, expire_on_commit=False)
