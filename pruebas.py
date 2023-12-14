from tkinter import PhotoImage
import customtkinter
import customtkinter as ctk
from customtkinter import CTk, CTkFrame, CTkButton
import PIL.Image
from PIL import ImageTk,Image
from tkinter import *
import tkinter as tk
import pygame
import sqlite3
from tkcalendar import Calendar

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")
#import de utilerias de sqlite
from database_utils import agregar_cliente,registrarPago

conn = sqlite3.connect('BaseDatos.db') #vinculo la base de datos

cursor = conn.cursor() # este es mi curson que me permite realizar consultar y modificaciona a la bd
import tkinter as tk
from PIL import Image, ImageTk
import customtkinter

class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('SALUD INTEGRAL')
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

# Llenar el menú
        frame = customtkinter.CTkFrame(self.frame_menu, width=320, height=360, corner_radius=15)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        l2 = customtkinter.CTkLabel(self.frame_menu, text="Bienvenido", font=('Century Gothic', 20))
        l2.pack(pady=10)

        # Botones
        button_Clientes = customtkinter.CTkButton(master=self.frame_menu, width=220, text="Clientes", command=lambda:(self.frame_clientes.pack(),self.frame_menu.pack_forget()), corner_radius=6)
        button_Clientes.pack(pady=10)

        button_pagoCuota = customtkinter.CTkButton(master=self.frame_menu, width=220, text="Pagos", command=lambda:(self.frame_pagos.pack(),self.frame_menu.pack_forget()), corner_radius=6)
        button_pagoCuota.pack(pady=10)

        button_cerrar = customtkinter.CTkButton(master=self.frame_menu, width=100, height=20, text="Cerrar", command=self.destroy, compound="left", fg_color='white', text_color='black', hover_color='#AFAFAF')
        button_cerrar.pack(pady=10)

# Llenar clientes
        frame = customtkinter.CTkFrame(master=self.frame_clientes, width=320, height=360, corner_radius=15, border_width=12, border_color="black")
        frame.pack(pady=10)

    # Cargar una imagen para volver atras
        imagen = ctk.CTkImage(light_image=PIL.Image.open("./assets/volver.png"),
                                dark_image=PIL.Image.open("./assets/volver.png"),
                                size=(30, 30))
        boton_con_imagen = ctk.CTkButton(self.frame_clientes, image=imagen,text="Volver", command=lambda:(self.frame_menu.pack(),self.frame_clientes.pack_forget()))
        boton_con_imagen.place(relx=0.03, rely=0.03)

        # Mensaje
        msjPrincipal = customtkinter.CTkLabel(self.frame_clientes, text="Mis Clientes", font=('Century Gothic', 20))
        msjPrincipal.place(x=50, y=45)

        button_registrarCliente = customtkinter.CTkButton(self.frame_clientes, width=220, text="REGISTRAR NUEVO CLIENTE", command=lambda: (self.frame_clientes.pack_forget(),self.frame_registrarCliente.pack()), corner_radius=6)
        button_registrarCliente.place(x=50, y=110)

        button_actualizarCliente = customtkinter.CTkButton(self.frame_clientes, width=220, text="ACTUALIZAR CLIENTE", command=lambda: (self.frame_clientes.pack_forget(),self.frame_actualizarClientes.pack()), corner_radius=6)
        button_actualizarCliente.place(x=50, y=165)

        button_consultarCliente = customtkinter.CTkButton(self.frame_clientes, width=220, text="CONSULTAR CLIENTE", command=lambda: cambiarVentana(clientes, ventana_RegistrarCliente), corner_radius=6)
        button_consultarCliente.place(x=50, y=220)

#Llenar pagos
        frame = customtkinter.CTkFrame(master=self.frame_pagos, width=320, height=360, corner_radius=15, border_width=12, border_color="black")
        frame.pack(pady=10)

    # Cargar una imagen para volver atras
        imagen = ctk.CTkImage(light_image=PIL.Image.open("./assets/volver.png"),
                                dark_image=PIL.Image.open("./assets/volver.png"),
                                size=(30, 30))
        boton_con_imagen = ctk.CTkButton(self.frame_pagos, image=imagen,text="Volver", command=lambda:(self.frame_menu.pack(),self.frame_pagos.pack_forget()))
        boton_con_imagen.place(relx=0.03, rely=0.03)

        # Mensaje
        msjPrincipal = customtkinter.CTkLabel(self.frame_pagos, text="PAGOS", font=('Century Gothic', 20))
        msjPrincipal.place(x=50, y=45)

        button_registrarCliente = customtkinter.CTkButton(self.frame_pagos, width=220, text="PAGO DE CUOTA", command=lambda: (self.frame_pagos.pack_forget(),self.frame_pagoCuota.pack()), corner_radius=6)
        button_registrarCliente.place(x=50, y=110)

        button_actualizarCliente = customtkinter.CTkButton(self.frame_pagos, width=220, text="ACTUALIZAR PLANES", command=lambda: (self.frame_pagos.pack_forget(),self.frame_actualizarPrecio.pack()), corner_radius=6)
        button_actualizarCliente.place(x=50, y=165)

        button_consultarCliente = customtkinter.CTkButton(self.frame_pagos, width=220, text="ASISTENCIAS", command=lambda: cambiarVentana(clientes, ventana_RegistrarCliente), corner_radius=6)
        button_consultarCliente.place(x=50, y=220)

