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
from tkinter import ttk

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
