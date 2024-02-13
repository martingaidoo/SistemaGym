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
from tkinter import messagebox


fecha_actual = datetime.now()
actualFechaHora = fecha_actual.strftime("%d/%m/%Y %H:%M:%S")
fecha_con_mes_adicional = fecha_actual + relativedelta(months=1)
# Formatear la fecha como días/mes/año
actual = fecha_actual.strftime("%d/%m/%Y")

actaulMasMes = fecha_con_mes_adicional.strftime("%d/%m/%Y")
#sirve para destrouit la ventada de la asistencia del cliente
banderaDestroy = True


def reproducir_sonido(value):
    pygame.init()
    pygame.mixer.init()
    if value == "pago":
        sonido = pygame.mixer.Sound("./sonidobien.wav")
        sonido.play()
    else:
        sonido = pygame.mixer.Sound("./sonidomal.mp3")
        sonido.play()
        



""" en esta funcion registrara la asistencia de un usuario

Args: 
    id (str): describe la id de un cliente.

return:
    registrar: registra la asistencia el la tabla de asistencia con una fecha 
"""
def registrarAsistencia(datos, self): 
    #reproducir_sonido()
    if int(datos[7]) == 1:
        def funcion_despues_del_temporizador(label): #sirve para destruir las ventanas de asistencia del cliente
            global banderaDestroy
            if banderaDestroy:
                vencidoDark.destroy()
                label.destroy()
                label_deuda = customtkinter.CTkLabel(self.frame_asistencia, text="", fg_color="transparent")
                label_deuda.configure(text=f"")
                label_deuda.grid(row=6, column=1, pady=(0, 0), sticky="nsew")
        def timerBandera(): #sirve para darle un tiempo a lña ventana y que no se destroy
            global banderaDestroy
            banderaDestroy = True
        id_cliente,apellido,nombre, documento, correo, fecha_nacimiento, telefono, estado, id_cuota, deuda, plan, profesor, fecha, vencimiento, id_cliente2, id_cuota = datos
        fecha_vencimiento = datetime.strptime(vencimiento, "%d/%m/%Y")
        fecha_actual = datetime.strptime(actual, "%d/%m/%Y")
        #esto va a ser la imagen de la asistencia del cliente
        img_vencido = customtkinter.CTkImage(light_image=Image.open("./assets/casiVencidaLight.png"),
                                        dark_image=Image.open("./assets/casiVencidaDark.png"),
                                        size=(500, 200))
        texto_personalizado = f" \n                {nombre} {apellido}\n \n \n {plan}\n \n \n \n {vencimiento}\n"
        vencidoDark = customtkinter.CTkLabel(self.frame_asistencia, image=img_vencido, text=texto_personalizado,
                                                    font=("Arial", 14),
                                                    anchor="n")  # "w" significa alinear a la izquierda
        vencidoDark.grid(row=4, column=1, pady=(20,0), sticky="nsew")
        if (fecha_actual >= fecha_vencimiento):
                #esto va a ser la ventana de vencimiento de abajo
                banderaDestroy = False
                label_vencido = customtkinter.CTkLabel(self.frame_asistencia, text=f"CUOTA VENCIDA", fg_color="red")
                label_vencido.grid(row=5, column=1,sticky="nsew")
                self.frame_asistencia.after(7000, timerBandera) 
                self.frame_asistencia.after(8000, lambda: (funcion_despues_del_temporizador(label_vencido)))
                reproducir_sonido("vencido")
                
                #esto va a de al dia de abajo
                #ruido de vencimiento 
        if (fecha_actual < fecha_vencimiento):
            #ruido de cuota al dia
            banderaDestroy = False
            if (fecha_vencimiento-fecha_actual).days <= 5:
                label_vence = customtkinter.CTkLabel(self.frame_asistencia, text=f"VENCE EN {(fecha_vencimiento-fecha_actual).days} DÍAS", fg_color="yellow")
                label_vence.grid(row=5, column=1, pady=(0,0),sticky="nsew")
                self.frame_asistencia.after(7000, timerBandera) 
                self.frame_asistencia.after(8000, lambda: (funcion_despues_del_temporizador(label_vence)))        
            else:
                label_ALDIA = customtkinter.CTkLabel(self.frame_asistencia, text=f"CUOTA AL DIA", fg_color="green")
                label_ALDIA.grid(row=5, column=1,sticky="nsew")
                self.frame_asistencia.after(7000, timerBandera) 
                self.frame_asistencia.after(8000, lambda: (funcion_despues_del_temporizador(label_ALDIA)))
            reproducir_sonido("pago")
        #esto va a ser la ventana de deuda de abajo
        if int(deuda) > 0:
            label_deuda = customtkinter.CTkLabel(self.frame_asistencia, text="", fg_color="orange")
            label_deuda.configure(text=f"Deuda: {deuda}")
            label_deuda.grid(row=6, column=1, pady=(0, 0), sticky="nsew")
        else:
            label_deuda = customtkinter.CTkLabel(self.frame_asistencia, text="", fg_color="transparent")
            label_deuda.configure(text=f"")
            label_deuda.grid(row=6, column=1, pady=(0, 0), sticky="nsew")
        conn = sqlite3.connect("BaseDatos.db")
        cursor = conn.cursor()
        
        cursor.execute("INSERT INTO Asistencia (Cliente, Fecha) VALUES (?, ?)",
                            (id_cliente, actualFechaHora))
        print(actualFechaHora)
        conn.commit()
        conn.close()
    else:
        mensaje = f"El cliente no esta habilitado, fue dado de baja"
        messagebox.showinfo("Error", mensaje)


def controlAcceso(self):
        conexion = sqlite3.connect("BaseDatos.db")
        cursor = conexion.cursor()
        # Consultar la base de datos para obtener la lista
        cursor.execute("SELECT Nombre || ' ' || Apellido || ' ' || Documento AS NombreCompleto FROM Clientes")
        resultados = cursor.fetchall()
        lista_resultante = [tupla[0] for tupla in resultados]



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
        
        self.bind("<Return>", funcion_al_presionar_tecla)
        