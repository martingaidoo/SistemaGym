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

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

fecha_actual = datetime.now()
actual = fecha_actual.strftime("%d/%m/%Y")

#import de utilerias de sqlite


conn = sqlite3.connect('BaseDatos.db') #vinculo la base de datos

cursor = conn.cursor() # este es mi curson que me permite realizar consultar y modificaciona a la bd

#se usa en la pantalla de consultar cuotas o clientes
banderaVencimiento = False
class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('COLUMBUS')
        self.iconbitmap("./assets/logo.ico")
        self.state('zoomed')        

        # fondo
        img1 = ImageTk.PhotoImage(Image.open("./assets/gym2.png"))
        l1 = customtkinter.CTkLabel(self, image=img1, text="")
        l1.place(x=0, y=0, relwidth=1, relheight=1)

# Inicializar todos los frames (uno para cada menú)
        self.frame_menu = customtkinter.CTkFrame(self)
        self.frame_clientes = customtkinter.CTkFrame(self)
        self.frame_pagos = customtkinter.CTkFrame(self)
        self.frame_pagoCuota = customtkinter.CTkFrame(self)
        self.frame_registrarCliente = customtkinter.CTkFrame(self)
        self.frame_actualizarClientes = customtkinter.CTkFrame(self)
        self.frame_actualizarPrecio = customtkinter.CTkFrame(self)
        self.frame_asistencia = customtkinter.CTkFrame(self)
        self.frame_consultarCuotas = customtkinter.CTkFrame(self)
        self.frame_consultarCuotasVencidas = customtkinter.CTkFrame(self)

# Llenar el menú
        
        frame = customtkinter.CTkFrame(master = self.frame_menu, width=300, height=300, corner_radius=15)
        frame.pack(pady=0)

        l2 = customtkinter.CTkLabel(frame, text="Bienvenido", font=('Century Gothic', 20))
        l2.place(relx=0.35, rely=0.1)

        # Botones
        button_Clientes = customtkinter.CTkButton(self.frame_menu, width=220, text="Clientes", command=lambda:(self.frame_clientes.pack(pady=60),self.frame_menu.pack_forget()), corner_radius=6)
        button_Clientes.place(relx=0.15, rely=0.3)

        button_pagoCuota = customtkinter.CTkButton(self.frame_menu, width=220, text="Pagos", command=lambda:(self.frame_pagos.pack(pady=60),self.frame_menu.pack_forget()), corner_radius=6)
        button_pagoCuota.place(relx=0.15, rely=0.5)

        button_cerrar = customtkinter.CTkButton(self.frame_menu, width=100, height=20, text="Cerrar", command=self.destroy, compound="left", fg_color='white', text_color='black', hover_color='#AFAFAF')
        button_cerrar.place(relx=0.34, rely=0.7)

# Llenar clientes
        frame = customtkinter.CTkFrame(master=self.frame_clientes, width=320, height=360, corner_radius=15)
        frame.pack(pady=0)

    # Cargar una imagen para volver atras
        imagen = ctk.CTkImage(light_image=PIL.Image.open("./assets/volver.png"),
                                dark_image=PIL.Image.open("./assets/volver.png"),
                                size=(30, 30))
        boton_con_imagen = ctk.CTkButton(self.frame_clientes, image=imagen,text="Volver", command=lambda:(self.frame_menu.pack(pady=70),self.frame_clientes.pack_forget()))
        boton_con_imagen.place(relx=0.03, rely=0.03)

        # Mensaje
        msjPrincipal = customtkinter.CTkLabel(frame, text="Mis Clientes", font=('Century Gothic', 20))
        msjPrincipal.place(x=100, y=70)
        
        button_registrarCliente = customtkinter.CTkButton(self.frame_clientes, width=220, text="REGISTRAR NUEVO CLIENTE", command=lambda: (self.frame_clientes.pack_forget(),self.frame_registrarCliente.pack()), corner_radius=6)
        button_registrarCliente.place(x=50, y=110)

        button_actualizarCliente = customtkinter.CTkButton(self.frame_clientes, width=220, text="ACTUALIZAR CLIENTE", command=lambda: (self.frame_clientes.pack_forget(),self.frame_actualizarClientes.pack(pady=60)), corner_radius=6)
        button_actualizarCliente.place(x=50, y=165)

        button_consultarCliente = customtkinter.CTkButton(self.frame_clientes, width=220, text="CONSULTAR CUOTAS", command=lambda: (self.frame_consultarCuotas.pack(pady=60),self.frame_clientes.pack_forget()), corner_radius=6)
        button_consultarCliente.place(x=50, y=220)

        button_generarexel = customtkinter.CTkButton(self.frame_clientes, width=220, text="GENERAR EXCEL CLIENTES", command=lambda: (generar_completo()), corner_radius=6)
        button_generarexel.place(x=50, y=275)

        

