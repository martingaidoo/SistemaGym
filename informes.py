"""
import sqlite3
import pandas as pd
import subprocess

def generar_cliente():
    # Conectar a la base de datos SQLite
    conn = sqlite3.connect("BaseDatos.db")

    # Consulta SQL para obtener todos los datos de la tabla "Clientes"
    consulta = "SELECT * FROM Clientes;"

    # Leer los datos en un DataFrame de pandas
    df = pd.read_sql_query(consulta, conn)

    # Guardar el DataFrame en un archivo Excel
    df.to_excel("clientes_data.xlsx", index=False)

    # Cerrar la conexión a la base de datos
    conn.close()

def generar_completo():
    # Conectar a la base de datos SQLite
    conn = sqlite3.connect("BaseDatos.db")

    # Consulta SQL para obtener solo las columnas necesarias de la tabla "Clientes"
    consulta_clientes = "SELECT id, Apellido, Nombre, Documento, Telefono, Correo, Fecha_Nacimiento FROM Clientes;"

    # Consulta SQL para obtener solo las columnas necesarias de la tabla "Cuotas"
    consulta_cuotas = "SELECT Cuotas.id_cliente, Cuotas.Haber, Cuotas.[PLAN], Cuotas.Fecha, Cuotas.Vencimiento FROM Cuotas;"

    # Leer los datos en DataFrames de pandas
    df_clientes = pd.read_sql_query(consulta_clientes, conn)
    df_cuotas = pd.read_sql_query(consulta_cuotas, conn)

    # Realizar un join entre las tablas usando la columna 'id_cliente'
    df_completo = pd.merge(df_cuotas, df_clientes, left_on='id_cliente', right_on='id', how='left')

    # Seleccionar solo las columnas necesarias
    columnas_seleccionadas = ['Apellido', 'Nombre', 'Documento', 'Telefono', 'Correo', 'Fecha_Nacimiento', 'PLAN', 'Haber', 'Fecha', 'Vencimiento']
    df_resultado = df_completo[columnas_seleccionadas]

    # Guardar el DataFrame resultante en un archivo Excel
    df_resultado.to_excel("datos_clientes.xlsx", index=False)

    # Cerrar la conexión a la base de datos
    conn.close()

    subprocess.Popen(["start", "excel", "datos_clientes.xlsx"], shell=True)
"""
import sqlite3
import pandas as pd
import subprocess
from datetime import datetime

def generar_completo():
    # Conectar a la base de datos SQLite
    conn = sqlite3.connect("BaseDatos.db")

    # Consulta SQL para obtener solo las columnas necesarias de la tabla "Clientes"
    consulta_clientes = "SELECT id, Apellido, Nombre, Documento, Telefono, Correo, Fecha_Nacimiento FROM Clientes;"

    # Consulta SQL para obtener solo las columnas necesarias de la tabla "Cuotas"
    consulta_cuotas = "SELECT Cuotas.id_cliente, Cuotas.Haber, Cuotas.[PLAN], Cuotas.Fecha, Cuotas.Vencimiento FROM Cuotas;"

    # Leer los datos en DataFrames de pandas
    df_clientes = pd.read_sql_query(consulta_clientes, conn)
    df_cuotas = pd.read_sql_query(consulta_cuotas, conn)

    # Realizar un join entre las tablas usando la columna 'id_cliente'
    df_completo = pd.merge(df_cuotas, df_clientes, left_on='id_cliente', right_on='id', how='left')

    # Convertir la columna 'Vencimiento' a objetos datetime
    df_completo['Vencimiento'] = pd.to_datetime(df_completo['Vencimiento'], errors='coerce')

    # Agregar una nueva columna 'Estado' basada en la comparación entre fecha actual y fecha de vencimiento
    fecha_actual = datetime.now()
    df_completo['Estado'] = df_completo['Vencimiento'].apply(lambda x: 'Activo' if pd.notnull(x) and x > fecha_actual else 'Vencido')

    # Formatear la columna 'Vencimiento' antes de guardarla en el archivo Excel
    df_completo['Vencimiento_Formateada'] = df_completo['Vencimiento'].dt.strftime('%d/%m/%Y')

    # Seleccionar solo las columnas necesarias, incluyendo la nueva columna 'Estado'
    columnas_seleccionadas = ['Apellido', 'Nombre', 'Documento', 'Telefono', 'Correo', 'Fecha_Nacimiento', 'PLAN', 'Haber', 'Fecha', 'Vencimiento_Formateada', 'Estado']
    df_resultado = df_completo[columnas_seleccionadas]

    # Guardar el DataFrame resultante en un archivo Excel
    df_resultado.to_excel("datos_clientes.xlsx", index=False)

    # Cerrar la conexión a la base de datos
    conn.close()

    subprocess.Popen(["start", "excel", "datos_clientes.xlsx"], shell=True)

# Llamada a la función
generar_completo()

