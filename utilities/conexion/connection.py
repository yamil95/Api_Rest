from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import text


server = "servidoryamil.database.windows.net"
database = "yamildb"
username = "rootyamil"
password = "Yferru9259"

driver = '{ODBC Driver 17 for SQL Server}'

odbc_str = 'DRIVER='+driver+';SERVER='+server+';PORT=1433;UID='+username+';DATABASE='+ database + ';PWD='+ password
connect_str = 'mssql+pyodbc:///?odbc_connect='+ odbc_str
engine = create_engine(connect_str)
#Base = declarative_base()


