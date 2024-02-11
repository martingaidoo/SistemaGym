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
import customtkinter as ctk


banderaVencimiento = False

fecha_actual = datetime.now()
actualFechaHora = fecha_actual.strftime("%d/%m/%Y %H:%M:%S")
fecha_con_mes_adicional = fecha_actual + relativedelta(months=1)
# Formatear la fecha como días/mes/año
actual = fecha_actual.strftime("%d/%m/%Y")


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