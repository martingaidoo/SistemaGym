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
import requests
from datetime import datetime, timedelta
import os
import sys

banderaVencimiento = False

def controlAcceso(self):
        conexion = sqlite3.connect("BaseDatos.db")
        cursor = conexion.cursor()
        # Consultar la base de datos para obtener la lista
        cursor.execute("SELECT Nombre || ' ' || Apellido || ' ' || Documento AS NombreCompleto FROM Clientes")
        resultados = cursor.fetchall()
        lista_resultante = [tupla[0] for tupla in resultados]
        def mostrar_seleccion2(event):
            selected_indices = lista_resultados_asistencia.curselection()
            
            if selected_indices:
                selected_item = lista_resultados_asistencia.get(selected_indices[0])
                entry_asistencia.delete(0, tk.END)  # Limpiar el contenido actual
                entry_asistencia.insert(0, selected_item[-8:])

        def actualizar_resultados2():
            # Obtiene la entrada actual del cuadro de texto
            entrada = entry_asistencia.get()
            # Filtra la lista de nombres y apellidos en función de la entrada
            resultados_filtrados = [nombre_apellido for nombre_apellido in lista_resultante if entrada in nombre_apellido.lower()]
            resultados_filtrados = resultados_filtrados[:4]
            # Borra los elementos actuales en la lista de resultados
            lista_resultados_asistencia.delete(0, tk.END)
            # Agrega los nuevos resultados filtrados a la lista
            for resultado in resultados_filtrados:
                lista_resultados_asistencia.insert(tk.END, resultado)
            # Muestra u oculta la lista de resultados en función de si hay resultados
            if not resultados_filtrados or entry_asistencia.get() == "":
                lista_resultados_asistencia.grid_forget()  # Cambiado a grid_forget
            else:
                lista_resultados_asistencia.grid(row=4, column=1, pady=(20, 0), sticky="nsew")  # Cambiado a grid
                # Ajusta la altura de la lista de resultados
                lista_resultados_asistencia.config(height=len(resultados_filtrados))
            # Programa la próxima ejecución de la función después de 100 milisegundos
            self.after(100, actualizar_resultados2)
        global lista_resultados_asistencia


        self.frame_asistencia = customtkinter.CTkFrame(self, width=250)
        self.frame_asistencia.grid(row=0, rowspan=2, column=1,columnspan=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.frame_asistencia.grid_columnconfigure((0,2), weight=2)
        self.frame_asistencia.grid_columnconfigure(1, weight=0)
        self.frame_asistencia.grid_rowconfigure((0, 1,2,3,4), weight=0)

        lista_resultados_asistencia = tk.Listbox(self.frame_asistencia)
        lista_resultados_asistencia.config(width=20, height=5)
        
        label_titulo = customtkinter.CTkLabel(self.frame_asistencia, text="CONTROL DE ACCESO", font=('Century Gothic',30))
        label_titulo.grid(row=0, column=1, pady=(20, 0), sticky="nsew")
        label_documento = customtkinter.CTkLabel(self.frame_asistencia, text="Documente:", font=('Century Gothic',15))
        label_documento.grid(row=1, column=1, pady=(20, 0), sticky="nsew")
        
        entry_asistencia = customtkinter.CTkEntry(self.frame_asistencia,
                                    width=500,
                                    height=25,
                                    corner_radius=10)
        entry_asistencia.grid(row=2, column=1, pady=(20, 0), sticky="nsew")
        button = customtkinter.CTkButton(self.frame_asistencia, width=220, text="CONFIRMAR", command=lambda: (registrarAsistencia(obtener_datos_cliente(entry_asistencia.get()),self),entry_asistencia.delete(0, tk.END)), corner_radius=6)
        button.grid(row=3, column=1, pady=(20, 0), sticky="nsew")
        #hace lo mismo que apretar el boton

        def funcion_al_presionar_tecla(event):
            if entry_asistencia.get() != "":
                registrarAsistencia(obtener_datos_cliente(entry_asistencia.get()),self),entry_asistencia.delete(0, tk.END)
        #ejecuta la funcion de arriba con apretar el enter
        actualizar_resultados2()
        self.bind("<Return>", funcion_al_presionar_tecla)
        lista_resultados_asistencia.bind("<<ListboxSelect>>", mostrar_seleccion2)


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

def actualizarClientes(self):
        self.frame_actualizarClientes = customtkinter.CTkFrame(self, width=250)
        self.frame_actualizarClientes.grid(row=0, rowspan=2, column=1,columnspan=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.frame_actualizarClientes.grid_columnconfigure((0,2), weight=1)
        self.frame_actualizarClientes.grid_columnconfigure(1, weight=0)
        self.frame_actualizarClientes.grid_rowconfigure((7), weight=1)
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


                self.label_Deuda = ctk.CTkLabel(frame, text="Deuda:")
                self.label_Deuda.grid(row=4, column=0)  #tienen mal el nombre de las entradas hay que arreglarlo@@@@@@@@@@@@@@@@@@@@@@@@@@
                self.Deuda_entry = ctk.CTkEntry(frame)
                self.Deuda_entry.grid(row=4, column=1)

                self.label_Plan = ctk.CTkLabel(frame, text="Plan:")
                self.label_Plan.grid(row=4, column=2) #tienen mal el nombre de las entradas hay que arreglarlo@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                self.Plan_entry = ctk.CTkEntry(frame)
                self.Plan_entry.grid(row=4, column=3)

                self.label_Fecha = ctk.CTkLabel(frame, text="Fecha inicio:")
                self.label_Fecha.grid(row=5, column=0)
                self.Fecha_entry = ctk.CTkEntry(frame)
                self.Fecha_entry.grid(row=5, column=1)

                self.label_Vencimiento = ctk.CTkLabel(frame, text="Vencimiento:")
                self.label_Vencimiento.grid(row=5, column=2)
                self.Vencimiento_entry = ctk.CTkEntry(frame)
                self.Vencimiento_entry.grid(row=5, column=3)


                # Crear botones
                self.btn_actualizar = ctk.CTkButton(frame, text="Actualizar", command=self.actualizar)
                self.btn_actualizar.grid(row=6, column=2)

                self.btn_vencido = ctk.CTkButton(frame, text="Vencido", command=lambda: (self.mostrar_programas(), cambiar()))
                self.btn_vencido.grid(row=6, column=0)


                # Crear una lista para mostrar los datos de la base de datos
                self.lista_programas = tk.Listbox(frame)
                self.lista_programas.grid(row=7, column=0, columnspan=4, sticky=tk.W + tk.E + tk.N + tk.S)
                self.mostrar_programas()

                # Asignar una función para manejar la selección en la lista
                self.lista_programas.bind('<<ListboxSelect>>', self.seleccionar_programa)



                def cambiar():
                    global banderaVencimiento
                    banderaVencimiento = not (banderaVencimiento)

            def mostrar_programas(self):
                self.lista_programas.delete(0, ctk.END)
                programas = self.cursor.execute('SELECT * FROM Clientes').fetchall()
                for programa in programas:
                    id, nombre, apellido, correo, documento, fechaNacimiento, telefono, Estado = programa  # Obtener los dos últimos elementos de la tupla
                    if int(Estado) == 1:
                        consulta = """
                        SELECT * FROM Cuotas id_cliente WHERE id_cliente = ?;
                        """
                        self.cursor.execute(consulta, (id,)) 
                        datos_cuota = self.cursor.fetchone()
                        if banderaVencimiento == False:
                            if datos_cuota:
                                idCuota,deuda,plan,profesor,inicio,vencimiento,idCliente,idProfesor = datos_cuota
                                self.lista_programas.insert(ctk.END, (apellido, nombre, documento, correo, fechaNacimiento, telefono, deuda, plan, inicio,vencimiento))
                            else:
                                deuda=""
                                plan=""
                                inicio=""
                                vencimiento=""
                                self.lista_programas.insert(ctk.END, (apellido, nombre, documento, correo, fechaNacimiento, telefono, deuda, plan, inicio,vencimiento))
                        if banderaVencimiento == True:
                            if datos_cuota:
                                fecha_actual = datetime.strptime(actual, "%d/%m/%Y")
                                fecha_vencimiento = datetime.strptime(datos_cuota[5], "%d/%m/%Y")
                                if fecha_actual >= fecha_vencimiento:
                                    idCuota,deuda,plan,profesor,inicio,vencimiento,idCliente,idProfesor = datos_cuota
                                    self.lista_programas.insert(ctk.END, (apellido, nombre, documento, correo, fechaNacimiento, telefono, deuda, plan, inicio,vencimiento))


            def actualizar(self):
                apellido = self.Apellido_entry.get()
                nombre = self.nombre_entry.get()
                correo = self.Correo_entry.get()
                documento = self.Documento_entry.get()
                fechaNacimiento = self.FechaNacimiento_entry.get()
                telefono = self.Telefono_entry.get()

                deuda = self.Deuda_entry.get()
                fecha = self.Fecha_entry.get()
                vencimiento = self.Vencimiento_entry.get()
                plan = self.Plan_entry.get()

                consulta = """SELECT * FROM Clientes WHERE Apellido = ? AND Nombre = ?;"""
                self.cursor.execute(consulta, (apellido, nombre))
                cliente = self.cursor.fetchone()

                if apellido and nombre and correo and documento and fechaNacimiento and telefono and deuda != "" and fecha != "" and vencimiento != "" and plan != "":
                    self.cursor.execute("UPDATE Clientes SET Apellido=?, Nombre=?, Correo=?, Telefono=?, Fecha_Nacimiento=? WHERE Documento=?",
                                        (apellido, nombre, correo, telefono, fechaNacimiento, documento))
                    self.conexion.commit()

                    self.cursor.execute("UPDATE Cuotas SET Haber=?, PLAN=?, Fecha=?, Vencimiento=? WHERE id=?",
                                        (deuda,plan, fecha, vencimiento, cliente[0]))
                    self.conexion.commit()
                    
                    self.mostrar_programas()
                    self.limpiar_campos()
                elif apellido and nombre and correo and documento and fechaNacimiento and telefono and deuda == "" and fecha == "" and vencimiento == "" and plan == "":
                    self.cursor.execute("UPDATE Clientes SET Apellido=?, Nombre=?, Correo=?, Telefono=?, Fecha_Nacimiento=? WHERE Documento=?",
                                        (apellido, nombre, correo, telefono, fechaNacimiento, documento))
                    self.conexion.commit()
                    self.mostrar_programas()
                    self.limpiar_campos()

            def seleccionar_programa(self, event):
                programa = self.lista_programas.get(self.lista_programas.curselection())
                nombre, apellido, correo,documento , fechaNacimiento, telefono, deuda, plan, inicio,vencimiento = programa
                
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

                self.Deuda_entry.delete(0, ctk.END)
                self.Deuda_entry.insert(0, deuda)
                self.Plan_entry.delete(0, ctk.END)
                self.Plan_entry.insert(0, plan)
                self.Fecha_entry.delete(0, ctk.END)
                self.Fecha_entry.insert(0, inicio)
                self.Vencimiento_entry.delete(0, tk.END)
                self.Vencimiento_entry.insert(0, vencimiento)

            def limpiar_campos(self):
                self.Apellido_entry.delete(0, ctk.END)
                self.nombre_entry.delete(0, ctk.END)
                self.FechaNacimiento_entry.delete(0, tk.END)
                self.Correo_entry.delete(0, ctk.END)
                self.Documento_entry.delete(0, ctk.END)
                self.Telefono_entry.delete(0, ctk.END)
                self.Deuda_entry.delete(0, ctk.END)
                self.Fecha_entry.delete(0, ctk.END)
                self.Vencimiento_entry.delete(0, ctk.END)
                self.Plan_entry.delete(0, ctk.END)

            def __del__(self):
                self.conexion.close()

        ProgramaABM_Clientes(self.frame_actualizarClientes)


def pagoCuotas(self):
        conexion = sqlite3.connect("BaseDatos.db")
        cursor = conexion.cursor()
        # Consultar la base de datos para obtener la lista
        cursor.execute("SELECT Nombre || ' ' || Apellido || ' ' || Documento AS NombreCompleto FROM Clientes")
        resultados = cursor.fetchall()
        lista_resultante = [tupla[0] for tupla in resultados]
        def mostrar_seleccion3(event):
            selected_indices = lista_resultados_pago.curselection()
            
            if selected_indices:
                selected_item = lista_resultados_pago.get(selected_indices[0])
                entry_cliente.delete(0, tk.END)  # Limpiar el contenido actual
                entry_cliente.insert(0, selected_item[-8:])

        def actualizar_resultados3():
            # Obtiene la entrada actual del cuadro de texto
            entrada = entry_cliente.get()
            # Filtra la lista de nombres y apellidos en función de la entrada
            resultados_filtrados = [nombre_apellido for nombre_apellido in lista_resultante if entrada in nombre_apellido.lower()]
            resultados_filtrados = resultados_filtrados[:4]
            # Borra los elementos actuales en la lista de resultados
            lista_resultados_pago.delete(0, tk.END)
            # Agrega los nuevos resultados filtrados a la lista
            for resultado in resultados_filtrados:
                lista_resultados_pago.insert(tk.END, resultado)
            # Muestra u oculta la lista de resultados en función de si hay resultados
            if not resultados_filtrados or entry_cliente.get() == "":
                lista_resultados_pago.grid_forget()  # Cambiado a grid_forget
            else:
                lista_resultados_pago.grid(row=2, column=2, pady=(0, 0), sticky="nsew")  # Cambiado a grid
                # Ajusta la altura de la lista de resultados
                lista_resultados_pago.config(height=len(resultados_filtrados))
            # Programa la próxima ejecución de la función después de 100 milisegundos
            self.after(100, actualizar_resultados3)

        self.frame_pagoCuota = customtkinter.CTkFrame(self, width=250)
        self.frame_pagoCuota.grid(row=0, rowspan=2, column=1,columnspan=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.frame_pagoCuota.grid_columnconfigure((0,2), weight=1)
        self.frame_pagoCuota.grid_columnconfigure(1, weight=0)
        self.frame_pagoCuota.grid_rowconfigure((0, 1, 2), weight=0)

        global lista_resultados_pago
        lista_resultados_pago = tk.Listbox(self.frame_pagoCuota)
        lista_resultados_pago.config(width=20, height=5)

    #LABEL TITULO
        label_titulo = customtkinter.CTkLabel(self.frame_pagoCuota, text="PAGO DE CUOTA", font=('Century Gothic',20))
        label_titulo.grid(row=0, column=1, padx=(0, 0), pady=(10, 0), sticky="nsew")

        #Entradas
        label_cliente = customtkinter.CTkLabel(self.frame_pagoCuota, text="documento", font=('Century Gothic',15))
        label_cliente.grid(row=1, column=1, padx=(0, 0), pady=(10, 0), sticky="nsew")

        entry_cliente = customtkinter.CTkEntry(self.frame_pagoCuota, width=220, height=25, corner_radius=10)
        entry_cliente.grid(row=2, column=1, padx=(0, 0), pady=(10, 0), sticky="nsew")

        label_programa = customtkinter.CTkLabel(self.frame_pagoCuota, text="Programa", font=('Century Gothic',15))
        label_programa.grid(row=3, column=1, padx=(0, 0), pady=(10, 0), sticky="nsew")

        conexion = sqlite3.connect('BaseDatos.db')
        cursor = conexion.cursor()

        #menu_desplegable = ttk.Combobox(self.frame_pagoCuota, width=35, height=25)

        # Obtener los nombres de los clientes desde la base de datos
        cursor.execute("SELECT Nombre FROM Programa")
        nombres = cursor.fetchall()
        lista_nombres = [tupla[0] for tupla in nombres]

        # Agregar los nombres al menú desplegable
        menu_desplegable = customtkinter.CTkComboBox(self.frame_pagoCuota, values=lista_nombres, variable="")

        # Mostrar el menú desplegable
        menu_desplegable.grid(row=4, column=1, padx=(0, 0), pady=(10, 0), sticky="nsew")

        label_vencimiento = customtkinter.CTkLabel(self.frame_pagoCuota, text="Vencimiento", font=('Century Gothic',15))
        label_vencimiento.grid(row=5, column=1, padx=(0, 0), pady=(10, 0), sticky="nsew")

        # Agregar los nombres al menú desplegable
        lista_vencimiento = ["Fecha actual", "Ultimo vencimiento"]

        menu_vencimiento = customtkinter.CTkComboBox(self.frame_pagoCuota, values=lista_vencimiento, variable="")

        # Mostrar el menú desplegable
        menu_vencimiento.grid(row=6, column=1, padx=(0, 0), pady=(10, 0), sticky="nsew")


        label_pago = customtkinter.CTkLabel(self.frame_pagoCuota, text="Pago $", font=('Century Gothic',15))
        label_pago.grid(row=7, column=1, padx=(0, 0), pady=(10, 0), sticky="nsew")
        entry_pago = customtkinter.CTkEntry(self.frame_pagoCuota, width=120, height=25, corner_radius=10)
        entry_pago.grid(row=8, column=1, padx=(0, 0), pady=(10, 0), sticky="nsew")

        label_profesor = customtkinter.CTkLabel(self.frame_pagoCuota, text="Profesor", font=('Century Gothic',15))
        label_profesor.grid(row=9, column=1, padx=(0, 0), pady=(10, 0), sticky="nsew")
        entry_profesor = customtkinter.CTkEntry(self.frame_pagoCuota, width=220, height=25, corner_radius=10)
        entry_profesor.grid(row=10, column=1, padx=(0, 0), pady=(10, 0), sticky="nsew")

        button_confirmar = customtkinter.CTkButton(
            self.frame_pagoCuota,
            width=220,
            text="Confirmar",
            command=lambda: (registrarPago([entry_cliente.get(), entry_pago.get(), menu_desplegable.get(), entry_profesor.get(), menu_vencimiento.get()]), self.frame_pagos.pack(pady=60),self.frame_pagoCuota.pack_forget()),corner_radius=6)
        button_confirmar.grid(row=11, column=1, padx=(0, 0), pady=(10, 0), sticky="nsew")
        
        actualizar_resultados3()
        lista_resultados_pago.bind("<<ListboxSelect>>", mostrar_seleccion3)

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
    
    def mostrar_seleccion(event):
        selected_indices = lista_resultados.curselection()
        if selected_indices:
            selected_item = lista_resultados.get(selected_indices[0])
            self.entry.delete(0, tk.END)  # Limpiar el contenido actual
            self.entry.insert(0, selected_item)

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
    self.entry = customtkinter.CTkEntry(self, placeholder_text="buscar ficha")
    self.entry.grid(row=3, column=0, padx=(20, 20), pady=(20, 20), sticky="nsew")
    self.main_button_1 = customtkinter.CTkButton(master=self,text="Buscar", fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), command=lambda:(fichacliente(self.entry.get()[-8:])))
    self.main_button_1.grid(row=3, column=1, padx=(20, 20), pady=(20, 20), sticky="nsew")
    
    actualizar_resultados()

    lista_resultados.bind("<<ListboxSelect>>", mostrar_seleccion)

    conexion.close()


def fichacliente(documento):
    cliente , cuota =buscar_cliente_con_cuotas(documento)
    fecha_actual = datetime.now()
    fecha_nacimiento = datetime.strptime(cliente[5], "%d/%m/%Y")
    fecha_actual = datetime.strptime(actual, "%d/%m/%Y")
    edad = fecha_actual.year - fecha_nacimiento.year - ((fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    
    def darAltaBaja(valor, id_cli):
        conexion = sqlite3.connect("BaseDatos.db")
        cursor = conexion.cursor()
        if valor:
            cursor.execute("UPDATE Clientes SET Estado = ? WHERE id = ?",
                    ("1", id_cli))
            conexion.commit()
        else:
            cursor.execute("UPDATE Clientes SET Estado = ? WHERE id = ?",
                    ("0", id_cli))
            conexion.commit()

    class aplicacion(ctk.CTk):
        def __init__(self):
                super().__init__()

                # configure window
                self.title("Gym Master")
                self.geometry(f"{900}x{500}")
                self.overrideredirect(True)
                self.configure(highlightthickness=2, highlightbackground="black")
                
                # configure la ventada grid(4x4)
                self.grid_columnconfigure(1, weight=1)
                self.grid_columnconfigure((2, 3), weight=0)
                self.grid_rowconfigure((0, 1, 2), weight=1)

                #frame de arriba

                self.buscarFichas_frame = customtkinter.CTkFrame(self, width=20, corner_radius=0)
                self.buscarFichas_frame.grid(row=0, column=0, columnspan=4, pady=(0, 10), sticky="nsew")
                self.buscarFichas_frame.grid_columnconfigure(0, weight=1)

                label = customtkinter.CTkLabel(self.buscarFichas_frame, text="FICHA DEL SOCIO", fg_color="transparent",text_color="blue",font=customtkinter.CTkFont(size=20, weight="bold"))
                label.grid(row=0, column=0,columnspan=3, pady=(10, 10), sticky="nsew")

                boton_cierre = customtkinter.CTkButton(self.buscarFichas_frame, text="Cerrar", command=lambda:(self.destroy()), fg_color= "red", hover_color="#FF5555")
                boton_cierre.grid(row=0, column=4, sticky="nsew")

                # frame de la izquierda
                #img_persona = customtkinter.CTkImage(light_image=Image.open("./assets/personaLight2.png"),
                #                        dark_image=Image.open("./assets/personaDark2.png"),
                #                        size=(200, 200))
                

                self.sidebar_frame = customtkinter.CTkFrame(self, width=140)
                self.sidebar_frame.grid(row=1, column=0, rowspan=2, padx=(10, 10), pady=(10, 10) , sticky="nsew")

                #persona = customtkinter.CTkLabel(self.sidebar_frame, image=img_persona, text="")  # "w" significa alinear a la izquierda
                #persona.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="nsew")

                boton_tomarFoto = customtkinter.CTkButton(self.sidebar_frame, text="Tomar Foto", command=lambda:())
                boton_tomarFoto.grid(row=1, column=0,padx=(10, 10), pady=(10, 5), sticky="nsew")

                boton_INFORMACIONmEDICA = customtkinter.CTkButton(self.sidebar_frame, text="Informacion Medica", command=lambda:())
                boton_INFORMACIONmEDICA.grid(row=2, column=0,padx=(10, 10), pady=(10, 5), sticky="nsew")
                

                #frame del medio
                self.mensajes = customtkinter.CTkFrame(self, width=250)
                self.mensajes.grid(row=1, rowspan=2, column=1,columnspan=2, padx=(10, 10), pady=(10, 10), sticky="nsew")
                self.mensajes.grid_columnconfigure(2, weight=1)
                self.mensajes.grid_columnconfigure((1, 0), weight=0)


                label_nombre = customtkinter.CTkLabel(self.mensajes, text="Nombre:", fg_color="transparent", text_color= "blue")
                label_nombre.grid(row=0, column=0, padx=(10, 10), pady=(5, 5), sticky="nsew")

                label_nombre_seleccion = customtkinter.CTkLabel(self.mensajes, text=cliente[2] + " " + cliente[1] , fg_color="transparent")
                label_nombre_seleccion.grid(row=0, column=1, padx=(10, 10), pady=(5, 5), sticky="nsew")

                label_documento = customtkinter.CTkLabel(self.mensajes, text="Documento:", fg_color="transparent", text_color= "blue")
                label_documento.grid(row=1, column=0, padx=(10, 10), pady=(5, 5), sticky="nsew")

                label_documento_seleccion = customtkinter.CTkLabel(self.mensajes, text=cliente[3], fg_color="transparent")
                label_documento_seleccion.grid(row=1, column=1, padx=(10, 10), pady=(5, 5), sticky="nsew")

                label_fecha_nacimiento = customtkinter.CTkLabel(self.mensajes, text="Fecha de Nacimiento:", fg_color="transparent", text_color= "blue")
                label_fecha_nacimiento.grid(row=2, column=0, padx=(40, 10), pady=(5, 5), sticky="nsew")

                label_fecha_nacimiento_seleccion = customtkinter.CTkLabel(self.mensajes, text=cliente[5], fg_color="transparent")
                label_fecha_nacimiento_seleccion.grid(row=2, column=1, padx=(40, 10), pady=(5, 5), sticky="nsew")

                label_edad = customtkinter.CTkLabel(self.mensajes, text="Edad:", fg_color="transparent", text_color= "blue")
                label_edad.grid(row=3, column=0, padx=(10, 10), pady=(5, 5), sticky="nsew")

                label_edad_seleccion = customtkinter.CTkLabel(self.mensajes, text=edad, fg_color="transparent")
                label_edad_seleccion.grid(row=3, column=1, padx=(40, 10), pady=(5, 5), sticky="nsew")

                label_Mail = customtkinter.CTkLabel(self.mensajes, text="Mail:", fg_color="transparent", text_color= "blue")
                label_Mail.grid(row=4, column=0, padx=(10, 10), pady=(5, 5), sticky="nsew")

                label_mail_seleccion = customtkinter.CTkLabel(self.mensajes, text=cliente[4], fg_color="transparent")
                label_mail_seleccion.grid(row=4, column=1, padx=(40, 10), pady=(5, 5), sticky="nsew")

                label_Telefono = customtkinter.CTkLabel(self.mensajes, text="Telefono:", fg_color="transparent", text_color= "blue")
                label_Telefono.grid(row=5, column=0, padx=(10, 10), pady=(5, 5), sticky="nsew")

                label_telefono_seleccion = customtkinter.CTkLabel(self.mensajes, text=cliente[6], fg_color="transparent")
                label_telefono_seleccion.grid(row=5, column=1, padx=(10, 10), pady=(5, 5), sticky="nsew")

                label_ebservacion = customtkinter.CTkLabel(self.mensajes, text="Observacion:", fg_color="transparent", text_color= "blue")
                label_ebservacion.grid(row=6, column=0, padx=(10, 10), pady=(5, 5), sticky="nsew")

                label_observacion_seleccion = customtkinter.CTkLabel(self.mensajes, text="---", fg_color="transparent")
                label_observacion_seleccion.grid(row=6, column=1, padx=(10, 10), pady=(5, 5), sticky="nsew")


                # frame de la derecha
                self.derecha_frame = customtkinter.CTkFrame(self, width=140)
                self.derecha_frame.grid(row=1, column=3,rowspan=2, padx=(10, 10), pady=(10, 10), sticky="nsew")
                self.derecha_frame.grid_columnconfigure(0, weight=1)
                boton_asistencias = customtkinter.CTkButton(self.derecha_frame, text="Ver asistencias", command=lambda:())
                boton_asistencias.grid(row=0, column=0,padx=(10, 10), pady=(30, 10), sticky="nsew")
                boton_pagos = customtkinter.CTkButton(self.derecha_frame, text="Ver pagos", command=lambda:())
                boton_pagos.grid(row=1, column=0,padx=(10, 10), pady=(10, 10), sticky="nsew")
                boton_verplanes = customtkinter.CTkButton(self.derecha_frame, text="Ver rutinas", command=lambda:())
                boton_verplanes.grid(row=3, column=0,padx=(10, 10), pady=(10, 10), sticky="nsew")
                boton_cobrar = customtkinter.CTkButton(self.derecha_frame, text="Cobrar Cuota", command=lambda:())
                boton_cobrar.grid(row=4, column=0,padx=(10, 10), pady=(10, 10), sticky="nsew")


                # freame de abajo
                self.buscarFichas_frame = customtkinter.CTkFrame(self, width=20, corner_radius=0)
                self.buscarFichas_frame.grid(row=3, column=0, columnspan=4, pady=(10, 0), sticky="nsew")

                self.buscarFichas_frame.grid_columnconfigure(1, weight=1)
                self.buscarFichas_frame.grid_columnconfigure((0, 2, 3), weight=0)
                self.buscarFichas_frame.grid_rowconfigure((0, 1, 2), weight=1)

                label_plan_realiza = customtkinter.CTkLabel(self.buscarFichas_frame, text="PLAN SELECCIONADO", fg_color="transparent",text_color="blue",font=customtkinter.CTkFont(size=20, weight="bold"))
                label_plan_realiza.grid(row=0, column=0,columnspan=3, padx=(10, 10), pady=(10, 10), sticky="nsew")

                label_plan = customtkinter.CTkLabel(self.buscarFichas_frame, text="PLAN", fg_color="gray")
                label_plan.grid(row=1, column=0, pady=(10, 10), sticky="nsew")
        
                label_planSeleccion = customtkinter.CTkLabel(self.buscarFichas_frame, text=cuota[2], fg_color="transparent")
                label_planSeleccion.grid(row=2, column=0, padx=(10, 10), pady=(10, 10), sticky="nsew")

                label_Vencimiento = customtkinter.CTkLabel(self.buscarFichas_frame, text="Vencimiento", fg_color="gray")
                label_Vencimiento.grid(row=1, column=1, pady=(10, 10), sticky="nsew")
                label_VencimientoSeleccion = customtkinter.CTkLabel(self.buscarFichas_frame, text=cuota[5], fg_color="transparent")
                label_VencimientoSeleccion.grid(row=2, column=1, padx=(10, 10), pady=(10, 10), sticky="nsew")

                label_Estado = customtkinter.CTkLabel(self.buscarFichas_frame, text="Estado", fg_color="gray")
                label_Estado.grid(row=1, column=2, pady=(10, 10), sticky="nsew")
                label_Estadoseleccion = customtkinter.CTkLabel(self.buscarFichas_frame, text="falta", fg_color="transparent")
                label_Estadoseleccion.grid(row=2, column=2, padx=(100, 100), pady=(10, 10), sticky="nsew")

                label_Deuda = customtkinter.CTkLabel(self.buscarFichas_frame, text="Deuda", fg_color="gray")
                label_Deuda.grid(row=1, column=3, pady=(10, 10), sticky="nsew")
                label_Deudaseleccion = customtkinter.CTkLabel(self.buscarFichas_frame, text=cuota[1], fg_color="transparent")
                label_Deudaseleccion.grid(row=2, column=3, padx=(100, 100), pady=(10, 10), sticky="nsew")
                
                if int(cliente[7]) == 1:
                    boton_baja = customtkinter.CTkButton(self.buscarFichas_frame, text="Dar de Baja", command=lambda:(darAltaBaja(False, cliente[0]), self.destroy()), fg_color="red", hover_color="#FF5555")
                    boton_baja.grid(row=4, column=0, padx=(10, 10), pady=(10, 10), sticky="nsew")
                else:
                    boton_alta = customtkinter.CTkButton(self.buscarFichas_frame, text="Dar de Alta", command=lambda:(darAltaBaja(True, cliente[0]), self.destroy()), fg_color="green", hover_color="#00FF00")
                    boton_alta.grid(row=4, column=0, padx=(10, 10), pady=(10, 10), sticky="nsew")





                self.center_window()
                
        def center_window(self):
            self.update_idletasks()
            width = self.winfo_width()
            height = self.winfo_height()
            x = (self.winfo_screenwidth() - width) // 2 + 50
            y = (self.winfo_screenheight() - height) // 2
            self.geometry(f"{width}x{height}+{x}+{y}")

    # Crear instancia de la aplicación y ejecutar el bucle de eventos
    ficha = aplicacion()
    ficha.mainloop()


def caja(self):
    self.frame_caja = customtkinter.CTkFrame(self, width=250)
    self.frame_caja.grid(row=0, rowspan=2, column=1,columnspan=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
    self.frame_caja.grid_columnconfigure(0, weight=1)
    self.frame_caja.grid_rowconfigure(3, weight=1)
    class TablaDatos:
        def __init__(self, frame):
            self.frame = frame
            # Conexión a la base de datos
            self.conexion = sqlite3.connect("BaseDatos.db")
            self.cursor = self.conexion.cursor()

            # Calendario para la fecha de inicio
            self.lbl_fecha_inicio = customtkinter.CTkLabel(frame, text="Fecha de inicio:")
            self.lbl_fecha_inicio.grid(column=0, row=0, padx=(70,70), pady=(20, 20))

            self.cal_inicio = Calendar(frame, date_pattern="yyyy-mm-dd", width=180, height=120)
            self.cal_inicio.grid(column=0, row=1, padx=(70,70), pady=(20, 20))

            # Calendario para la fecha final
            self.lbl_fecha_fin = customtkinter.CTkLabel(frame, text="Fecha de fin:", fg_color="transparent")
            self.lbl_fecha_fin.grid(column=1, row=0, padx=(70,70), pady=(20, 20))

            self.cal_fin = Calendar(frame, date_pattern="yyyy-mm-dd", width=180, height=120)
            self.cal_fin.grid(column=1, row=1, padx=(70,70), pady=(20, 20))

            # Botón para actualizar la tabla
            self.btn_actualizar = customtkinter.CTkButton(frame, text="Actualizar", command=self.actualizar_tabla)
            self.btn_actualizar.grid(column=0, columnspan=2, row=2, padx=(20,20), pady=(20, 20))

            # Crear tabla
            self.tree = ttk.Treeview(frame, columns=("Nombre", "Cobro", "Fecha", "Profesor"), show="headings")
            self.tree.heading("Nombre", text="Nombre")
            self.tree.heading("Cobro", text="Cobro")
            self.tree.heading("Fecha", text="Fecha")
            self.tree.heading("Profesor", text="Profesor")
            self.tree.grid(column=0, columnspan=2, row=3, sticky="nsew")

            # Obtener datos de la base de datos
            self.obtener_datos()

        def obtener_datos(self):
            # Obtener fechas seleccionadas
            print("entreee")
            fecha_inicio = self.cal_inicio.get_date()
            fecha_fin = self.cal_fin.get_date()

            # Ejecutar consulta para obtener datos de la tabla Cobro en el rango de fechas
            self.cursor.execute("SELECT id_cliente, cobro, fecha, profesor  FROM Cobro ORDER BY fecha DESC")

            # Limpiar tabla antes de actualizar
            for row in self.tree.get_children():
                self.tree.delete(row)

            # Recorrer resultados y añadirlos a la tabla en orden inverso
            for row in reversed(self.cursor.fetchall()):
                # Buscar el nombre del cliente usando el id_cliente

                fecha1_datetime = datetime.strptime(fecha_inicio, "%Y-%m-%d")
                fecha2_datetime = datetime.strptime(fecha_fin, "%Y-%m-%d")
                fechaCobro = datetime.strptime(row[2], "%d/%m/%Y")          
                if fecha1_datetime <= fechaCobro <= fecha2_datetime:
                    id_cliente = row[0]
                    self.cursor.execute("SELECT Nombre, Apellido FROM Clientes WHERE id=?", (id_cliente,))
                    nombre_cliente, apellido_cliente = self.cursor.fetchone()
                    nombre_completo = nombre_cliente + " " + apellido_cliente
                    # Añadir datos a la tabla
                    self.tree.insert("", 0, values=(nombre_completo, row[1], row[2], row[3]))

        def actualizar_tabla(self):
            # Obtener y actualizar datos según el rango de fechas seleccionado
            self.obtener_datos()
    TablaDatos(self.frame_caja)

def asistencias(self):
    self.frame_asistencia = customtkinter.CTkFrame(self, width=250)
    self.frame_asistencia.grid(row=0, rowspan=2, column=1,columnspan=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
    self.frame_asistencia.grid_columnconfigure(0, weight=1)
    self.frame_asistencia.grid_rowconfigure(3, weight=1)

    class TablaDatos:
        def __init__(self,frame):

            self.frame = frame

            # Conexión a la base de datos
            self.conexion = sqlite3.connect("BaseDatos.db")
            self.cursor = self.conexion.cursor()


            # Calendario para la fecha de inicio
            self.lbl_fecha_inicio = customtkinter.CTkLabel(frame, text="Fecha de inicio:")
            self.lbl_fecha_inicio.grid(column=0, row=0, padx=(20,20), pady=(20, 20))

            self.cal_inicio = Calendar(frame, date_pattern="yyyy-mm-dd", width=180, height=120)
            self.cal_inicio.grid(column=0, row=1, padx=(20,20), pady=(20, 20))

            # Calendario para la fecha final
            self.lbl_fecha_fin = customtkinter.CTkLabel(frame, text="Fecha de fin:", fg_color="transparent")
            self.lbl_fecha_fin.grid(column=1, row=0, padx=(20,20), pady=(20, 20))

            self.cal_fin = Calendar(frame, date_pattern="yyyy-mm-dd", width=180, height=120)
            self.cal_fin.grid(column=1, row=1, padx=(20,20), pady=(20, 20))

            entry = customtkinter.CTkEntry(frame, placeholder_text="Documento")
            entry.grid(column=0, row=2, padx=(20,20), pady=(20, 20))

            # Botón para actualizar la tabla
            self.btn_actualizar = customtkinter.CTkButton(frame, text="Actualizar", command=lambda: (self.actualizar_tabla(entry.get())))
            self.btn_actualizar.grid(column=1, row=2, padx=(20,20), pady=(20, 20))

            # Crear tabla
            self.tree = ttk.Treeview(frame, columns=("Nombre", "Fecha", "Hora", "Estado"), show="headings")
            self.tree.heading("Nombre", text="Nombre")
            self.tree.heading("Fecha", text="Fecha")
            self.tree.heading("Hora", text="Hora")
            self.tree.heading("Estado", text="Estado")
            self.tree.grid(column=0, columnspan=2, row=3, sticky="nsew")

            # Obtener datos de la base de datos
            self.obtener_datos(entry.get())

        def obtener_datos(self, entradaDocumento):
            # Obtener fechas seleccionadas
            fecha_inicio = self.cal_inicio.get_date()
            fecha_fin = self.cal_fin.get_date()

            # Ejecutar consulta para obtener datos de la tabla Cobro en el rango de fechas
            self.cursor.execute("SELECT id, Cliente, Fecha FROM Asistencia ORDER BY fecha DESC")

            # Limpiar tabla antes de actualizar
            for row in self.tree.get_children():
                self.tree.delete(row)

            # Recorrer resultados y añadirlos a la tabla en orden inverso
            for row in reversed(self.cursor.fetchall()):
                # Buscar el nombre del cliente usando el id_cliente

                fecha1_datetime = datetime.strptime(fecha_inicio, "%Y-%m-%d")
                fecha2_datetime = datetime.strptime(fecha_fin, "%Y-%m-%d")
                fechaAsistencia, horaAsistencia = row[2].split()
                fechaAsistencia2 = datetime.strptime(fechaAsistencia, "%d/%m/%Y")
                horaAsistencia2 = datetime.strptime(horaAsistencia, "%H:%M:%S")

                if fecha1_datetime <= fechaAsistencia2 <= fecha2_datetime:
                    id_cliente = row[1]

                    self.cursor.execute("SELECT Nombre, Apellido, Documento FROM Clientes WHERE id=?", (id_cliente,))

                    nombre_cliente, apellido_cliente, documento= self.cursor.fetchone()

                    nombre_completo = nombre_cliente + " " + apellido_cliente
                    if entradaDocumento == "":
                        self.cursor.execute("SELECT Vencimiento FROM Cuotas WHERE id_cliente=?", (id_cliente,))
                        vencimiento = self.cursor.fetchone()
                        actual = datetime.now()
                        actualformateado_datetime = datetime.strptime(actual.strftime("%d/%m/%Y"), "%d/%m/%Y")
                        vencimientoformateado = datetime.strptime(vencimiento[0], "%d/%m/%Y")
                        if  vencimientoformateado >= actualformateado_datetime:
                            # Añadir datos a la tabla
                            self.tree.insert("", 0, values=(nombre_completo, fechaAsistencia, horaAsistencia, "Al dia"))
                        else:
                            self.tree.insert("", 0, values=(nombre_completo, fechaAsistencia, horaAsistencia, "Vencido"))
                    else:
                        if int(entradaDocumento) == int(documento):
                            self.cursor.execute("SELECT Vencimiento FROM Cuotas WHERE id_cliente=?", (id_cliente,))
                            vencimiento = self.cursor.fetchone()
                            actual = datetime.now()
                            actualformateado_datetime = datetime.strptime(actual.strftime("%d/%m/%Y"), "%d/%m/%Y")
                            vencimientoformateado = datetime.strptime(vencimiento[0], "%d/%m/%Y")
                            if  vencimientoformateado >= actualformateado_datetime:
                                # Añadir datos a la tabla
                                self.tree.insert("", 0, values=(nombre_completo, fechaAsistencia, horaAsistencia, "Al dia"))
                            else:
                                self.tree.insert("", 0, values=(nombre_completo, fechaAsistencia, horaAsistencia, "Vencido"))

        def actualizar_tabla(self, entradaDocumento):
            # Obtener y actualizar datos según el rango de fechas seleccionado
            self.obtener_datos(entradaDocumento)
    TablaDatos(self.frame_asistencia)



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

    # Iterar sobre los resultados y realizar el filtrado fuera de la consulta
    for fila in resultados:
        # Convertir la fecha de vencimiento de la cuota a un objeto datetime
        # Obtener la fecha de vencimiento de la cuota
        # Obtener la fecha de vencimiento de la cuota
        fecha_vencimiento_cuota = datetime.strptime(str(fila[-3]), "%d/%m/%Y")
        # Calcular la diferencia de días entre la fecha actual y la fecha de vencimiento de la cuota
        diferencia_dias = (fecha_vencimiento_cuota - fecha_actual).days
        # Si la diferencia es de 5 días o menos, añadir los datos del cliente y la cuota al array
        print(diferencia_dias)
        if 0 < diferencia_dias < 5:
            clientes_vencimiento_cercano.append(fila)

    for cliente_cuota_info in clientes_vencimiento_cercano:
        # Extraer la información necesaria de la tupla cliente_cuota_info

        numero_telefono = cliente_cuota_info[6]  # Número de teléfono del cliente
        fecha_vencimiento_cuota = cliente_cuota_info[-3]  # Fecha de vencimiento de la cuota

        # Construir el mensaje para el cliente
        mensaje = f"Su cuota vencerá en los próximos días, la fecha de vencimiento es {fecha_vencimiento_cuota}"

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



def whatsapp_api(self):
    url = 'http://localhost:3000/enviar-mensaje'
    data, info_cliente = conocerClientesPorVencer()

    def button_event():
        print("button pressed")
        response = requests.post(url, json=data)
        if response.status_code == 200:
            print("Solicitud POST exitosa")
            print("Respuesta del servidor:", response.json())
        else:
            print("Error al enviar la solicitud POST:", response.status_code)

    notificar = customtkinter.CTkScrollableFrame(self, label_text="Notificar")
    notificar.pack(pady=10)
    for i in info_cliente:
        etiqueta_notificacion = customtkinter.CTkLabel(notificar, text=f"{i[1]} {i[2]} - Vence pronto")
        etiqueta_notificacion.pack(fill="x", padx=0, pady=5)
    button = customtkinter.CTkButton(self, text="Enviar Mensaje", command=button_event)
    button.pack(pady=10)
