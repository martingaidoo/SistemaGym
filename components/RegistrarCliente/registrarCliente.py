import sqlite3
import tkinter
import tkinter as tk
import customtkinter
import tkinter.messagebox
from datetime import datetime, timedelta
import pygame
from database_utils import obtener_datos_cliente
from dateutil.relativedelta import relativedelta
from tkinter import PhotoImage
from PIL import ImageTk,Image
from tkcalendar import Calendar
from tkinter import messagebox







""" en esta funcion registrara un cliente nuevo

Args: 
    cliente_data (lista): describe una informacion que se extrae de las entradas en tkinter y son pasadas como lista

return:
    registrar: registra un nuevo cliente 
"""

def agregar_cliente(cliente_data):
    # Conectar a la base de datos SQLite (asegúrate de que la base de datos exista)
    conn = sqlite3.connect("BaseDatos.db")
    cursor = conn.cursor()
    # Obtener los datos del cliente
    nombre, apellido, correo, documento, fecha_nacimiento, telefono = cliente_data
    # Verificar que ningún dato esté vacío
    if apellido and nombre and documento and correo and fecha_nacimiento and telefono:
        if not any(char.isdigit() for char in nombre) and not any(char.isdigit() for char in apellido) :
            if  len(documento)==8 and documento.isdigit():
                cursor.execute("SELECT * FROM Clientes WHERE Documento = ?", (documento,))
                existente = cursor.fetchone()

                if existente:
                    # Documento ya existe en la base de datos
                    messagebox.showinfo('Error', f"El documento {documento} ya está registrado.")
                else:
                    if telefono.isdigit():
                    
                        try:
                            # Insertar los datos en la tabla
                            cursor.execute("INSERT INTO Clientes (Apellido, Nombre, Documento, Correo, Fecha_Nacimiento, Telefono, Estado) VALUES (?, ?, ?, ?, ?, ?, ?)",
                                        (apellido, nombre, documento, correo, fecha_nacimiento, telefono, 1))
                            # Confirmar la transacción
                            conn.commit()
                            mensaje = f"Registro de Cliente:\n\nNombre: {nombre}\nApellido: {apellido}\nDocumento: {documento}\nCorreo: {correo}\nNacimiento: {fecha_nacimiento}\nTelefono: {telefono}"
                            messagebox.showinfo("Cliente Registrado", mensaje)
                        except sqlite3.Error as e:
                            conn.rollback()
                        finally:
                            conn.close()
                    else:
                        messagebox.showinfo(f'Error', f"{telefono} no es un posible numero valido")
                        
            else:
                messagebox.showinfo(f'Error', f"{documento} no es un documento valido")
        
                
        else:
            
            messagebox.showinfo(f'Error', "El nombre o el apellido no cumple con el formato")
        



def registrarCliente(self):
        self.frame_registrarCliente = customtkinter.CTkFrame(self, width=250)
        self.frame_registrarCliente.grid(row=0, rowspan=2, column=1,columnspan=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.frame_registrarCliente.grid_columnconfigure((0,2), weight=1)
        self.frame_registrarCliente.grid_columnconfigure(1, weight=0)
        #LABEL TITULO
        label_titulo = customtkinter.CTkLabel(self.frame_registrarCliente, text="Registrar clientes", font=('Century Gothic',20))
        label_titulo.grid(row=0, column=1, padx=(20, 0), pady=(5, 0), sticky="nsew")

        #Entradas
        label_nombre = customtkinter.CTkLabel(self.frame_registrarCliente, text="Nombre", font=('Century Gothic',15))
        label_nombre.grid(row=1, column=1, padx=(20, 0), pady=(5, 0), sticky="nsew")
        entry_nombre = customtkinter.CTkEntry(self.frame_registrarCliente, width=120, height=25, corner_radius=10)
        entry_nombre.grid(row=2, column=1, padx=(20, 0), pady=(5, 0), sticky="nsew")

        label_apellido = customtkinter.CTkLabel(self.frame_registrarCliente, text="Apellido", font=('Century Gothic',15))
        label_apellido.grid(row=3, column=1, padx=(20, 0), pady=(5, 0), sticky="nsew")
        entry_apellido = customtkinter.CTkEntry(self.frame_registrarCliente, width=120, height=25, corner_radius=10)
        entry_apellido.grid(row=4, column=1, padx=(20, 0), pady=(5, 0), sticky="nsew")

        label_documento = customtkinter.CTkLabel(self.frame_registrarCliente, text="Documento", font=('Century Gothic',15))
        label_documento.grid(row=5, column=1, padx=(20, 0), pady=(5, 0), sticky="nsew")
        entry_documento = customtkinter.CTkEntry(self.frame_registrarCliente, width=120, height=25, corner_radius=10)
        entry_documento.grid(row=6, column=1, padx=(20, 0), pady=(5, 0), sticky="nsew")

        label_correo = customtkinter.CTkLabel(self.frame_registrarCliente, text="Correo", font=('Century Gothic',15))
        label_correo.grid(row=7, column=1, padx=(20, 0), pady=(5, 0), sticky="nsew")
        entry_correo = customtkinter.CTkEntry(self.frame_registrarCliente, width=120, height=25, corner_radius=10)
        entry_correo.grid(row=8, column=1, padx=(20, 0), pady=(5, 0), sticky="nsew")

        label_telefono = customtkinter.CTkLabel(self.frame_registrarCliente, text="Telefono", font=('Century Gothic',15))
        label_telefono.grid(row=9, column=1, padx=(20, 0), pady=(5, 0), sticky="nsew")
        entry_telefono = customtkinter.CTkEntry(self.frame_registrarCliente, width=120, height=25, corner_radius=10)
        entry_telefono.grid(row=10, column=1, padx=(20, 0), pady=(5, 0), sticky="nsew")

        label_fechaNacimiento = customtkinter.CTkLabel(self.frame_registrarCliente, text="Fecha de nacimiento", font=('Century Gothic',15)) # se ingresa ejemplo "año-mes-dia"
        label_fechaNacimiento.grid(row=11, column=1, padx=(20, 0), pady=(5, 0), sticky="nsew")

        frameCalendario = customtkinter.CTkFrame(master=self.frame_registrarCliente, width=300, height=300)
        frameCalendario.grid(row=12, column=1, padx=(20, 0), pady=(5, 0), sticky="nsew")
        
        # Crear un objeto Calendar
        cal = Calendar(frameCalendario, selectmode="day", year=2023, month=10, day=23)

        # Colocar los widgets en la ventana
        cal.pack(pady=10)
        
        #boton confirmar
        button_confirmar = customtkinter.CTkButton(
            master=self.frame_registrarCliente,
            width=220,
            text="Confirmar",
            command=lambda: (agregar_cliente([entry_nombre.get(),entry_apellido.get(), entry_correo.get(), entry_documento.get(), datetime.strptime(cal.get_date(), "%d/%m/%y").strftime("%d/%m/%Y"), entry_telefono.get()]),self.frame_pagoCuota.pack(pady=60),self.frame_registrarCliente.pack_forget()),
            corner_radius=6
        )
        button_confirmar.grid(row=13, column=1, padx=(20, 0), pady=(5, 0), sticky="nsew")