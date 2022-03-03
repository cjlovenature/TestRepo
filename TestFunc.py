import requests,pyodbc,json,pymysql,logging
from jsondiff import diff

#-------------MYSQL ----------------------
connection = pymysql.connect(host='localhost',user='root',password='data@123',db='sriram')

def createTable(connection):
    cursor_obj = connection.cursor()
    query = """create table table_name(column1 varchar(50), column2 integer not null primary key,column3 char(1) );"""
    try:
        cursor_obj.execute(query)
        connection.commit()
        connection.close()
    except:
      logging.error("Failed to create table")
    
#-------------- data insertion ---------------

def insertData(connection,val1,val2,val3):
    cursor_obj = connection.cursor()
    query = "INSERT INTO table_name(column1,column2,column3) VALUES (%s,%s,%s);"
    try:
        cursor_obj.execute(query,(val1,val2,val3))
        connection.commit()
        connection.close()
    except:
        logging.error("Insertion failed !!!!!!")
    
#-------------- SHOW ALL DATA IN TABLE---------------
def showData(connection):
    cursor_obj = connection.cursor()
    query = "select * from table_name;"
    cursor_obj.execute(query)
    data = cursor_obj.fetchall()
    print(data)
    
# ------------------FUNCTION CALLS ----------
#createTable(connection)
#insertData(connection,'company',674,'Y')
    
    

# ------------------ working with SQL Server ---------------------
# cnxn_strng = 'DRIVER={ODBC Driver 17 for SQL Server};Server=localhost;Database=DUMMY_DB;'
# connection = pyodbc.connect(cnxn_strng)


