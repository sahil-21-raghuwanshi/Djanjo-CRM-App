

import mysql.connector

dataBase =mysql.connector.connect(
    host='localhost',
    user='root',
    password='2104@!Sahil')
    
cursorOject=dataBase.cursor()

cursorOject.execute("CREATE DATABASE database_sahil")

print("ALL Done !")