# llenar pagoCuota
        frame = customtkinter.CTkFrame(self.frame_pagoCuota, width=600, height=700, corner_radius=15)
        frame.pack(pady=10)

    # Cargar una imagen para volver atras
        imagen = ctk.CTkImage(light_image=PIL.Image.open("./assets/volver.png"),
                                dark_image=PIL.Image.open("./assets/volver.png"),
                                size=(30, 30))
        boton_con_imagen = ctk.CTkButton(self.frame_pagoCuota, image=imagen,text="Volver", command=lambda:(self.frame_pagos.pack(),self.frame_pagoCuota.pack_forget()))
        boton_con_imagen.place(relx=0.03, rely=0.03)

    #LABEL TITULO
        label_titulo = customtkinter.CTkLabel(master=frame, text="PAGO DE CUOTA", font=('Century Gothic',20))
        label_titulo.place(relx=0.36, rely=0.1)

        #Entradas
        label_cliente = customtkinter.CTkLabel(master=frame, text="Cliente", font=('Century Gothic',15))
        label_cliente.place(relx=0.45, rely=0.2)
        entry_cliente = customtkinter.CTkEntry(master=frame, width=220, height=25, corner_radius=10)
        entry_cliente.place(relx=0.5, rely=0.26, anchor=tk.CENTER)

        label_programa = customtkinter.CTkLabel(master=frame, text="Programa", font=('Century Gothic',15))
        label_programa.place(relx=0.44, rely=0.3)
        entry_programa = customtkinter.CTkEntry(master=frame, width=220, height=25, corner_radius=10)
        entry_programa.place(relx=0.5, rely=0.36, anchor=tk.CENTER)

        label_pago = customtkinter.CTkLabel(master=frame, text="Pago $", font=('Century Gothic',15))
        label_pago.place(relx=0.44, rely=0.4)
        entry_pago = customtkinter.CTkEntry(master=frame, width=120, height=25, corner_radius=10)
        entry_pago.place(relx=0.5, rely=0.46, anchor=tk.CENTER)

        label_profesor = customtkinter.CTkLabel(master=frame, text="Profesor", font=('Century Gothic',15))
        label_profesor.place(relx=0.44, rely=0.5)
        entry_profesor = customtkinter.CTkEntry(master=frame, width=220, height=25, corner_radius=10)
        entry_profesor.place(relx=0.5, rely=0.56, anchor=tk.CENTER)
        
        label_fecha= customtkinter.CTkLabel(master=frame, text="Fecha", font=('Century Gothic',15)) 
        label_fecha.place(relx=0.45, rely=0.6)
        frameCalendario = customtkinter.CTkFrame(master=frame, width=300, height=300)
        frameCalendario.place(relx=0.5, rely=0.75, anchor=tk.CENTER)
        
        # Crear un objeto Calendar
        cal = Calendar(frameCalendario, selectmode="day", year=2023, month=10, day=23)

        # Colocar los widgets en la ventana
        cal.pack(pady=10)
        
        button_confirmar = customtkinter.CTkButton(
            master=frame,
            width=220,
            text="Confirmar",
            command=lambda: (registrarPago([entry_cliente.get(), entry_pago.get(), entry_programa.get(), entry_profesor.get(), cal.get_date()])),                
            corner_radius=6
        )
        button_confirmar.place(relx=0.33, rely=0.9)

