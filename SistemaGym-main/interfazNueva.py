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
from tkinter import PhotoImage
from PIL import Image, ImageTk
import os
import sys


customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


def conectar_bd():
        # Configura la conexión a la base de datos SQLite
        conexion = sqlite3.connect('BaseDatos.db')
        return conexion

def obtener_notificaciones():
    # Conecta a la base de datos
    conexion = conectar_bd()

    # Crea un cursor para ejecutar consultas SQL
    cursor = conexion.cursor()

    # Obtiene la fecha actual como un objeto datetime
    fecha_actual = datetime.now().date()

    # Consulta para obtener los nombres de las personas cuyo vencimiento ha pasado
    consulta = """
        SELECT Clientes.Nombre, Cuotas.vencimiento
        FROM Cuotas
        JOIN Clientes ON Cuotas.id_cliente = Clientes.id
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
            
            self.interface_mode = "Dark"  # Puedes cambiar esto dinámicamente según tu lógica

            # Cargar los iconos según el modo de apariencia
            self.load_icons()
            
            icon_path = "./assets/controlaccesodark.png"
            icon_path2 = "./assets/registrarnuevoclientedark.png"
            icon_path3 = "./assets/actualizarclientesdark.png"
            icon_path4 = "./assets/consultarcuotasdark.png"
            icon_path5 = "./assets/pagocuotadark.png"
            icon_path6 = "./assets/actualizarplanesdark.png"
            icon_path7 = "./assets/cajadark.png"
            icon_path8 = "./assets/exel.png"
            icon_path9 = "./assets/asistenciasDark.png"
            icon_pathbuscarficha = "./assets/buscardark.png"

            new_size = (40, 40)
            img = Image.open(icon_path)
            img_2 = Image.open(icon_path2)
            img_2 = img_2.resize(new_size)
            img_3 = Image.open(icon_path3)
            img_3 = img_3.resize(new_size)
            img_4 = Image.open(icon_path4)
            img_4 = img_4.resize(new_size)
            img_5 = Image.open(icon_path5)
            img_5 = img_5.resize(new_size)
            img_6 = Image.open(icon_path6)
            img_6 = img_6.resize(new_size)
            img_7 = Image.open(icon_path7)
            img_7 = img_7.resize(new_size)
            img_8 = Image.open(icon_path8)
            img_8 = img_8.resize(new_size)
            img_9 = Image.open(icon_path9)
            img_9 = img_9.resize(new_size)
            imgbuscarficha = Image.open(icon_pathbuscarficha)
            imgbuscarficha = imgbuscarficha.resize(new_size)
            

        # Ajusta el tamaño deseado (por ejemplo, 50x50 píxeles)
            img = img.resize(new_size)

    # Guarda la imagen ajustada como un archivo temporal en formato GIF
            temp_gif_path = "temp_icon.gif"
            img.save(temp_gif_path, "GIF")

# Crea un objeto PhotoImage con la imagen ajustada
            icon_image = PhotoImage(file=temp_gif_path)
            self.icon_image = ImageTk.PhotoImage(img)
            icon_image_2 = ImageTk.PhotoImage(img_2)
            icon_image_3 = ImageTk.PhotoImage(img_3)
            icon_image_4 = ImageTk.PhotoImage(img_4)
            icon_image_5 = ImageTk.PhotoImage(img_5)
            icon_image_6 = ImageTk.PhotoImage(img_6)
            icon_image_7 = ImageTk.PhotoImage(img_7)
            icon_image_8 = ImageTk.PhotoImage(img_8)
            icon_image_9 = ImageTk.PhotoImage(img_9)
            icon_imagenbuscarficha = ImageTk.PhotoImage(imgbuscarficha)

            
            # configure window
            self.title("Salud Integral Gym")
            self.geometry(f"{1100}x{580}")
            self.iconbitmap("./assets/logo.ico")

            # configure grid layout (4x4)
            self.grid_columnconfigure(1, weight=1)
            self.grid_columnconfigure((2, 3), weight=0)
            self.grid_rowconfigure((0, 1, 2), weight=1)

            # create sidebar frame with widgets
            self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
            self.sidebar_frame.grid(row=0, column=0, rowspan=8, sticky="nsew")
            self.sidebar_frame.grid_rowconfigure(9, weight=1)
            self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Salud Integral", font=customtkinter.CTkFont(size=20, weight="bold"))
            self.logo_label.grid(row=0, column=0, padx=20, pady=(10, 10))
            self.sidebar_button_1 = customtkinter.CTkLabel(self.sidebar_frame, image=self.icon_image, text="Control de acceso", compound="top")
            self.sidebar_button_1.bind("<Button-1>", lambda event: controlAcceso(self))
            self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)

            self.sidebar_button_2 = customtkinter.CTkLabel(self.sidebar_frame, image=icon_image_2, text="Registrar nuevo cliente", compound="top")
            self.sidebar_button_2.bind("<Button-1>", lambda event: (registrarCliente(self)))
            self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
            self.sidebar_button_3 = customtkinter.CTkLabel(self.sidebar_frame, image=icon_image_3, text="Actualizar Clientes", compound="top")
            self.sidebar_button_3.bind("<Button-1>", lambda event: (actualizarClientes(self)))
            self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)

            self.sidebar_button_5 = customtkinter.CTkLabel(self.sidebar_frame, image=icon_image_5, text="Pago de cuota", compound="top")
            self.sidebar_button_5.bind("<Button-1>", lambda event: (pagoCuotas(self)))
            self.sidebar_button_5.grid(row=4, column=0, padx=20, pady=10)

            self.sidebar_button_6 = customtkinter.CTkLabel(self.sidebar_frame, image=icon_image_6, text="Actualizar planes", compound="top")
            self.sidebar_button_6.bind("<Button-1>", lambda event: (actualizarPrecio(self)))
            self.sidebar_button_6.grid(row=5, column=0, padx=20, pady=10)

            self.sidebar_button_7 = customtkinter.CTkLabel(self.sidebar_frame, image=icon_image_7, text="Caja", compound="top")
            self.sidebar_button_7.bind("<Button-1>", lambda event: (caja(self)))
            self.sidebar_button_7.grid(row=6, column=0, padx=20, pady=10)

            self.sidebar_button_8 = customtkinter.CTkLabel(self.sidebar_frame, image=icon_image_8, text="Generar Excel", compound="top")
            self.sidebar_button_8.bind("<Button-1>", lambda event: (generar_completo()))
            self.sidebar_button_8.grid(row=7, column=0, padx=20, pady=10)
  

            self.sidebar_button_9 = customtkinter.CTkLabel(self.sidebar_frame, image=icon_image_9, text="Asistencias", compound="top")
            self.sidebar_button_9.bind("<Button-1>", lambda event: (asistencias(self)))
            self.sidebar_button_9.grid(row=8, column=0, padx=20, pady=10)
            
            #
            self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Color fondo", anchor="w")
            self.appearance_mode_label.grid(row=9, column=0, padx=20, pady=(10, 0))
            self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                        command=self.change_appearance_mode_event)
            self.appearance_mode_optionemenu.grid(row=10, column=0, padx=20, pady=(10, 0))
            self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="Escala UI:", anchor="w")
            self.scaling_label.grid(row=11, column=0, padx=20, pady=(10, 0))
            self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                                command=self.change_scaling_event)
            self.scaling_optionemenu.grid(row=12, column=0, padx=20, pady=(10, 0))

            # create main entry and button
            self.buscarFichas_frame = customtkinter.CTkFrame(self, width=140, corner_radius=6)
            self.buscarFichas_frame.grid(row=3, column=1, columnspan=3, padx=(20, 0), pady=(10, 0), sticky="nsew")
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
                #self.sidebar_button_9.configure(state="disabled", text="Este boton no lo podes clickear")
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
         # Cambia el modo de la interfaz y recarga los iconos
        self.interface_mode = new_appearance_mode.lower()
        self.load_icons()

        # Actualiza los botones conlos nuevos iconos
        self.sidebar_button_1.configure(image=self.get_current_icon_button_1())
        self.sidebar_button_2.configure(image=self.get_current_icon_button_2())
        self.sidebar_button_3.configure(image=self.get_current_icon_button_3())
        self.sidebar_button_5.configure(image=self.get_current_icon_button_5())
        self.sidebar_button_6.configure(image=self.get_current_icon_button_6())
        self.sidebar_button_7.configure(image=self.get_current_icon_button_7())
        self.sidebar_button_9.configure(image=self.get_current_icon_button_9())
        self.buscarFichas_frame.configure(image=self.get_current_icon_button_buscarficha())
        
        
    def get_current_icon_button_1(self):
        # Devuelve el icono correspondiente al modo actual para el botón 1
        return self.icon_image_light if self.interface_mode == "light" else self.icon_image_dark
    def get_current_icon_button_2(self):
        # Devuelve el icono correspondiente al modo actual para el botón 1
        return self.icon_image_light2 if self.interface_mode == "light" else self.icon_image_dark2
    def get_current_icon_button_3(self):
        # Devuelve el icono correspondiente al modo actual para el botón 1
        return self.icon_image_light3 if self.interface_mode == "light" else self.icon_image_dark3
    def get_current_icon_button_4(self):
        # Devuelve el icono correspondiente al modo actual para el botón 1
        return self.icon_image_light4 if self.interface_mode == "light" else self.icon_image_dark4
    def get_current_icon_button_5(self):
        # Devuelve el icono correspondiente al modo actual para el botón 1
        return self.icon_image_light5 if self.interface_mode == "light" else self.icon_image_dark5
    def get_current_icon_button_6(self):
        # Devuelve el icono correspondiente al modo actual para el botón 1
        return self.icon_image_light6 if self.interface_mode == "light" else self.icon_image_dark6
    def get_current_icon_button_7(self):
        # Devuelve el icono correspondiente al modo actual para el botón 1
        return self.icon_image_light7 if self.interface_mode == "light" else self.icon_image_dark7
    def get_current_icon_button_8(self):
        # Devuelve el icono correspondiente al modo actual para el botón 1
        return self.icon_image_light8 if self.interface_mode == "light" else self.icon_image_dark8
    def get_current_icon_button_9(self):
        # Devuelve el icono correspondiente al modo actual para el botón 1
        return self.icon_image_light9 if self.interface_mode == "light" else self.icon_image_dark9
    def get_current_icon_button_buscarficha(self):
        # Devuelve el icono correspondiente al modo actual para el botón 1
        return self.icon_image_lightbuscar if self.interface_mode == "light" else self.icon_image_darkbuscar


    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)
    def load_icons(self):
        # Rutas de los archivos de iconos para light y dark mode
        
        icon_path_dark = "./assets/controlaccesodark.png"
        icon_path2_dark = "./assets/registrarnuevoclientedark.png"
        icon_path3_dark = "./assets/actualizarclientesdark.png"
        icon_path4_dark = "./assets/consultarcuotasdark.png"
        icon_path5_dark = "./assets/pagocuotadark.png"
        icon_path6_dark = "./assets/actualizarplanesdark.png"
        icon_path7_dark = "./assets/cajadark.png"
        icon_path8_dark = "./assets/exel.png"
        icon_path9_dark = "./assets/asistenciasDark.png"
        icon_path_darkbuscar = "./assets/buscardark.png"

        icon_path_light = "./assets/controlaccesolight.png"
        icon_path2_light = "./assets/registrarnuevoclientelight.png"
        icon_path3_light = "./assets/actualizarclienteslight.png"
        #icon_path4_light = "./assets/consultarcuotaslight.png"
        icon_path5_light = "./assets/pagocuotalight.png"
        icon_path6_light = "./assets/actualizarplaneslight.png"
        icon_path7_light = "./assets/cajalight.png"
        icon_path8_light = "./assets/exel.png"
        icon_path9_light = "./assets/asistenciasLight.png"
        icon_path_lightbuscar = "./assets/buscarlight.png"

        # Abre las imágenes con Pillow y ajusta el tamaño si es necesario
        img_light = Image.open(icon_path_light).resize((40, 40))
        img_light2 =Image.open(icon_path2_light).resize((40, 40))
        img_light3 = Image.open(icon_path3_light).resize((40, 40))
        #img_light4 =Image.open(icon_path4_light).resize((40, 40))
        img_light5 = Image.open(icon_path5_light).resize((40, 40))
        img_light6 =Image.open(icon_path6_light).resize((40, 40))
        img_light7 = Image.open(icon_path7_light).resize((40, 40))
        img_light8 = Image.open(icon_path8_light).resize((40, 40))
        img_light9 = Image.open(icon_path9_light).resize((40, 40))
        img_buscarlight = Image.open(icon_path_lightbuscar).resize((40, 40))
        
        img_dark = Image.open(icon_path_dark).resize((40, 40))
        img_dark2 = Image.open(icon_path2_dark).resize((40, 40))
        img_dark3 =Image.open(icon_path3_dark).resize((40, 40))
        #img_dark4 = Image.open(icon_path4_dark).resize((40, 40))
        img_dark5 =Image.open(icon_path5_dark).resize((40, 40))
        img_dark6 = Image.open(icon_path6_dark).resize((40, 40))
        img_dark7 = Image.open(icon_path7_dark).resize((40, 40))
        img_dark8 =Image.open(icon_path8_dark).resize((40, 40))
        img_dark9 = Image.open(icon_path9_dark).resize((40, 40))
        img_buscardark = Image.open(icon_path_darkbuscar).resize((40, 40))
        
        

        # Guarda las imágenes ajustadas como objetos ImageTk
        self.icon_image_light = ImageTk.PhotoImage(img_light)
        self.icon_image_light2 = ImageTk.PhotoImage(img_light2)
        self.icon_image_light3 = ImageTk.PhotoImage(img_light3)
        #self.icon_image_light4 = ImageTk.PhotoImage(img_light4)
        self.icon_image_light5 = ImageTk.PhotoImage(img_light5)
        self.icon_image_light6 = ImageTk.PhotoImage(img_light6)
        self.icon_image_light7 = ImageTk.PhotoImage(img_light7)
        self.icon_image_light8 = ImageTk.PhotoImage(img_light8)
        self.icon_image_light9 = ImageTk.PhotoImage(img_light9)
        self.icon_image_lightbuscar = ImageTk.PhotoImage(img_buscarlight)
        
        self.icon_image_dark = ImageTk.PhotoImage(img_dark)
        self.icon_image_dark2 = ImageTk.PhotoImage(img_dark2)
        self.icon_image_dark3 = ImageTk.PhotoImage(img_dark3)
        #self.icon_image_dark4 = ImageTk.PhotoImage(img_dark4)
        self.icon_image_dark5 = ImageTk.PhotoImage(img_dark5)
        self.icon_image_dark6 = ImageTk.PhotoImage(img_dark6)
        self.icon_image_dark7 = ImageTk.PhotoImage(img_dark7)
        self.icon_image_dark8 = ImageTk.PhotoImage(img_dark8)
        self.icon_image_dark9 = ImageTk.PhotoImage(img_dark9)
        self.icon_image_darkbuscar = ImageTk.PhotoImage(img_buscardark)
        

if __name__ == "__main__":
    app = App()
    app.mainloop()