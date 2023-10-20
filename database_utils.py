import tkinter
from tkinter import PhotoImage
import customtkinter
from customtkinter import CTk, CTkFrame, CTkButton
from PIL import ImageTk,Image
import tkinter as tk
import pygame
import sqlite3
class ProgramaABM_Clientes:
    def __init__(self, frame):
        self.frame = frame
        

        # Conectarse a la base de datos SQLite
        self.conexion = sqlite3.connect("BaseDatos.db")
        self.cursor = self.conexion.cursor()
        self.conexion.commit()

        # Crear etiquetas y campos de entrada
        self.label_nombre = tk.Label(frame, text="Nombre:")
        self.label_nombre.grid(row=1, column=0)
        self.nombre_entry = tk.Entry(frame)
        self.nombre_entry.grid(row=1, column=1)

        self.label_Apellido = tk.Label(frame, text="Apellido:")
        self.label_Apellido.grid(row=1, column=2)
        self.Apellido_entry = tk.Entry(frame)
        self.Apellido_entry.grid(row=1, column=3)

        self.label_Documento = tk.Label(frame, text="Documento:")
        self.label_Documento.grid(row=2, column=0)
        self.Documento_entry = tk.Entry(frame)
        self.Documento_entry.grid(row=2, column=1)

        self.label_Correo = tk.Label(frame, text="Correo:")
        self.label_Correo.grid(row=2, column=2)
        self.Correo_entry = tk.Entry(frame)
        self.Correo_entry.grid(row=2, column=3)

        self.label_FechaNacimiento = tk.Label(frame, text="Fecha de nacimiento:")
        self.label_FechaNacimiento.grid(row=3, column=0)
        self.FechaNacimiento_entry = tk.Entry(frame)
        self.FechaNacimiento_entry.grid(row=3, column=1)

        self.label_Telefono = tk.Label(frame, text="Telefono:")
        self.label_Telefono.grid(row=3, column=2)
        self.Telefono_entry = tk.Entry(frame)
        self.Telefono_entry.grid(row=3, column=3)




        # Crear botones
        self.btn_agregar = tk.Button(frame, text="Agregar", command=self.agregar)
        self.btn_agregar.grid(row=4, column=0)

        self.btn_actualizar = tk.Button(frame, text="Actualizar", command=self.actualizar)
        self.btn_actualizar.grid(row=4, column=2)



        # Crear una lista para mostrar los datos de la base de datos
        self.lista_programas = tk.Listbox(frame)
        self.lista_programas.grid(row=5, column=0, columnspan=4, sticky=tk.W + tk.E + tk.N + tk.S)
        self.mostrar_programas()

        # Asignar una función para manejar la selección en la lista
        self.lista_programas.bind('<<ListboxSelect>>', self.seleccionar_programa)

    def mostrar_programas(self):
        self.lista_programas.delete(0, tk.END)
        programas = self.cursor.execute('SELECT * FROM Clientes').fetchall()
        for programa in programas:
            _, nombre, apellido, correo, documento, fechaNacimiento, telefono = programa  # Obtener los dos últimos elementos de la tupla
            self.lista_programas.insert(tk.END, (apellido, nombre, correo, documento, fechaNacimiento, telefono))


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
        self.Telefono_entry.delete(0, tk.END)
        self.Telefono_entry.insert(0, telefono)
        self.Documento_entry.delete(0, tk.END)
        self.Documento_entry.insert(0, documento)
        self.Correo_entry.delete(0, tk.END)
        self.Correo_entry.insert(0, correo)
        self.FechaNacimiento_entry.delete(0, tk.END)
        self.FechaNacimiento_entry.insert(0, fechaNacimiento)

        self.nombre_entry.delete(0, tk.END)
        self.nombre_entry.insert(0, nombre)

        self.Apellido_entry.delete(0, tk.END)
        self.Apellido_entry.insert(0, apellido)

    def limpiar_campos(self):
        self.Apellido_entry.delete(0, tk.END)
        self.nombre_entry.delete(0, tk.END)
        self.FechaNacimiento_entry.delete(0, tk.END)
        self.Correo_entry.delete(0, tk.END)
        self.Documento_entry.delete(0, tk.END)
        self.Telefono_entry.delete(0, tk.END)

    def __del__(self):
        self.conexion.close()

def ventana_AcutalizarClientes():
    actualizarClientes = tk.Tk()
    actualizarClientes.geometry("600x440")
    actualizarClientes.config(bg="#7f5af0")
    actualizarClientes.title("Actualizar precios")
    imagen = tk.PhotoImage(file="./assets/volver.png")


    frame1=customtkinter.CTkFrame(master=actualizarClientes, width=500, height=360, corner_radius=15)
    frame1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    #FrameClientes
    frame = tk.Frame(actualizarClientes, width=500, height=360)
    frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    ProgramaABM_Clientes(frame)
    actualizarClientes.mainloop()


