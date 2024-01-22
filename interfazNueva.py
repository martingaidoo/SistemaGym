import tkinter
import tkinter.messagebox
import customtkinter
from logicaBotones import *
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


customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
def conectar_bd():
        # Configura la conexión a la base de datos SQLite
        conexion = sqlite3.connect('C:/Users/Usuario/Desktop/Laburo/SistemaGym-main/BaseDatos.db')
        return conexion

def obtener_notificaciones():
        # Conecta a la base de datos
        conexion = conectar_bd()

        # Crea un cursor para ejecutar consultas SQL
        cursor = conexion.cursor()

        # Obtiene la fecha actual
        fecha_actual = datetime.now().strftime('%Y-%m-%d')

        # Consulta para obtener los nombres de las personas cuyo vencimiento ha pasado
        consulta = """
            SELECT Clientes.Nombre
            FROM Cuotas
            JOIN Clientes ON Cuotas.id = Cuotas.id
            WHERE Cuotas.vencimiento < ?
        """

        # Ejecuta la consulta
        cursor.execute(consulta, (fecha_actual,))

        # Obtiene los resultados
        resultados = cursor.fetchall()

        # Cierra el cursor y la conexión
        cursor.close()
        conexion.close()

        return resultados
class App(customtkinter.CTk):
    def __init__(self):
            super().__init__()

            # configure window
            self.title("Gym Master")
            self.geometry(f"{1100}x{580}")

            # configure grid layout (4x4)
            self.grid_columnconfigure(1, weight=1)
            self.grid_columnconfigure((2, 3), weight=0)
            self.grid_rowconfigure((0, 1, 2), weight=1)

            # create sidebar frame with widgets
            self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
            self.sidebar_frame.grid(row=0, column=0, rowspan=8, sticky="nsew")
            self.sidebar_frame.grid_rowconfigure(8, weight=1)
            self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Salud Integral", font=customtkinter.CTkFont(size=20, weight="bold"))
            self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
            self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=lambda:(controlAcceso(self)), text="Control de acceso")
            self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
            self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, command=lambda:(registrarCliente(self)), text = "Registrar Nuevo Cliente")
            self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
            self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, command=lambda:(actualizarClientes(self)), text = "Actualizar Cliente")
            self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
            self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame, command=lambda:(consultarCuotas(self)), text = "Consultar Cuotas")
            self.sidebar_button_4.grid(row=4, column=0, padx=20, pady=10)
            self.sidebar_button_5 = customtkinter.CTkButton(self.sidebar_frame, command=lambda:(pagoCuotas(self)), text = "Pago de Cuota")
            self.sidebar_button_5.grid(row=5, column=0, padx=20, pady=10)
            self.sidebar_button_6 = customtkinter.CTkButton(self.sidebar_frame, command=lambda:(actualizarPrecio(self)), text = "Actualizar Planes")
            self.sidebar_button_6.grid(row=6, column=0, padx=20, pady=10)
            self.sidebar_button_7 = customtkinter.CTkButton(self.sidebar_frame, command=lambda:(generar_completo()), text = "Generar Exel Clientes")
            self.sidebar_button_7.grid(row=7, column=0, padx=20, pady=10)
            #simplemente se hace invisible este boton para que genere un espacio
            self.sidebar_button_8 = customtkinter.CTkButton(self.sidebar_frame, command=lambda:(self.sidebar_button_event), text="Hace click")
            self.sidebar_button_8.grid(row=8, column=0, padx=20, pady=(5,5))
            self.sidebar_button_8.grid_forget()
            #
            self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Color fondo", anchor="w")
            self.appearance_mode_label.grid(row=9, column=0, padx=20, pady=(10, 0))
            self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                        command=self.change_appearance_mode_event)
            self.appearance_mode_optionemenu.grid(row=10, column=0, padx=20, pady=(10, 10))
            self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="Escala UI:", anchor="w")
            self.scaling_label.grid(row=11, column=0, padx=20, pady=(10, 0))
            self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                                command=self.change_scaling_event)
            self.scaling_optionemenu.grid(row=12, column=0, padx=20, pady=(10, 20))

            # create main entry and button
            self.buscarFichas_frame = customtkinter.CTkFrame(self, width=140, corner_radius=6)
            self.buscarFichas_frame.grid(row=3, column=1, columnspan=3, padx=(20, 0), pady=(10, 10), sticky="nsew")
            mostrarResultados(self.buscarFichas_frame)
            # create tabview
            self.tabview = customtkinter.CTkTabview(self, width=250)
            self.tabview.grid(row=1, column=3, padx=(20, 0), pady=(20, 0), sticky="nsew")
            self.tabview.add("opciones")
            self.tabview.add("WhatsApp")
            self.tabview.add("Configuracion")
            self.tabview.tab("opciones").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
            self.tabview.tab("WhatsApp").grid_columnconfigure(0, weight=1)

            self.optionmenu_1 = customtkinter.CTkOptionMenu(self.tabview.tab("opciones"), dynamic_resizing=False,
                                                            values=["Opcion 1", "Opcion 2", "Opcion 3"])
            self.optionmenu_1.grid(row=0, column=0, padx=20, pady=(20, 10))
            self.combobox_1 = customtkinter.CTkComboBox(self.tabview.tab("opciones"),
                                                        values=["Opcion 1", "Opcion 2", "Opcio n3"])
            self.combobox_1.grid(row=1, column=0, padx=20, pady=(10, 10))
            self.string_input_button = customtkinter.CTkButton(self.tabview.tab("opciones"), text="Cuadro de dialogo",
                                                                command=self.open_input_dialog_event)
            self.string_input_button.grid(row=2, column=0, padx=20, pady=(10, 10))
            self.label_tab_2 = customtkinter.CTkLabel(self.tabview.tab("WhatsApp"), text="Label Pestaña 2")
            self.label_tab_2.grid(row=0, column=0, padx=20, pady=20)

  


            # create scrollable frame
            self.scrollable_frame = customtkinter.CTkScrollableFrame(self, label_text="Notificaciones")
            self.scrollable_frame.grid(row=0, column=3, padx=(20, 0), pady=(20, 0), sticky="nsew")
            self.scrollable_frame.grid_columnconfigure(0, weight=1)

        # Obtén las notificaciones y agrega etiquetas para cada notificación
            lista_notificaciones = obtener_notificaciones()
            for notificacion_text in lista_notificaciones:
                nombre = next(iter(notificacion_text), None)

    # Si se encontró un nombre, agrega etiqueta para la notificación
                if nombre:
                    etiqueta_notificacion = customtkinter.CTkLabel(self.scrollable_frame, text=f"{nombre} - Vencido")
                    etiqueta_notificacion.pack(fill="x", padx=10, pady=5)
                    

                # set default values
                self.sidebar_button_8.configure(state="disabled", text="Este boton no lo podes clickear")
                #self.scrollable_frame_switches[0].select()
                #self.scrollable_frame_switches[4].select()
                self.appearance_mode_optionemenu.set("Dark")
                self.scaling_optionemenu.set("100%")
                self.optionmenu_1.set("Menu")
                self.combobox_1.set("Opciones")

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Escribi algo:", title="Cuadro de dialogo")
        print("El usuario escribio:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

if __name__ == "__main__":
    app = App()
    app.mainloop()