#llenar asistencia
        frame = customtkinter.CTkFrame(self.frame_asistencia, width=320, height=360)
        frame.pack(pady=0)
        imagen = ctk.CTkImage(light_image=PIL.Image.open("./assets/volver.png"),
                                dark_image=PIL.Image.open("./assets/volver.png"),
                                size=(30, 30))
        boton_con_imagen = ctk.CTkButton(self.frame_asistencia, image=imagen,text="Volver", command=lambda:(self.frame_pagos.pack(pady=60),self.frame_asistencia.pack_forget()))
        boton_con_imagen.place(relx=0.03, rely=0.03)

        label_titulo = customtkinter.CTkLabel(frame, text="ASISTENCIA", font=('Century Gothic',20))
        label_titulo.place(relx=0.3, rely=0.2)
        label_titulo = customtkinter.CTkLabel(frame, text="Documente:", font=('Century Gothic',15))
        label_titulo.place(relx=0.3, rely=0.4)
        
        entry_asistencia = customtkinter.CTkEntry(self.frame_asistencia,
                                    width=120,
                                    height=25,
                                    corner_radius=10)
        entry_asistencia.place(relx=0.3, rely=0.5)
        button = customtkinter.CTkButton(self.frame_asistencia, width=220, text="confirmar", command=lambda: (registrarAsistencia(obtener_datos_cliente(entry_asistencia.get())),entry_asistencia.delete(0, tk.END)), corner_radius=6)
        button.place(x=50, y=220)
        #hace lo mismo que apretar el boton
        def funcion_al_presionar_tecla(event):
            if entry_asistencia.get() != "":
                registrarAsistencia(obtener_datos_cliente(entry_asistencia.get())),entry_asistencia.delete(0, tk.END)
        #ejecuta la funcion de arriba con apretar el enter
        self.bind("<Return>", funcion_al_presionar_tecla)

#Llenar pagos
        frame = customtkinter.CTkFrame(master=self.frame_pagos, width=320, height=360, corner_radius=15)
        frame.pack(pady=0)

    # Cargar una imagen para volver atras
        imagen = ctk.CTkImage(light_image=PIL.Image.open("./assets/volver.png"),
                                dark_image=PIL.Image.open("./assets/volver.png"),
                                size=(30, 30))
        boton_con_imagen = ctk.CTkButton(self.frame_pagos, image=imagen,text="Volver", command=lambda:(self.frame_menu.pack(pady=70),self.frame_pagos.pack_forget()))
        boton_con_imagen.place(relx=0.03, rely=0.03)

        # Mensaje
        msjPrincipal = customtkinter.CTkLabel(frame, text="PAGOS", font=('Century Gothic', 20))
        msjPrincipal.place(x=130, y=70)

        button_registrarCliente = customtkinter.CTkButton(self.frame_pagos, width=220, text="PAGO DE CUOTA", command=lambda: (self.frame_pagos.pack_forget(),self.frame_pagoCuota.pack(pady=70)), corner_radius=6)
        button_registrarCliente.place(x=50, y=110)

        button_actualizarCliente = customtkinter.CTkButton(self.frame_pagos, width=220, text="ACTUALIZAR PLANES", command=lambda: (self.frame_pagos.pack_forget(),self.frame_actualizarPrecio.pack(pady=70)), corner_radius=6)
        button_actualizarCliente.place(x=50, y=165)

        button_consultarCliente = customtkinter.CTkButton(self.frame_pagos, width=220, text="ASISTENCIAS", command=lambda: (self.frame_asistencia.pack(pady=70), self.frame_pagos.pack_forget()), corner_radius=6)
        button_consultarCliente.place(x=50, y=220)

