#from sqlalchemy import create_engine
#from sqlalchemy.ext.asyncio import AsyncSession
#from sqlalchemy.ext.asyncio import create_async_engine
#from sqlalchemy.orm import sessionmaker
#import os
import sqlite3
"""
proposito : Esta porcion de codigo se utilizo cuando la base de datos estaba en azure , por motivos de infra
            voy a utilizar una db local para el desarrollo de la aplicacion 


server = os.getenv("server") #'yamilpsg.postgres.database.azure.com'#"servidoryamil.database.windows.net"
database = os.getenv("database")  #'yamilpruebas' #"yamildb"
username =  os.getenv ("user")#'yamil_ps@yamilpsg'#"rootyamil"
password = os.getenv("password") #"Yferru9259"

DATABASE_URL = f"postgresql+asyncpg://{username}:{password}@{server}:5432/{database}"
engine = create_async_engine(DATABASE_URL, echo=True)
async_session = sessionmaker( engine, class_=AsyncSession, expire_on_commit=False)
"""
engine = sqlite3.connect("globant.db")