# Llenar al registrar clientes
        frame = customtkinter.CTkFrame(master=self.frame_registrarCliente, width=800, height=800, corner_radius=15, border_color="black",border_width=12)
        frame.pack(pady=10)
    # Cargar una imagen para volver atras
        imagen = ctk.CTkImage(light_image=PIL.Image.open("./assets/volver.png"),
                                dark_image=PIL.Image.open("./assets/volver.png"),
                                size=(30, 30))
        boton_con_imagen = ctk.CTkButton(self.frame_registrarCliente, image=imagen,text="Volver", command=lambda:(self.frame_clientes.pack(),self.frame_registrarCliente.pack_forget()))
        boton_con_imagen.place(relx=0.03, rely=0.03)
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

        label_fechaNacimiento = customtkinter.CTkLabel(master=self.frame_registrarCliente, text="Fecha de nacimiento", font=('Century Gothic',15)) # se ingresa ejemplo "año-mes-dia"
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
            command=lambda: (agregar_cliente([entry_nombre.get(),entry_apellido.get(), entry_correo.get(), entry_documento.get(), cal.get_date(), entry_telefono.get()]),self.frame_clientes.pack(),self.frame_registrarCliente.pack_forget()),
            corner_radius=6
        )
        button_confirmar.place(relx=0.18, rely=0.90)

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

                self.label_Documento = ctk.CTkLabel(frame, text="Documento:")
                self.label_Documento.grid(row=2, column=0)
                self.Documento_entry = ctk.CTkEntry(frame)
                self.Documento_entry.grid(row=2, column=1)

                self.label_Correo = ctk.CTkLabel(frame, text="Correo:")
                self.label_Correo.grid(row=2, column=2)
                self.Correo_entry = ctk.CTkEntry(frame)
                self.Correo_entry.grid(row=2, column=3)

                self.label_FechaNacimiento = ctk.CTkLabel(frame, text="Fecha de nacimiento:")
                self.label_FechaNacimiento.grid(row=3, column=0)
                self.FechaNacimiento_entry = ctk.CTkEntry(frame)
                self.FechaNacimiento_entry.grid(row=3, column=1)

                self.label_Telefono = ctk.CTkLabel(frame, text="Telefono:")
                self.label_Telefono.grid(row=3, column=2)
                self.Telefono_entry = ctk.CTkEntry(frame)
                self.Telefono_entry.grid(row=3, column=3)




                # Crear botones
                self.btn_agregar = ctk.CTkButton(frame, text="Agregar", command=self.agregar)
                self.btn_agregar.grid(row=4, column=0)

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
                    self.lista_programas.insert(ctk.END, (apellido, nombre, correo, documento, fechaNacimiento, telefono))


            def agregar(self):
                apellido = self.Apellido_entry.get()
                nombre = self.nombre_entry.get()
                correo = self.Correo_entry.get()
                documento = self.Documento_entry.get()
                fechaNacimiento = self.FechaNacimiento_entry.get()
                telefono = self.Telefono_entry.get()

                if apellido and nombre and correo and documento and fechaNacimiento and telefono:
                    self.cursor.execute("INSERT INTO Clientes (Apellido, Nombre, Correo, Documento, Fecha_Nacimiento, Telefono) VALUES (?, ?, ?, ?, ?, ?)",
                                        (apellido, nombre, correo, documento, fechaNacimiento, telefono))
                    self.conexion.commit()
                    self.mostrar_programas()
                    self.limpiar_campos()


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

        frame=customtkinter.CTkFrame(self.frame_actualizarClientes, width=800, height=600, corner_radius=15)
        frame.pack(pady=10)

        # Cargar una imagen para volver atras
        imagen = ctk.CTkImage(light_image=PIL.Image.open("./assets/volver.png"),
                                dark_image=PIL.Image.open("./assets/volver.png"),
                                size=(30, 30))
        
        boton_con_imagen = ctk.CTkButton(master=self.frame_actualizarClientes, image=imagen,text="Volver", command=lambda:(self.frame_clientes.pack(),self.frame_actualizarClientes.pack_forget()))
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

        frame=customtkinter.CTkFrame(self.frame_actualizarPrecio, width=800, height=600, corner_radius=15)
        frame.pack(pady=10)

        # Cargar una imagen para volver atras
        imagen = ctk.CTkImage(light_image=PIL.Image.open("./assets/volver.png"),
                                dark_image=PIL.Image.open("./assets/volver.png"),
                                size=(30, 30))
        
        boton_con_imagen = ctk.CTkButton(master=self.frame_actualizarPrecio, image=imagen,text="Volver", command=lambda:(self.frame_pagos.pack(),self.frame_actualizarPrecio.pack_forget()))
        boton_con_imagen.pack(pady=10)

        ProgramaABM(frame)



        # Mostrar el primer menú al inicio
        self.frame_menu.pack()

if __name__ == "__main__":
    app = VentanaPrincipal()
    app.mainloop()