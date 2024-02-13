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
            self.tree = ttk.Treeview(frame, columns=("Nombre", "Cobro", "Fecha", "Profesor", "Metodo"), show="headings")
            self.tree.heading("Nombre", text="Nombre")
            self.tree.heading("Cobro", text="Cobro")
            self.tree.heading("Fecha", text="Fecha")
            self.tree.heading("Profesor", text="Profesor")
            self.tree.heading("Metodo", text="Metodo de pago")
            self.tree.grid(column=0, columnspan=2, row=3, sticky="nsew")

            self.label_totalE = customtkinter.CTkLabel(frame, text="Total efectivo:")
            self.label_totalE.grid(column=0, row=4, padx=(70,70), pady=(20, 20))

            self.label_totalT = customtkinter.CTkLabel(frame, text="Total transferencia:")
            self.label_totalT.grid(column=1, row=4, padx=(70,70), pady=(20, 20))

            # Obtener datos de la base de datos
            self.obtener_datos()

        def obtener_datos(self):
            # Obtener fechas seleccionadas
            print("entreee")
            totalEfectivo=0
            totalTransferencia=0
            fecha_inicio = self.cal_inicio.get_date()
            fecha_fin = self.cal_fin.get_date()

            # Ejecutar consulta para obtener datos de la tabla Cobro en el rango de fechas
            self.cursor.execute("SELECT id_cliente, cobro, fecha, profesor, metodoPago  FROM Cobro ORDER BY fecha DESC")

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
                    if row[4] == "Efectivo":
                        totalEfectivo += int(row[1])
                    else:
                        totalTransferencia += int(row[1])
                    id_cliente = row[0]
                    self.cursor.execute("SELECT Nombre, Apellido FROM Clientes WHERE id=?", (id_cliente,))
                    nombre_cliente, apellido_cliente = self.cursor.fetchone()
                    nombre_completo = nombre_cliente + " " + apellido_cliente
                    # Añadir datos a la tabla
                    self.tree.insert("", 0, values=(nombre_completo, row[1], row[2], row[3], row[4]))
            self.label_totalT.configure(text="Total transferencia:" + str(totalTransferencia))
            self.label_totalE.configure(text="Total efectivo:" + str(totalEfectivo))

        def actualizar_tabla(self):
            print("entro 2")
            # Obtener y actualizar datos según el rango de fechas seleccionado
            #self.label_totalT.configure(text="Total transferencia: 0")
            #self.label_totalE.configure(text="Total efectivo: 0")
            self.obtener_datos()
    TablaDatos(self.frame_caja)