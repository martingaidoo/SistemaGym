import tkinter
from tkinter import PhotoImage
import customtkinter
from customtkinter import CTk, CTkFrame, CTkButton
from PIL import ImageTk,Image
import tkinter as tk
import sqlite3
from datetime import datetime
from dateutil.relativedelta import relativedelta
from tkinter import messagebox

# Obtener la fecha actual

fecha_actual = datetime.now()
actualFechaHora = fecha_actual.strftime("%d/%m/%Y %H:%M:%S")
fecha_con_mes_adicional = fecha_actual + relativedelta(months=1)
# Formatear la fecha como días/mes/año
actual = fecha_actual.strftime("%d/%m/%Y")

actaulMasMes = fecha_con_mes_adicional.strftime("%d/%m/%Y")
#sirve para destrouit la ventada de la asistencia del cliente
banderaDestroy = True



def buscar_cliente_con_cuotas(documento):
    # Conectar con la base de datos
    conexion = sqlite3.connect('BaseDatos.db')
    cursor = conexion.cursor()

    # Ejecutar la consulta SQL para seleccionar la información del cliente por su documento
    cursor.execute("SELECT * FROM Clientes WHERE Documento = ?", (documento,))
    cliente = cursor.fetchone()  # Obtener el primer cliente que coincida con el documento
    
    if cliente:
        # Obtener las cuotas del cliente
        cursor.execute("SELECT * FROM Cuotas WHERE id_cliente = ?", (cliente[0],))
        cuotas = cursor.fetchone()
    else:
        cuotas = []

    # Cerrar la conexión con la base de datos
    conexion.close()

    return cliente, cuotas



""" en esta funcion registrara un cliente nuevo

Args: 
    documento (int): recibe un documento proporcionado por el usuario

return:
    datos_cliente: returna la fila de la tabla de clientes que contenga el documento proporcionado
"""
def obtener_datos_cliente(documento):
    # Consulta SQL para obtener los datos de un cliente por su documento
    conn = sqlite3.connect("BaseDatos.db")
    cursor = conn.cursor()
    consulta = """
    SELECT * FROM Clientes WHERE Documento = ?;
    """
    cursor.execute(consulta, (documento,)) 
    datos_cliente = cursor.fetchone()    
    #id_cliente, apellido, nombre, documento, correo, fecha_nacimiento, telefono = datos_cliente
    consulta = """
    SELECT * FROM Cuotas WHERE id_cliente = ?;
    """
    cursor.execute(consulta, (datos_cliente[0],))
    datos_cliente = datos_cliente + cursor.fetchone()
    conn.close()
    return datos_cliente