ventana_AcutalizarClientes()









class ProgramaABM_Clientes:
    def __init__(self, frame):
        self.frame = frame
        

        # Conectarse a la base de datos SQLite
        self.conexion = sqlite3.connect("BaseDatos.db")
        self.cursor = self.conexion.cursor()
        self.conexion.commit()

        # Crear etiquetas y campos de entrada
        self.label_nombre = tk.Label(frame, text="Nombre:")
        self.label_nombre.grid(row=1, column=0)
        self.nombre_entry = tk.Entry(frame)
        self.nombre_entry.grid(row=1, column=1)

        self.label_Apellido = tk.Label(frame, text="Apellido:")
        self.label_Apellido.grid(row=1, column=2)
        self.Apellido_entry = tk.Entry(frame)
        self.Apellido_entry.grid(row=1, column=3)

        self.label_Documento = tk.Label(frame, text="Documento:")
        self.label_Documento.grid(row=2, column=0)
        self.Documento_entry = tk.Entry(frame)
        self.Documento_entry.grid(row=2, column=1)

        self.label_Correo = tk.Label(frame, text="Correo:")
        self.label_Correo.grid(row=2, column=2)
        self.Correo_entry = tk.Entry(frame)
        self.Correo_entry.grid(row=2, column=3)

        self.label_FechaNacimiento = tk.Label(frame, text="Fecha de nacimiento:")
        self.label_FechaNacimiento.grid(row=3, column=0)
        self.FechaNacimiento_entry = tk.Entry(frame)
        self.FechaNacimiento_entry.grid(row=3, column=1)

        self.label_Telefono = tk.Label(frame, text="Telefono:")
        self.label_Telefono.grid(row=3, column=2)
        self.Telefono_entry = tk.Entry(frame)
        self.Telefono_entry.grid(row=3, column=3)




        # Crear botones
        self.btn_agregar = tk.Button(frame, text="Agregar", command=self.agregar)
        self.btn_agregar.grid(row=4, column=0)

        self.btn_actualizar = tk.Button(frame, text="Actualizar", command=self.actualizar)
        self.btn_actualizar.grid(row=4, column=2)



        # Crear una lista para mostrar los datos de la base de datos
        self.lista_programas = tk.Listbox(frame)
        self.lista_programas.grid(row=5, column=0, columnspan=4, sticky=tk.W + tk.E + tk.N + tk.S)
        self.mostrar_programas()

        # Asignar una función para manejar la selección en la lista
        self.lista_programas.bind('<<ListboxSelect>>', self.seleccionar_programa)

    def mostrar_programas(self):
        self.lista_programas.delete(0, tk.END)
        programas = self.cursor.execute('SELECT * FROM Clientes').fetchall()
        for programa in programas:
            _, nombre, apellido, correo, documento, fechaNacimiento, telefono = programa  # Obtener los dos últimos elementos de la tupla
            self.lista_programas.insert(tk.END, (apellido, nombre, correo, documento, fechaNacimiento, telefono))


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
        self.Telefono_entry.delete(0, tk.END)
        self.Telefono_entry.insert(0, telefono)
        self.Documento_entry.delete(0, tk.END)
        self.Documento_entry.insert(0, documento)
        self.Correo_entry.delete(0, tk.END)
        self.Correo_entry.insert(0, correo)
        self.FechaNacimiento_entry.delete(0, tk.END)
        self.FechaNacimiento_entry.insert(0, fechaNacimiento)

        self.nombre_entry.delete(0, tk.END)
        self.nombre_entry.insert(0, nombre)

        self.Apellido_entry.delete(0, tk.END)
        self.Apellido_entry.insert(0, apellido)

    def limpiar_campos(self):
        self.Apellido_entry.delete(0, tk.END)
        self.nombre_entry.delete(0, tk.END)
        self.FechaNacimiento_entry.delete(0, tk.END)
        self.Correo_entry.delete(0, tk.END)
        self.Documento_entry.delete(0, tk.END)
        self.Telefono_entry.delete(0, tk.END)

    def __del__(self):
        self.conexion.close()

def ventana_AcutalizarClientes():
    actualizarClientes = tk.Tk()
    actualizarClientes.geometry("600x440")
    actualizarClientes.config(bg="#7f5af0")
    actualizarClientes.title("Actualizar precios")

    imagen = tk.PhotoImage(file="./assets/volver.png")

    # Crear un botón con la imagen
    boton_con_imagen = tk.Button(actualizarClientes, image=imagen, command=lambda: (cambiarVentana(actualizarClientes, ventana_Programa)))
    boton_con_imagen.place(relx=0.03, rely=0.03)

    frame1=customtkinter.CTkFrame(master=actualizarClientes, width=500, height=360, corner_radius=15)
    frame1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    #FrameClientes
    frame = tk.Frame(actualizarClientes, width=500, height=360)
    frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    ProgramaABM_Clientes(frame)
    actualizarClientes.mainloop()

