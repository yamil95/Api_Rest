from sqlalchemy import  ForeignKey, Column, Integer, String
import sys
from utilities.conexion.connection import Base,engine


class Empleados(Base):
   __tablename__ = 'empleado'
   id = Column (Integer,primary_key=True,autoincrement=True)
   id_empleado = Column(Integer)
   name = Column(String)
   datetime = Column(String)
   departamento_id = Column(Integer)
   job_id = Column(Integer)
   
   

class Departamentos(Base):
   __tablename__ = 'departamento'
   id = Column (Integer,primary_key=True,autoincrement=True)
   id_departamentos = Column(Integer)
   name_departamento = Column(String)

class Jobs(Base):
   __tablename__ = 'job'
   id = Column (Integer,primary_key=True,autoincrement=True)
   id_jobs= Column(Integer)
   name_job = Column(String)

class Users(Base):
   __tablename__ = 'user'
   id = Column (Integer,primary_key=True,autoincrement=True)
   email= Column(String)
   password = Column(String)
   


Base.metadata.create_all(engine)