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
from informes import *

import os
import sys

banderaVencimiento = False

def controlAcceso(self):
        self.frame_asistencia = customtkinter.CTkFrame(self, width=250)
        self.frame_asistencia.grid(row=0, rowspan=2, column=1,columnspan=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        label_titulo = customtkinter.CTkLabel(self.frame_asistencia, text="CONTROL DE ACCESO", font=('Century Gothic',30))
        label_titulo.place(relx=0.34, rely=0.1)
        label_titulo = customtkinter.CTkLabel(self.frame_asistencia, text="Documente:", font=('Century Gothic',15))
        label_titulo.place(relx=0.34, rely=0.2)
        
        entry_asistencia = customtkinter.CTkEntry(self.frame_asistencia,
                                    width=200,
                                    height=25,
                                    corner_radius=10)
        entry_asistencia.place(relx=0.48, rely=0.2)
        button = customtkinter.CTkButton(self.frame_asistencia, width=220, text="CONFIRMAR", command=lambda: (registrarAsistencia(obtener_datos_cliente(entry_asistencia.get())),entry_asistencia.delete(0, tk.END)), corner_radius=6)
        button.place(x=330, y=165)
        #hace lo mismo que apretar el boton

        def funcion_al_presionar_tecla(event):
            if entry_asistencia.get() != "":
                registrarAsistencia(obtener_datos_cliente(entry_asistencia.get())),entry_asistencia.delete(0, tk.END)
        #ejecuta la funcion de arriba con apretar el enter
        self.bind("<Return>", funcion_al_presionar_tecla)

def registrarCliente(self):
        self.frame_registrarCliente = customtkinter.CTkFrame(self, width=250)
        self.frame_registrarCliente.grid(row=0, rowspan=2, column=1,columnspan=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        #LABEL TITULO
        label_titulo = customtkinter.CTkLabel(self.frame_registrarCliente, text="Registrar clientes", font=('Century Gothic',20))
        label_titulo.place(relx=0.26, rely=0.03)

        #Entradas
        label_nombre = customtkinter.CTkLabel(self.frame_registrarCliente, text="Nombre", font=('Century Gothic',15))
        label_nombre.place(relx=0.32, rely=0.1)
        entry_nombre = customtkinter.CTkEntry(self.frame_registrarCliente, width=120, height=25, corner_radius=10)
        entry_nombre.place(relx=0.5, rely=0.16, anchor=tk.CENTER)

        label_apellido = customtkinter.CTkLabel(self.frame_registrarCliente, text="Apellido", font=('Century Gothic',15))
        label_apellido.place(relx=0.32, rely=0.2)
        entry_apellido = customtkinter.CTkEntry(self.frame_registrarCliente, width=120, height=25, corner_radius=10)
        entry_apellido.place(relx=0.5, rely=0.26, anchor=tk.CENTER)

        label_documento = customtkinter.CTkLabel(self.frame_registrarCliente, text="Documento", font=('Century Gothic',15))
        label_documento.place(relx=0.32, rely=0.3)
        entry_documento = customtkinter.CTkEntry(self.frame_registrarCliente, width=120, height=25, corner_radius=10)
        entry_documento.place(relx=0.5, rely=0.36, anchor=tk.CENTER)

        label_correo = customtkinter.CTkLabel(self.frame_registrarCliente, text="Correo", font=('Century Gothic',15))
        label_correo.place(relx=0.32, rely=0.4)
        entry_correo = customtkinter.CTkEntry(self.frame_registrarCliente, width=120, height=25, corner_radius=10)
        entry_correo.place(relx=0.5, rely=0.46, anchor=tk.CENTER)

        label_telefono = customtkinter.CTkLabel(self.frame_registrarCliente, text="Telefono", font=('Century Gothic',15))
        label_telefono.place(relx=0.32, rely=0.5)
        entry_telefono = customtkinter.CTkEntry(self.frame_registrarCliente, width=120, height=25, corner_radius=10)
        entry_telefono.place(relx=0.5, rely=0.56, anchor=tk.CENTER)

        label_fechaNacimiento = customtkinter.CTkLabel(self.frame_registrarCliente, text="Fecha de nacimiento", font=('Century Gothic',15)) # se ingresa ejemplo "año-mes-dia"
        label_fechaNacimiento.place(relx=0.32, rely=0.58)

        frameCalendario = customtkinter.CTkFrame(master=self.frame_registrarCliente, width=300, height=300)
        frameCalendario.place(relx=0.5, rely=0.75, anchor=tk.CENTER)
        
        # Crear un objeto Calendar
        cal = Calendar(frameCalendario, selectmode="day", year=2023, month=10, day=23)

        # Colocar los widgets en la ventana
        cal.pack(pady=10)
        
        #boton confirmar
        button_confirmar = customtkinter.CTkButton(
            master=self.frame_registrarCliente,
            width=220,
            text="Confirmar",
            command=lambda: (agregar_cliente([entry_nombre.get(),entry_apellido.get(), entry_correo.get(), entry_documento.get(), cal.get_date(), entry_telefono.get()]),self.frame_pagoCuota.pack(pady=60),self.frame_registrarCliente.pack_forget()),
            corner_radius=6
        )
        button_confirmar.place(relx=0.35, rely=0.90)

def actualizarClientes(self):
        self.frame_actualizarClientes = customtkinter.CTkFrame(self, width=250)
        self.frame_actualizarClientes.grid(row=0, rowspan=2, column=1,columnspan=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        class ProgramaABM_Clientes:
            def __init__(self, frame):
                self.frame = frame

                # Conectarse a la base de datos SQLite
                self.conexion = sqlite3.connect("BaseDatos.db")
                self.cursor = self.conexion.cursor()
                self.conexion.commit()

                # Crear etiquetas y campos de entrada
                self.label_nombre = ctk.CTkLabel(frame, text="Nombre:")
                self.label_nombre.grid(row=1, column=0)
                self.nombre_entry = ctk.CTkEntry(frame)
                self.nombre_entry.grid(row=1, column=1)

                self.label_Apellido = ctk.CTkLabel(frame, text="Apellido:")
                self.label_Apellido.grid(row=1, column=2)
                self.Apellido_entry = ctk.CTkEntry(frame)
                self.Apellido_entry.grid(row=1, column=3)

                self.label_Correo = ctk.CTkLabel(frame, text="Correo:")
                self.label_Correo.grid(row=2, column=0)  #tienen mal el nombre de las entradas hay que arreglarlo@@@@@@@@@@@@@@@@@@@@@@@@@@
                self.Correo_entry = ctk.CTkEntry(frame)
                self.Correo_entry.grid(row=2, column=1)

                self.label_Documento= ctk.CTkLabel(frame, text="Documento:")
                self.label_Documento.grid(row=2, column=2) #tienen mal el nombre de las entradas hay que arreglarlo@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                self.Documento_entry = ctk.CTkEntry(frame)
                self.Documento_entry.grid(row=2, column=3)

                self.label_FechaNacimiento = ctk.CTkLabel(frame, text="Fecha de nacimiento:")
                self.label_FechaNacimiento.grid(row=3, column=0)
                self.FechaNacimiento_entry = ctk.CTkEntry(frame)
                self.FechaNacimiento_entry.grid(row=3, column=1)

                self.label_Telefono = ctk.CTkLabel(frame, text="Telefono:")
                self.label_Telefono.grid(row=3, column=2)
                self.Telefono_entry = ctk.CTkEntry(frame)
                self.Telefono_entry.grid(row=3, column=3)

                # Crear botones
                self.btn_actualizar = ctk.CTkButton(frame, text="Actualizar", command=self.actualizar)
                self.btn_actualizar.grid(row=4, column=2)



                # Crear una lista para mostrar los datos de la base de datos
                self.lista_programas = tk.Listbox(frame)
                self.lista_programas.grid(row=5, column=0, columnspan=4, sticky=tk.W + tk.E + tk.N + tk.S)
                self.mostrar_programas()

                # Asignar una función para manejar la selección en la lista
                self.lista_programas.bind('<<ListboxSelect>>', self.seleccionar_programa)

            def mostrar_programas(self):
                self.lista_programas.delete(0, ctk.END)
                programas = self.cursor.execute('SELECT * FROM Clientes').fetchall()
                for programa in programas:
                    _, nombre, apellido, correo, documento, fechaNacimiento, telefono = programa  # Obtener los dos últimos elementos de la tupla
                    self.lista_programas.insert(ctk.END, (apellido, nombre, documento, correo, fechaNacimiento, telefono))

            def actualizar(self):
                apellido = self.Apellido_entry.get()
                nombre = self.nombre_entry.get()
                correo = self.Correo_entry.get()
                documento = self.Documento_entry.get()
                fechaNacimiento = self.FechaNacimiento_entry.get()
                telefono = self.Telefono_entry.get()

                if apellido and nombre and correo and documento and fechaNacimiento and telefono:
                    self.cursor.execute("UPDATE Clientes SET Apellido=?, Nombre=?, Correo=?, Telefono=?, Fecha_Nacimiento=? WHERE Documento=?",
                                        (apellido, nombre, correo, telefono, fechaNacimiento, documento))
                    self.conexion.commit()
                    self.mostrar_programas()
                    self.limpiar_campos()

            def seleccionar_programa(self, event):
                programa = self.lista_programas.get(self.lista_programas.curselection())
                nombre, apellido, correo,documento , fechaNacimiento, telefono = programa
                self.Telefono_entry.delete(0, ctk.END)
                self.Telefono_entry.insert(0, telefono)
                self.Documento_entry.delete(0, ctk.END)
                self.Documento_entry.insert(0, documento)
                self.Correo_entry.delete(0, ctk.END)
                self.Correo_entry.insert(0, correo)
                self.FechaNacimiento_entry.delete(0, tk.END)
                self.FechaNacimiento_entry.insert(0, fechaNacimiento)

                self.nombre_entry.delete(0, ctk.END)
                self.nombre_entry.insert(0, nombre)

                self.Apellido_entry.delete(0, ctk.END)
                self.Apellido_entry.insert(0, apellido)

            def limpiar_campos(self):
                self.Apellido_entry.delete(0, ctk.END)
                self.nombre_entry.delete(0, ctk.END)
                self.FechaNacimiento_entry.delete(0, tk.END)
                self.Correo_entry.delete(0, ctk.END)
                self.Documento_entry.delete(0, ctk.END)
                self.Telefono_entry.delete(0, ctk.END)

            def __del__(self):
                self.conexion.close()

        ProgramaABM_Clientes(self.frame_actualizarClientes)

def consultarCuotas(self):      
        self.frame_consultarCuotas = customtkinter.CTkFrame(self, width=250)
        self.frame_consultarCuotas.grid(row=0, rowspan=2, column=1,columnspan=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        class ProgramaABM_cuotas:
            
            def __init__(self, frame):
                self.frame = frame

                # Conectarse a la base de datos SQLite
                self.conexion = sqlite3.connect("BaseDatos.db")
                self.cursor = self.conexion.cursor()
                self.conexion.commit()
        
                # Crear etiquetas y campos de entrada
                self.label_nombre = ctk.CTkLabel(frame, text="Nombre:")
                self.label_nombre.grid(row=1, column=0)
                self.nombre_entry = ctk.CTkEntry(frame)
                self.nombre_entry.grid(row=1, column=1)

                self.label_Apellido = ctk.CTkLabel(frame, text="Apellido:")
                self.label_Apellido.grid(row=1, column=2)
                self.Apellido_entry = ctk.CTkEntry(frame)
                self.Apellido_entry.grid(row=1, column=3)

                self.label_Deuda = ctk.CTkLabel(frame, text="Deuda:")
                self.label_Deuda.grid(row=2, column=0)  #tienen mal el nombre de las entradas hay que arreglarlo@@@@@@@@@@@@@@@@@@@@@@@@@@
                self.Deuda_entry = ctk.CTkEntry(frame)
                self.Deuda_entry.grid(row=2, column=1)

                self.label_Plan = ctk.CTkLabel(frame, text="Plan:")
                self.label_Plan.grid(row=2, column=2) #tienen mal el nombre de las entradas hay que arreglarlo@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                self.Plan_entry = ctk.CTkEntry(frame)
                self.Plan_entry.grid(row=2, column=3)

                self.label_Fecha = ctk.CTkLabel(frame, text="Fecha inicio:")
                self.label_Fecha.grid(row=3, column=0)
                self.Fecha_entry = ctk.CTkEntry(frame)
                self.Fecha_entry.grid(row=3, column=1)

                self.label_Vencimiento = ctk.CTkLabel(frame, text="Vencimiento:")
                self.label_Vencimiento.grid(row=3, column=2)
                self.Vencimiento_entry = ctk.CTkEntry(frame)
                self.Vencimiento_entry.grid(row=3, column=3)

                # Crear botones
                self.btn_actualizar = ctk.CTkButton(frame, text="Actualizar", command=self.actualizar)
                self.btn_actualizar.grid(row=4, column=2)

                self.btn_vencido = ctk.CTkButton(frame, text="Vencido", command=lambda: (self.mostrar_programas(), cambiar()))
                self.btn_vencido.grid(row=4, column=1)

                # Crear una lista para mostrar los datos de la base de datos
                self.lista_programas = tk.Listbox(frame)
                self.lista_programas.grid(row=5, column=0, columnspan=4, sticky=tk.W + tk.E + tk.N + tk.S)

                self.mostrar_programas()
     

                # Asignar una función para manejar la selección en la lista
                self.lista_programas.bind('<<ListboxSelect>>', self.seleccionar_programa)

                def cambiar():
                    global banderaVencimiento
                    banderaVencimiento = not (banderaVencimiento)

            def mostrar_programas(self):
                self.lista_programas.delete(0, ctk.END)
                cuotas = self.cursor.execute('SELECT * FROM Cuotas').fetchall()
                global banderaVencimiento
                if banderaVencimiento == False:
                    for cuota in cuotas:
                        id_cliente, haber, plan, profe, fecha, vencimiento, id_cliente2, id_programa = cuota  # Obtener los dos últimos elementos de la tupla
                        consulta = """SELECT * FROM Clientes WHERE id = ?;"""
                        self.cursor.execute(consulta, (id_cliente,)) 
                        cliente = self.cursor.fetchone()  
                        _, nombre, apellido, correo, documento, fechaNacimiento, telefono = cliente
                        self.lista_programas.insert(ctk.END, (apellido, nombre, haber, plan, fecha, vencimiento))
                if banderaVencimiento == True:
                    for cuota in cuotas:
                        fecha_actual = datetime.strptime(actual, "%d/%m/%Y")
                        fecha_vencimiento = datetime.strptime(cuota[5], "%d/%m/%Y")
                        if fecha_actual >= fecha_vencimiento:
                            id_cliente, haber, plan, profe, fecha, vencimiento, id_cliente2, id_programa = cuota  # Obtener los dos últimos elementos de la tupla
                            consulta = """SELECT * FROM Clientes WHERE id = ?;"""
                            self.cursor.execute(consulta, (id_cliente,)) 
                            cliente = self.cursor.fetchone()  
                            _, nombre, apellido, correo, documento, fechaNacimiento, telefono = cliente
                            self.lista_programas.insert(ctk.END, (apellido, nombre, haber, plan, fecha, vencimiento)) 


            def actualizar(self):
                apellido = self.Apellido_entry.get()
                nombre = self.nombre_entry.get()
                deuda = self.Deuda_entry.get()
                fecha = self.Fecha_entry.get()
                vencimiento = self.Vencimiento_entry.get()
                plan = self.Plan_entry.get()

                consulta = """SELECT * FROM Clientes WHERE Apellido = ? AND Nombre = ?;"""
                self.cursor.execute(consulta, (apellido, nombre))
                cliente = self.cursor.fetchone()


                if apellido and nombre and deuda and fecha and vencimiento and plan:

                    self.cursor.execute("UPDATE Cuotas SET Haber=?, PLAN=?, Fecha=?, Vencimiento=? WHERE id=?",
                                        (deuda,plan, fecha, vencimiento, cliente[0]))
                    self.conexion.commit()
                    self.mostrar_programas()
                    self.limpiar_campos()

            def seleccionar_programa(self, event):
                programa = self.lista_programas.get(self.lista_programas.curselection())
                nombre, apellido, haber, plan, fecha, vencimiento = programa
                self.Deuda_entry.delete(0, ctk.END)
                self.Deuda_entry.insert(0, haber)
                self.Plan_entry.delete(0, ctk.END)
                self.Plan_entry.insert(0, plan)
                self.Fecha_entry.delete(0, ctk.END)
                self.Fecha_entry.insert(0, fecha)
                self.Vencimiento_entry.delete(0, tk.END)
                self.Vencimiento_entry.insert(0, vencimiento)
                self.nombre_entry.delete(0, ctk.END)
                self.nombre_entry.insert(0, nombre)
                self.Apellido_entry.delete(0, ctk.END)
                self.Apellido_entry.insert(0, apellido)

            def limpiar_campos(self):
                self.Apellido_entry.delete(0, ctk.END)
                self.nombre_entry.delete(0, ctk.END)
                self.Deuda_entry.delete(0, ctk.END)
                self.Fecha_entry.delete(0, ctk.END)
                self.Vencimiento_entry.delete(0, ctk.END)
                self.Plan_entry.delete(0, ctk.END)

            def __del__(self):
                self.conexion.close()
        ProgramaABM_cuotas(self.frame_consultarCuotas)

def pagoCuotas(self):
        self.frame_pagoCuota = customtkinter.CTkFrame(self, width=250)
        self.frame_pagoCuota.grid(row=0, rowspan=2, column=1,columnspan=2, padx=(20, 0), pady=(20, 0), sticky="nsew")

    #LABEL TITULO
        label_titulo = customtkinter.CTkLabel(self.frame_pagoCuota, text="PAGO DE CUOTA", font=('Century Gothic',20))
        label_titulo.place(relx=0.34, rely=0.1)

        #Entradas
        label_cliente = customtkinter.CTkLabel(self.frame_pagoCuota, text="documento", font=('Century Gothic',15))
        label_cliente.place(relx=0.40, rely=0.2)

        entry_cliente = customtkinter.CTkEntry(self.frame_pagoCuota, width=220, height=25, corner_radius=10)
        entry_cliente.place(relx=0.5, rely=0.26, anchor=tk.CENTER)

        label_programa = customtkinter.CTkLabel(self.frame_pagoCuota, text="Programa", font=('Century Gothic',15))
        label_programa.place(relx=0.44, rely=0.35)

        conexion = sqlite3.connect('BaseDatos.db')
        cursor = conexion.cursor()

        menu_desplegable = ttk.Combobox(self.frame_pagoCuota, width=35, height=25)

        # Obtener los nombres de los clientes desde la base de datos
        cursor.execute("SELECT Nombre FROM Programa")
        nombres = cursor.fetchall()

        # Agregar los nombres al menú desplegable
        menu_desplegable['values'] = nombres

        #nombre_seleccionado = menu_desplegable.get()

        # Mostrar el menú desplegable
        menu_desplegable.place(relx=0.23, rely=0.4)


        label_pago = customtkinter.CTkLabel(self.frame_pagoCuota, text="Pago $", font=('Century Gothic',15))
        label_pago.place(relx=0.44, rely=0.5)
        entry_pago = customtkinter.CTkEntry(self.frame_pagoCuota, width=120, height=25, corner_radius=10)
        entry_pago.place(relx=0.5, rely=0.56, anchor=tk.CENTER)

        label_profesor = customtkinter.CTkLabel(self.frame_pagoCuota, text="Profesor", font=('Century Gothic',15))
        label_profesor.place(relx=0.44, rely=0.64)
        entry_profesor = customtkinter.CTkEntry(self.frame_pagoCuota, width=220, height=25, corner_radius=10)
        entry_profesor.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

        
        button_confirmar = customtkinter.CTkButton(
            self.frame_pagoCuota,
            width=220,
            text="Confirmar",
            command=lambda: (registrarPago([entry_cliente.get(), entry_pago.get(), menu_desplegable.get()[1:len(menu_desplegable.get())-1], entry_profesor.get()]), self.frame_pagos.pack(pady=60),self.frame_pagoCuota.pack_forget()),corner_radius=6)
        button_confirmar.place(relx=0.25, rely=0.9)


def actualizarPrecio(self):
        self.frame_actualizarPrecio = customtkinter.CTkFrame(self, width=250)
        self.frame_actualizarPrecio.grid(row=0, rowspan=2, column=1,columnspan=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
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
                self.lista_programas.grid(row=4, column=0, columnspan=2)
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


def buscarCliente(self):
    class CustomEntry(tk.Entry):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.bind("<KeyRelease>", self.actualizar_resultados)

        def actualizar_resultados(self, event):
            # Obtiene la entrada actual del cuadro de texto
            entrada = self.get().lower()

            # Filtra la lista de nombres y apellidos en función de la entrada
            resultados_filtrados = [nombre_apellido for nombre_apellido in lista_nombres_apellidos if entrada in nombre_apellido.lower()]

            # Borra los elementos actuales en la lista de resultados
            lista_resultados.delete(0, tk.END)

            # Agrega los nuevos resultados filtrados a la lista
            for resultado in resultados_filtrados:
                lista_resultados.insert(tk.END, resultado)

            # Muestra u oculta la lista de resultados en función de si hay resultados
            if not resultados_filtrados or self.entry.get() == "":
                lista_resultados.pack_forget()
                print("algo")
            else:
                lista_resultados.pack(pady=10)
                # Ajusta la altura de la lista de resultados
                lista_resultados.config(height=len(resultados_filtrados))
                print("algo")

    # Lista de nombres y apellidos (puedes cargarla desde una base de datos o cualquier otra fuente)
    lista_nombres_apellidos = ["Juan Pérez", "María García", "Luis Rodríguez", "Ana Martínez", "Pedro López", "Laura Sánchez"]

    # Crear un cuadro de entrada personalizado (CustomEntry)
    self.entry = customtkinter.CTkEntry(self, placeholder_text="Input")
    self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")
    self.main_button_1 = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
    self.main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

    # Crear una lista para mostrar los resultados
    lista_resultados = tk.Listbox(self)
    CustomEntry(self)

def mostrarResultados(self):
    conexion = sqlite3.connect("BaseDatos.db")
    cursor = conexion.cursor()

    # Consultar la base de datos para obtener la lista
    cursor.execute("SELECT Nombre || ' ' || Apellido || ' ' || Documento AS NombreCompleto FROM Clientes")
    resultados = cursor.fetchall()
    lista_resultante = [tupla[0] for tupla in resultados]

    def actualizar_resultados():
        # Obtiene la entrada actual del cuadro de texto
        entrada = self.entry.get()
        # Filtra la lista de nombres y apellidos en función de la entrada
        resultados_filtrados = [nombre_apellido for nombre_apellido in lista_resultante if entrada in nombre_apellido.lower()]
        resultados_filtrados = resultados_filtrados[:4]
        # Borra los elementos actuales en la lista de resultados
        lista_resultados.delete(0, tk.END)
        # Agrega los nuevos resultados filtrados a la lista
        for resultado in resultados_filtrados:
            lista_resultados.insert(tk.END, resultado)
        # Muestra u oculta la lista de resultados en función de si hay resultados
        # Muestra u oculta la lista de resultados en función de si hay resultados
        if not resultados_filtrados or self.entry.get() == "":
            lista_resultados.grid_forget()  # Cambiado a grid_forget
        else:
            lista_resultados.grid(row=3, column=2, padx=(0, 0), pady=5, sticky="nsew")  # Cambiado a grid
            # Ajusta la altura de la lista de resultados
            lista_resultados.config(height=len(resultados_filtrados))
        # Programa la próxima ejecución de la función después de 100 milisegundos
        self.after(100, actualizar_resultados)
    global lista_resultados
    
    # Crear una lista para mostrar los resultados
    lista_resultados = tk.Listbox(self)
    lista_resultados.config(width=20, height=5)  # Configurar el ancho y alto de la lista de resultados
    # Crear un cuadro de entrada personalizado (CustomEntry)
    self.entry = customtkinter.CTkEntry(self, placeholder_text="Input")
    self.entry.grid(row=3, column=0, padx=(20, 20), pady=(20, 20), sticky="nsew")
    self.main_button_1 = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
    self.main_button_1.grid(row=3, column=1, padx=(20, 20), pady=(20, 20), sticky="nsew")
    actualizar_resultados()
    conexion.close()