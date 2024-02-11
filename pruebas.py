from logicaBotones import *
from tkinter import PhotoImage
import customtkinter
import PIL.Image
from tkinter import *
import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk
import time

from datetime import datetime, timedelta
import sqlite3


import sqlite3
from datetime import datetime, timedelta

def obtener_notificaciones_recientes():
    # Conexión a la base de datos SQLite
    conn = sqlite3.connect('BaseDatos.db')
    cursor = conn.cursor()

    # Fecha actual menos 5 días
    fecha_limite = datetime.now() - timedelta(days=5)

    # Consulta SQL para obtener las notificaciones recientes
    consulta = """
    SELECT * FROM Notificacion
    WHERE Fecha >= ?
    """
    cursor.execute(consulta, (fecha_limite,))

    # Obtener los resultados
    filas = cursor.fetchall()

    # Cerrar la conexión y retornar las filas obtenidas
    conn.close()
    return filas

# Ejemplo de uso de la función
notificaciones_recientes = obtener_notificaciones_recientes()
for notificacion in notificaciones_recientes:
    print(notificacion)




