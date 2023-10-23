import tkinter as tk
from tkcalendar import Calendar
from tkinter import PhotoImage
import customtkinter
import customtkinter as ctk
from customtkinter import CTk, CTkFrame, CTkButton
from PIL import ImageTk,Image
import tkinter as tk
import pygame
import sqlite3





import tkinter as tk
from tkcalendar import Calendar




    # Iniciar el bucle principal de la aplicación


def ventana_RegistrarCliente():
    RegistrarCielte = CTk()
    RegistrarCielte.geometry("800x600")
    RegistrarCielte.title("cuotas")
    

    imagen = ctk.CTkImage(light_image=Image.open("./assets/volver.png"),
                                dark_image=Image.open("./assets/volver.png"),
                                size=(30, 30))
    

    # Crear un botón con la imagen
    boton_con_imagen = ctk.CTkButton(RegistrarCielte, image=imagen,text="Volver", command=lambda: (cambiarVentana(RegistrarCielte, ventana_main)))
    boton_con_imagen.place(relx=0.03, rely=0.03)
    #FrameClientes
    frame = customtkinter.CTkFrame(master=RegistrarCielte, width=320, height=600, corner_radius=15, border_color="black",border_width=12)
    frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    #LABEL TITULO
    label_titulo = customtkinter.CTkLabel(master=frame, text="Registrar clientes", font=('Century Gothic',20))
    label_titulo.place(relx=0.26, rely=0.03)

    #Entradas
    label_nombre = customtkinter.CTkLabel(master=frame, text="Nombre", font=('Century Gothic',15))
    label_nombre.place(relx=0.32, rely=0.1)
    entry_nombre = customtkinter.CTkEntry(master=frame, width=120, height=25, corner_radius=10)
    entry_nombre.place(relx=0.5, rely=0.16, anchor=tk.CENTER)

    label_apellido = customtkinter.CTkLabel(master=frame, text="Apellido", font=('Century Gothic',15))
    label_apellido.place(relx=0.32, rely=0.2)
    entry_apellido = customtkinter.CTkEntry(master=frame, width=120, height=25, corner_radius=10)
    entry_apellido.place(relx=0.5, rely=0.26, anchor=tk.CENTER)

    label_documento = customtkinter.CTkLabel(master=frame, text="Documento", font=('Century Gothic',15))
    label_documento.place(relx=0.32, rely=0.3)
    entry_documento = customtkinter.CTkEntry(master=frame, width=120, height=25, corner_radius=10)
    entry_documento.place(relx=0.5, rely=0.36, anchor=tk.CENTER)

    label_correo = customtkinter.CTkLabel(master=frame, text="Correo", font=('Century Gothic',15))
    label_correo.place(relx=0.32, rely=0.4)
    entry_correo = customtkinter.CTkEntry(master=frame, width=120, height=25, corner_radius=10)
    entry_correo.place(relx=0.5, rely=0.46, anchor=tk.CENTER)

    label_telefono = customtkinter.CTkLabel(master=frame, text="Telefono", font=('Century Gothic',15))
    label_telefono.place(relx=0.32, rely=0.5)
    entry_telefono = customtkinter.CTkEntry(master=frame, width=120, height=25, corner_radius=10)
    entry_telefono.place(relx=0.5, rely=0.56, anchor=tk.CENTER)



    label_fechaNacimiento = customtkinter.CTkLabel(master=frame, text="Fecha de nacimiento", font=('Century Gothic',15)) # se ingresa ejemplo "año-mes-dia"
    label_fechaNacimiento.place(relx=0.32, rely=0.58)

    frameCalendario = customtkinter.CTkFrame(master=frame, width=300, height=300)
    frameCalendario.place(relx=0.5, rely=0.75, anchor=tk.CENTER)
    
    # Crear un objeto Calendar
    cal = Calendar(frameCalendario, selectmode="day", year=2023, month=10, day=23)

    # Colocar los widgets en la ventana
    cal.pack(pady=10)

    
    #boton confirmar
    button_confirmar = customtkinter.CTkButton(
        master=frame,
        width=220,
        text="Confirmar",
        command=lambda: agregar_cliente([entry_nombre.get(),entry_apellido.get(), entry_correo.get(), entry_documento.get(), cal.get_date()(), entry_telefono.get()]),
        corner_radius=6
    )
    button_confirmar.place(relx=0.18, rely=0.90)

    RegistrarCielte.mainloop()
ventana_RegistrarCliente()