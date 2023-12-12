import tkinter
from tkinter import PhotoImage
import customtkinter
from customtkinter import CTk, CTkFrame, CTkButton
from PIL import ImageTk,Image
import tkinter as tk
import pygame
import sqlite3

def agregar_cliente(cliente_data):
    # Conectar a la base de datos SQLite (asegúrate de que la base de datos exista)
    conn = sqlite3.connect("BaseDatos.db")
    cursor = conn.cursor()
    # Obtener los datos del cliente
    apellido, nombre, documento, correo, fecha_nacimiento, telefono = cliente_data
    # Verificar que ningún dato esté vacío
    if apellido and nombre and documento and correo and fecha_nacimiento and telefono:
        try:
            # Insertar los datos en la tabla
            cursor.execute("INSERT INTO Clientes (Apellido, Nombre, Documento, Correo, Fecha_Nacimiento, Telefono) VALUES (?, ?, ?, ?, ?, ?)",
                        (apellido, nombre, documento, correo, fecha_nacimiento, telefono))
            # Confirmar la transacción
            conn.commit()
        except sqlite3.Error as e:
            conn.rollback()
        finally:
            conn.close()
def registrarPago(data):
    # Conectar a la base de datos SQLite (asegúrate de que la base de datos exista)
    mixconexion = sqlite3.connect("BaseDatos.db")
    cursor = mixconexion.cursor()
    # Obtener los datos del cliente
    Nombre, Haber, PLAN, PROFESOR, fecha= data
    # Verificar que ningún dato esté vacío
    if Nombre and Haber and PLAN and PROFESOR and fecha:
        try:
            # Insertar los datos en la tabla
            cursor.execute("INSERT INTO Cuotas (Nombre, Haber, PLAN, PROFESOR, fecha) VALUES (?, ?, ?, ?, ?)", (Nombre, Haber, PLAN, PROFESOR, fecha))
            # Confirmar la transacción
            mixconexion.commit()
        except sqlite3.Error as ex:
            mixconexion.rollback()
        finally:
            mixconexion.close()