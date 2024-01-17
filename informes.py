import sqlite3
import pandas as pd
import subprocess
from datetime import datetime
from openpyxl import load_workbook
import openpyxl

nombre_activo = 'Activo'

def palabra(valor):
    try:
        entero_valor = int(valor)
        if int(valor) > 0 and int(valor) < 90000:
            return 'background-color: red'
        elif int(valor) <= 0:
            return 'background-color: #4CE308'
        else:
            return None
    except ValueError:
        if 'Regular' in str(valor):
            return 'background-color: #4CE308'
        elif 'Vencido' in str(valor):
            return 'background-color: red'
        else:
            return None



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
    df_completo['Vencimiento'] = pd.to_datetime(df_completo['Vencimiento'], errors='coerce', dayfirst=True)

    # Agregar una nueva columna 'Estado' basada en la comparación entre fecha actual y fecha de vencimiento
    fecha_actual = datetime.now()

    df_completo['Estado'] = df_completo['Vencimiento'].apply(lambda x: 'Regular' if pd.notnull(x) and x > fecha_actual else 'Vencido')

    # Formatear la columna 'Vencimiento' antes de guardarla en el archivo Excel
    df_completo['Vencimiento_Formateada'] = df_completo['Vencimiento'].dt.strftime('%d/%m/%Y')

    # Seleccionar solo las columnas necesarias, incluyendo la nueva columna 'Estado'
    columnas_seleccionadas = ['Apellido', 'Nombre', 'Documento', 'Telefono', 'Correo', 'Fecha_Nacimiento', 'PLAN', 'Haber', 'Fecha', 'Vencimiento_Formateada', 'Estado']
    df_resultado = df_completo[columnas_seleccionadas]

    # Aplicar estilos directamente al DataFrame antes de convertirlo en un objeto Styler
    df_resultado_styled = df_resultado.style.applymap(palabra)



    # Guardar el DataFrame resultante en un archivo Excel
    df_resultado_styled.to_excel("datos_clientes.xlsx", index=False)

    # Cerrar la conexión a la base de datos
    conn.close()

    # Abrir el archivo Excel
    subprocess.Popen(["start", "excel", "datos_clientes.xlsx"], shell=True)