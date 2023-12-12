import sqlite3
import pandas as pd
connection =sqlite3.connect("BaseDatos.db")
cursor = connection.cursor()
sqlquery = "SELECT * FROM Clientes"
cursor.execute(sqlquery)
result = cursor.fetchall()
for row in result:
    df = pd.read_sql_query(sqlquery, connection)
    df.to_csv("clientes.xls", index = False)

