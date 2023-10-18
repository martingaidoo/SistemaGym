import tkinter
from tkinter import PhotoImage
import customtkinter
from customtkinter import CTk, CTkFrame, CTkButton
from PIL import ImageTk,Image
import tkinter as tk
import pygame
import sqlite3

def agregar_cliente(cliente_data):
    conn = sqlite3.connect('BaseDatos.db')
    cursor = conn.cursor()
    insert_query = """
    INSERT INTO Clientes (Apellido, Nombre, Documento, Correo, Fecha_Nacimiento, Telefono)
    VALUES (?, ?, ?, ?, ?, ?)
    """
    
    cursor.execute(insert_query, cliente_data)
    conn.commit()
    conn.close()
