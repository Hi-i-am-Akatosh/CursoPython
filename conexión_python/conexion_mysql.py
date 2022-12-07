from optparse import Values
from tkinter import INSERT
import mysql.connector

try:
    connection = mysql.connector.connect(
        host = 'localhost',
        port = 3306,
        user = 'root',
        password = '12345',
        db = 'prueba_creacion'
    )
    mysql_cursor = connection.cursor()
    #mysql_cursor.execute("CREATE DATABASE prueba_creacion")
    #mysql_cursor.execute("CREATE TABLE usuarios(nombres VARCHAR(50),apellidos VARCHAR(50),edad INTEGER(10),direccion VARCHAR(100))")
    #mysql_cursor.execute("INSERT INTO usuarios(nombres,apellidos,edad,direccion) VALUES ("David","Navarro","21","Vicentina")")
    #mysql_cursor.execute("INSERT INTO usuarios(nombres,apellidos) VALUES ("David","Navarro")")
    #sql = "INSERT INTO usuarios(nombres,apellidos,edad,direccion) VALUES (%s,%s,%s,%s)"
    #val = ("David", "Navarro", "21", "Vicentina")
    #mysql_cursor.execute(sql,val)
    #connection.commit()

    #sql = "INSERT INTO usuarios(nombres,apellidos,edad,direccion) VALUES (%s,%s,%s,%s)"
    #val = [("David", "Navarro", "21", "Vicentina"),("Mauricio", "Galeano", "34", "Floresta"),("Carmen","Sarasti","71","Ichimbia")]
    #mysql_cursor.executemany(sql,val)
    #connection.commit()

    """mysql_cursor.execute("SELECT * FROM usuarios")
    result = mysql_cursor.fetchall()
    for x in result:
        print (x)"""

    """mysql_cursor.execute("SELECT nombres,edad FROM usuarios")
    result = mysql_cursor.fetchall()
    for x in result:
        print (x)"""

    

    """sql = "SELECT * FROM usuarios WHERE direccion = 'Floresta'"
    mysql_cursor.execute(sql)
    result = mysql_cursor.fetchall()
    for x in result:
        print (x)"""
    

    """sql = "SELECT * FROM usuarios ORDER BY edad"
    mysql_cursor.execute(sql)
    result = mysql_cursor.fetchall()
    for x in result:
        print (x)
    
    print("\n\n")

    sql = "SELECT * FROM usuarios ORDER BY edad DESC"
    mysql_cursor.execute(sql)
    result = mysql_cursor.fetchall()
    for x in result:
        print (x)"""

    """sql = "DELETE FROM usuarios WHERE nombres = 'David'"
    mysql_cursor.execute(sql)
    connection.commit()"""
    
    sql = "DROP TABLE propiedades"
    mysql_cursor.execute(sql)

    if (connection.is_connected()):                                                                     #varchar() = longitud string ;integer() = longitud int
        print("Conexión establecida")


except Exception as ex:
    print(ex)