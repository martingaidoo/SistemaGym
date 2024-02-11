import sqlite3
import tkinter
import tkinter as tk
import customtkinter
import tkinter.messagebox
from datetime import datetime, timedelta
import pygame
from dateutil.relativedelta import relativedelta
from tkinter import PhotoImage
from PIL import ImageTk,Image
from tkcalendar import Calendar
from tkinter import messagebox
import customtkinter as ctk

def actualizarPrecio(self):
    
        self.frame_actualizarPrecio = customtkinter.CTkFrame(self, width=250)
        self.frame_actualizarPrecio.grid(row=0, rowspan=2, column=1,columnspan=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.frame_actualizarPrecio.grid_columnconfigure((0,2), weight=1)
        self.frame_actualizarPrecio.grid_columnconfigure(1, weight=0)
        self.frame_actualizarPrecio.grid_rowconfigure((0, 1, 2), weight=0)
        class ProgramaABM:
            def __init__(self, frame):
                self.frame = frame

                # Conectarse a la base de datos SQLite
                self.conexion = sqlite3.connect("BaseDatos.db")
                self.cursor = self.conexion.cursor()
                self.conexion.commit()

                # Crear etiquetas y campos de entrada
                self.label_nombre = customtkinter.CTkLabel(frame, text="Nombre:")
                self.label_nombre.grid(row=1, column=0)
                self.nombre_entry = customtkinter.CTkEntry(frame)
                self.nombre_entry.grid(row=1, column=1)

                self.label_precio = customtkinter.CTkLabel(frame, text="Precio:")
                self.label_precio.grid(row=2, column=0)
                self.precio_entry = customtkinter.CTkEntry(frame)
                self.precio_entry.grid(row=2, column=1)

                # Crear botones
                self.btn_agregar = customtkinter.CTkButton(frame, text="Agregar", command=self.agregar)
                self.btn_agregar.grid(row=3, column=0)

                self.btn_actualizar = customtkinter.CTkButton(frame, text="Actualizar", command=self.actualizar)
                self.btn_actualizar.grid(row=3, column=1)

                # Crear una lista para mostrar los datos de la base de datos
                self.lista_programas = tk.Listbox(frame)
                self.lista_programas.grid(row=4, column=1)
                self.mostrar_programas()

                # Asignar una función para manejar la selección en la lista
                self.lista_programas.bind('<<ListboxSelect>>', self.seleccionar_programa)

            def mostrar_programas(self):
                self.lista_programas.delete(0, tk.END)
                programas = self.cursor.execute('SELECT * FROM Programa').fetchall()
                for programa in programas:
                    _, _, precio, nombre = programa  # Obtener los dos últimos elementos de la tupla
                    self.lista_programas.insert(tk.END, (precio, nombre))

            def agregar(self):
                nombre = self.nombre_entry.get()
                precio = self.precio_entry.get()
                if nombre and precio:
                    self.cursor.execute("INSERT INTO Programa (Plan, Precio, Nombre) VALUES (?, ?, ?)",
                                        (0, precio, nombre))
                    self.conexion.commit()
                    self.mostrar_programas()
                    self.limpiar_campos()

            def actualizar(self):
                nombre = self.nombre_entry.get()
                precio = self.precio_entry.get()
                if nombre and precio:
                    self.cursor.execute("UPDATE Programa SET Precio=? WHERE Nombre=?", (precio, nombre))
                    self.conexion.commit()
                    self.mostrar_programas()
                    self.limpiar_campos()

            def seleccionar_programa(self, event):
                programa = self.lista_programas.get(self.lista_programas.curselection())
                precio, nombre = programa
                self.nombre_entry.delete(0, tk.END)
                self.nombre_entry.insert(0, nombre)
                self.precio_entry.delete(0, tk.END)
                self.precio_entry.insert(0, precio)

            def limpiar_campos(self):
                self.nombre_entry.delete(0, tk.END)
                self.precio_entry.delete(0, tk.END)

            def __del__(self):
                self.conexion.close()

        ProgramaABM(self.frame_actualizarPrecio)