# llenar pagoCuota
        frame = customtkinter.CTkFrame(self.frame_pagoCuota, width=400, height=600, corner_radius=15)
        frame.pack(pady=0)

    # Cargar una imagen para volver atras
        imagen = ctk.CTkImage(light_image=PIL.Image.open("./assets/volver.png"),
                                dark_image=PIL.Image.open("./assets/volver.png"),
                                size=(30, 30))
        boton_con_imagen = ctk.CTkButton(self.frame_pagoCuota, image=imagen,text="Volver", command=lambda:(self.frame_pagos.pack(pady=60),self.frame_pagoCuota.pack_forget()))
        boton_con_imagen.place(relx=0.03, rely=0.03)

    #LABEL TITULO
        label_titulo = customtkinter.CTkLabel(master=frame, text="PAGO DE CUOTA", font=('Century Gothic',20))
        label_titulo.place(relx=0.34, rely=0.1)

        #Entradas
        label_cliente = customtkinter.CTkLabel(master=frame, text="documento", font=('Century Gothic',15))
        label_cliente.place(relx=0.40, rely=0.2)

        entry_cliente = customtkinter.CTkEntry(master=frame, width=220, height=25, corner_radius=10)
        entry_cliente.place(relx=0.5, rely=0.26, anchor=tk.CENTER)

        label_programa = customtkinter.CTkLabel(master=frame, text="Programa", font=('Century Gothic',15))
        label_programa.place(relx=0.44, rely=0.35)

        conexion = sqlite3.connect('BaseDatos.db')
        cursor = conexion.cursor()

        menu_desplegable = ttk.Combobox(master=frame, width=35, height=25)

        # Obtener los nombres de los clientes desde la base de datos
        cursor.execute("SELECT Nombre FROM Programa")
        nombres = cursor.fetchall()

        # Agregar los nombres al menú desplegable
        menu_desplegable['values'] = nombres

        #nombre_seleccionado = menu_desplegable.get()

        # Mostrar el menú desplegable
        menu_desplegable.place(relx=0.23, rely=0.4)


        label_pago = customtkinter.CTkLabel(master=frame, text="Pago $", font=('Century Gothic',15))
        label_pago.place(relx=0.44, rely=0.5)
        entry_pago = customtkinter.CTkEntry(master=frame, width=120, height=25, corner_radius=10)
        entry_pago.place(relx=0.5, rely=0.56, anchor=tk.CENTER)

        label_profesor = customtkinter.CTkLabel(master=frame, text="Profesor", font=('Century Gothic',15))
        label_profesor.place(relx=0.44, rely=0.64)
        entry_profesor = customtkinter.CTkEntry(master=frame, width=220, height=25, corner_radius=10)
        entry_profesor.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

        
        button_confirmar = customtkinter.CTkButton(
            master=frame,
            width=220,
            text="Confirmar",
            command=lambda: (registrarPago([entry_cliente.get(), entry_pago.get(), menu_desplegable.get()[1:len(menu_desplegable.get())-1], entry_profesor.get()]), self.frame_pagos.pack(pady=60),self.frame_pagoCuota.pack_forget()),corner_radius=6)
        button_confirmar.place(relx=0.25, rely=0.9)

# Llenar al registrar clientes
        frame = customtkinter.CTkFrame(master=self.frame_registrarCliente, width=800, height=800)
        frame.pack(pady=0)
    # Cargar una imagen para volver atras
        imagen = ctk.CTkImage(light_image=PIL.Image.open("./assets/volver.png"),
                                dark_image=PIL.Image.open("./assets/volver.png"),
                                size=(30, 30))
        boton_con_imagen = ctk.CTkButton(self.frame_registrarCliente, image=imagen,text="Volver", command=lambda:(self.frame_clientes.pack(pady=60),self.frame_registrarCliente.pack_forget()))
        boton_con_imagen.place(relx=0.03, rely=0.03)
        #LABEL TITULO
        label_titulo = customtkinter.CTkLabel(frame, text="Registrar clientes", font=('Century Gothic',20))
        label_titulo.place(relx=0.26, rely=0.03)

        #Entradas
        label_nombre = customtkinter.CTkLabel(frame, text="Nombre", font=('Century Gothic',15))
        label_nombre.place(relx=0.32, rely=0.1)
        entry_nombre = customtkinter.CTkEntry(self.frame_registrarCliente, width=120, height=25, corner_radius=10)
        entry_nombre.place(relx=0.5, rely=0.16, anchor=tk.CENTER)

        label_apellido = customtkinter.CTkLabel(frame, text="Apellido", font=('Century Gothic',15))
        label_apellido.place(relx=0.32, rely=0.2)
        entry_apellido = customtkinter.CTkEntry(self.frame_registrarCliente, width=120, height=25, corner_radius=10)
        entry_apellido.place(relx=0.5, rely=0.26, anchor=tk.CENTER)

        label_documento = customtkinter.CTkLabel(frame, text="Documento", font=('Century Gothic',15))
        label_documento.place(relx=0.32, rely=0.3)
        entry_documento = customtkinter.CTkEntry(self.frame_registrarCliente, width=120, height=25, corner_radius=10)
        entry_documento.place(relx=0.5, rely=0.36, anchor=tk.CENTER)

        label_correo = customtkinter.CTkLabel(frame, text="Correo", font=('Century Gothic',15))
        label_correo.place(relx=0.32, rely=0.4)
        entry_correo = customtkinter.CTkEntry(self.frame_registrarCliente, width=120, height=25, corner_radius=10)
        entry_correo.place(relx=0.5, rely=0.46, anchor=tk.CENTER)

        label_telefono = customtkinter.CTkLabel(frame, text="Telefono", font=('Century Gothic',15))
        label_telefono.place(relx=0.32, rely=0.5)
        entry_telefono = customtkinter.CTkEntry(self.frame_registrarCliente, width=120, height=25, corner_radius=10)
        entry_telefono.place(relx=0.5, rely=0.56, anchor=tk.CENTER)

        label_fechaNacimiento = customtkinter.CTkLabel(frame, text="Fecha de nacimiento", font=('Century Gothic',15)) # se ingresa ejemplo "año-mes-dia"
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


