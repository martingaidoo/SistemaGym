import tkinter
import tkinter.messagebox
import customtkinter
from tkinter import PhotoImage
import customtkinter
import customtkinter as ctk
from customtkinter import CTk, CTkFrame, CTkButton, CTkEntry
import PIL.Image
from PIL import ImageTk,Image
from tkinter import *
import tkinter as tk
import pygame
import sqlite3
from tkcalendar import Calendar
from tkinter import ttk
from tkinter import messagebox
import keyboard
from datetime import datetime
from database_utils import *
import requests
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

def valor_en_columna(valor, lista_filas):
    # Iterar sobre cada fila en la lista
    for fila in lista_filas:
        # Iterar sobre cada elemento de la fila
        for elemento in fila:
            # Verificar si el valor está presente en el elemento actual
            if valor == elemento:
                return True
    # Si no se encuentra en ninguna fila, retornar False
    return False

def conocerClientesPorVencer():
    data = []
    info_cliente = []

    # Conectar a la base de datos
    conn = sqlite3.connect('BaseDatos.db')
    cursor = conn.cursor()

    # Obtener la fecha actual y la fecha dentro de 5 días
    fecha_actual = datetime.now()
    fecha_limite = fecha_actual + timedelta(days=5)

    # Consulta SQL para obtener todos los registros de Clientes y Cuotas
    consulta = """
        SELECT Clientes.*, Cuotas.*
        FROM Clientes
        JOIN Cuotas ON Clientes.id = Cuotas.id_cliente
    """
    cursor.execute(consulta)

    # Obtener los resultados
    resultados = cursor.fetchall()

    # Lista para almacenar los datos de los clientes cuyas cuotas se vencen en 5 o menos días
    clientes_vencimiento_cercano = []

    clientes_notificados_recientes = obtener_notificaciones_recientes()

    # Iterar sobre los resultados y realizar el filtrado fuera de la consulta
    for fila in resultados:
        # Convertir la fecha de vencimiento de la cuota a un objeto datetime
        # Obtener la fecha de vencimiento de la cuota
        # Obtener la fecha de vencimiento de la cuota
        fecha_vencimiento_cuota = datetime.strptime(str(fila[-3]), "%d/%m/%Y")
        # Calcular la diferencia de días entre la fecha actual y la fecha de vencimiento de la cuota
        diferencia_dias = (fecha_vencimiento_cuota - fecha_actual).days
        # Si la diferencia es de 5 días o menos, añadir los datos del cliente y la cuota al array
        if 0 < diferencia_dias < 5:
            clientes_vencimiento_cercano.append(fila)

    for cliente_cuota_info in clientes_vencimiento_cercano:
        if not valor_en_columna(cliente_cuota_info[0], clientes_notificados_recientes):
            # Extraer la información necesaria de la tupla cliente_cuota_info

            numero_telefono = cliente_cuota_info[6]  # Número de teléfono del cliente
            fecha_vencimiento_cuota = cliente_cuota_info[-3]  # Fecha de vencimiento de la cuota

            fecha_vencimiento_datetime = datetime.strptime(str(fecha_vencimiento_cuota), "%d/%m/%Y")

            print((fecha_vencimiento_datetime - fecha_actual).days + 1)

            # Construir el mensaje para el cliente
            mensaje = f"Hola *{cliente_cuota_info[2]}*! Salud integral le recuerda que su cuota de *{cliente_cuota_info[10]}* esta a {(fecha_vencimiento_datetime - fecha_actual).days + 1} de vencer. Muchas Gracias!"
            print(mensaje)
            # Crear el diccionario con la información del cliente y su cuota
            cliente = {
                "numero": str(numero_telefono),  # Convertir a cadena de texto si es necesario
                "mensaje": mensaje
            }

            # Agregar el diccionario a la lista data
            data.append(cliente)
            info_cliente.append(cliente_cuota_info)

    # Cerrar la conexión
    conn.close()
    
    return (data, info_cliente)



def guardar_notificacion(tipo, id_cliente, mensaje):
    # Conexión a la base de datos SQLite
    conn = sqlite3.connect('BaseDatos.db')
    cursor = conn.cursor()
    # Fecha actual como un objeto datetime
    fecha_actual = datetime.now()
    # Insertar los datos en la tabla Notificacion
    cursor.execute("INSERT INTO Notificacion (Tipo, id_cliente, Mensaje, Fecha) VALUES (?, ?, ?, ?)", (tipo, id_cliente, mensaje, fecha_actual))
    # Confirmar la transacción y cerrar la conexión
    conn.commit()
    conn.close()


def whatsapp_api(self):
    url = 'http://localhost:3000/enviar-mensaje'
    data, info_cliente = conocerClientesPorVencer()

    def button_event():
        print("button pressed")
        response = requests.post(url, json=data)
        if response.status_code == 200:
            print("Respuesta del servidor:", response.json())
            for i in range(len(data)):
                print("Enviando notificación para:", data[i]["mensaje"])
                guardar_notificacion("whatsapp_ProxVencimiento", info_cliente[i][0], data[i]["mensaje"])
                #aca ejecutar limpiar etiquetanotificacion
            for child in notificar.winfo_children():
                child.destroy()
        else:
            print("Error al enviar la solicitud POST:", response.status_code)

    notificar = customtkinter.CTkScrollableFrame(self, label_text="Notificar")
    notificar.pack(pady=10)
    for i in info_cliente:
        etiqueta_notificacion = customtkinter.CTkLabel(notificar, text=f"{i[1]} {i[2]} - Vence pronto", font=("Arial", 12))
        etiqueta_notificacion.pack(fill="x", padx=0, pady=5)
    button = customtkinter.CTkButton(self, text="Enviar Mensaje", command=button_event)
    button.pack(pady=10)