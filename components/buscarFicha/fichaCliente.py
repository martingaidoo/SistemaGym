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
import requests
from datetime import datetime, timedelta
import os
import sys



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