#llenar consultar clientes##############################################
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
                        cursor.execute(consulta, (id_cliente,)) 
                        cliente = cursor.fetchone()  
                        _, nombre, apellido, correo, documento, fechaNacimiento, telefono = cliente
                        self.lista_programas.insert(ctk.END, (apellido, nombre, haber, plan, fecha, vencimiento))
                if banderaVencimiento == True:
                    for cuota in cuotas:
                        fecha_actual = datetime.strptime(actual, "%d/%m/%Y")
                        fecha_vencimiento = datetime.strptime(cuota[5], "%d/%m/%Y")
                        if fecha_actual >= fecha_vencimiento:
                            id_cliente, haber, plan, profe, fecha, vencimiento, id_cliente2, id_programa = cuota  # Obtener los dos últimos elementos de la tupla
                            consulta = """SELECT * FROM Clientes WHERE id = ?;"""
                            cursor.execute(consulta, (id_cliente,)) 
                            cliente = cursor.fetchone()  
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
                cursor.execute(consulta, (apellido, nombre))
                cliente = cursor.fetchone()


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

        frame=customtkinter.CTkFrame(self.frame_consultarCuotas, width=1000, height=800, corner_radius=15)
        frame.pack(pady=10)

        # Cargar una imagen para volver atras
        imagen = ctk.CTkImage(light_image=PIL.Image.open("./assets/volver.png"),
                                dark_image=PIL.Image.open("./assets/volver.png"),
                                size=(30, 30))
        
        boton_con_imagen = ctk.CTkButton(self.frame_consultarCuotas, image=imagen,text="Volver", command=lambda:(self.frame_clientes.pack(pady=60),self.frame_consultarCuotas.pack_forget()))
        boton_con_imagen.pack(pady=10)

        ProgramaABM_cuotas(frame)



# Llenar el menu actualizar cliente
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
                    self.cursor.execute("UPDATE Clientes SET Apellido=?, Nombre=?, Correo=?, Documento=?, Fecha_Nacimiento=? WHERE Telefono=?",
                                        (apellido, nombre, correo, documento, fechaNacimiento, telefono))
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

        frame=customtkinter.CTkFrame(self.frame_actualizarClientes, width=1000, height=800, corner_radius=15)
        frame.pack(pady=10)

        # Cargar una imagen para volver atras
        imagen = ctk.CTkImage(light_image=PIL.Image.open("./assets/volver.png"),
                                dark_image=PIL.Image.open("./assets/volver.png"),
                                size=(30, 30))
        
        boton_con_imagen = ctk.CTkButton(master=self.frame_actualizarClientes, image=imagen,text="Volver", command=lambda:(self.frame_clientes.pack(pady=60),self.frame_actualizarClientes.pack_forget()))
        boton_con_imagen.pack(pady=10)

        ProgramaABM_Clientes(frame)

#llenar actualizar planes
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

        frame=customtkinter.CTkFrame(self.frame_actualizarPrecio, width=800, height=600)
        frame.pack(pady=10)

        # Cargar una imagen para volver atras
        imagen = ctk.CTkImage(light_image=PIL.Image.open("./assets/volver.png"),
                                dark_image=PIL.Image.open("./assets/volver.png"),
                                size=(30, 30))
        
        boton_con_imagen = ctk.CTkButton(master=self.frame_actualizarPrecio, image=imagen,text="Volver", command=lambda:(self.frame_pagos.pack(pady=60),self.frame_actualizarPrecio.pack_forget()))
        boton_con_imagen.pack(pady=10)

        ProgramaABM(frame)

        def recargar(event):
            self.destroy()
            python = sys.executable
            os.execl(python, python, *sys.argv)

        self.bind("<F5>", recargar)
        # Mostrar el primer menú al inicio
        self.frame_menu.pack(pady=70)

if __name__ == "__main__":
    app = VentanaPrincipal()
    app.mainloop()