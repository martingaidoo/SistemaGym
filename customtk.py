import tkinter
from tkinter import PhotoImage
import customtkinter
from customtkinter import CTk, CTkFrame, CTkButton
from PIL import ImageTk,Image
import tkinter as tk
import pygame
import sqlite3


#import de utilerias de sqlite
from database_utils import agregar_cliente

import abm

conn = sqlite3.connect('BaseDatos.db') #vinculo la base de datos

cursor = conn.cursor() # este es mi curson que me permite realizar consultar y modificaciona a la bd



customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green
def jaja():
    
        pygame.init()
        pygame.mixer.init()
        sonido = pygame.mixer.Sound("coin.mp3")
        pygame.mixer.Sound.play(sonido)
        
    

def click_boton():
    print("hiciste click")
    jaja()

def cambiarVentana(ventanaActual, ventanaCambiar):
    ventanaActual.destroy()
    ventanaCambiar()



def ventana_clientes():  #VENTANA DE CLIENTES
    jaja()
    
    clientes = CTk()
    clientes.geometry("600x440")
    clientes.config(bg = "#7f5af0") 
    clientes.title("clientes")

            # Cargar una imagen para volver atras
    imagen = tk.PhotoImage(file="./assets/volver.png")

    # Crear un botón con la imagen
    boton_con_imagen = tk.Button(clientes, image=imagen, command=lambda: (cambiarVentana(clientes, ventana_main)))
    boton_con_imagen.place(relx=0.03, rely=0.03)
    
    
        #FrameClientes
    frame=customtkinter.CTkFrame(master=clientes, width=320, height=360, corner_radius=15)
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    


    #Mensaje
    msjPrincipal=customtkinter.CTkLabel(master=frame, text="Mis Clientes",font=('Century Gothic',20))
    msjPrincipal.place(x=50, y=45)
    button_registrarCliente = customtkinter.CTkButton(master=frame, width=220, text="REGISTRAR NUEVO CLIENTE", command = lambda :cambiarVentana(clientes, ventana_RegistrarCliente), corner_radius=6)#clientes
    button_registrarCliente.place(x=50, y=110)


    button_actualizarCliente = customtkinter.CTkButton(master=frame, width=220, text="ACTUALIZAR CLIENTE", command=click_boton, corner_radius=6)#clientes
    button_actualizarCliente.place(x=50, y=165)
    
    button_consultarCliente = customtkinter.CTkButton(master=frame, width=220, text="CONSULTAR CLIENTE", command=click_boton, corner_radius=6)#clientes
    button_consultarCliente.place(x=50, y=220)


    clientes.mainloop()


def ventana_RegistrarCliente():
    RegistrarCielte = CTk()
    RegistrarCielte.geometry("600x440")
    RegistrarCielte.config(bg = "#7f5af0") 
    RegistrarCielte.title("cuotas")
    

    # Cargar una imagen para volver atras
    imagen = tk.PhotoImage(file="./assets/volver.png")

    # Crear un botón con la imagen
    boton_con_imagen = tk.Button(RegistrarCielte, image=imagen, command=lambda: (cambiarVentana(RegistrarCielte, ventana_clientes)))
    boton_con_imagen.place(relx=0.03, rely=0.03)

    #FrameClientes
    frame = customtkinter.CTkFrame(master=RegistrarCielte, width=320, height=500, corner_radius=15)
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    #LABEL TITULO
    label_titulo = customtkinter.CTkLabel(master=frame, text="Registrar clientes", font=('Century Gothic',20))
    label_titulo.place(relx=0.26, rely=0.05)

    #Entradas
    label_nombre = customtkinter.CTkLabel(master=frame, text="Nombre", font=('Century Gothic',15))
    label_nombre.place(relx=0.32, rely=0.15)
    entry_nombre = customtkinter.CTkEntry(master=frame, width=120, height=25, corner_radius=10)
    entry_nombre.place(relx=0.5, rely=0.22, anchor=tkinter.CENTER)

    label_apellido = customtkinter.CTkLabel(master=frame, text="Apellido", font=('Century Gothic',15))
    label_apellido.place(relx=0.32, rely=0.27)
    entry_apellido = customtkinter.CTkEntry(master=frame, width=120, height=25, corner_radius=10)
    entry_apellido.place(relx=0.5, rely=0.34, anchor=tkinter.CENTER)

    label_documento = customtkinter.CTkLabel(master=frame, text="Documento", font=('Century Gothic',15))
    label_documento.place(relx=0.32, rely=0.39)
    entry_documento = customtkinter.CTkEntry(master=frame, width=120, height=25, corner_radius=10)
    entry_documento.place(relx=0.5, rely=0.46, anchor=tkinter.CENTER)

    label_correo = customtkinter.CTkLabel(master=frame, text="Correo", font=('Century Gothic',15))
    label_correo.place(relx=0.32, rely=0.51)
    entry_correo = customtkinter.CTkEntry(master=frame, width=120, height=25, corner_radius=10)
    entry_correo.place(relx=0.5, rely=0.58, anchor=tkinter.CENTER)

    label_telefono = customtkinter.CTkLabel(master=frame, text="Telefono", font=('Century Gothic',15))
    label_telefono.place(relx=0.32, rely=0.63)
    entry_telefono = customtkinter.CTkEntry(master=frame, width=120, height=25, corner_radius=10)
    entry_telefono.place(relx=0.5, rely=0.70, anchor=tkinter.CENTER)


    label_fechaNacimiento = customtkinter.CTkLabel(master=frame, text="Fecha de nacimiento", font=('Century Gothic',15)) # se ingresa ejemplo "año-mes-dia"
    label_fechaNacimiento.place(relx=0.32, rely=0.75)
    entry_fechaNacimiento = customtkinter.CTkEntry(master=frame, width=120, height=25, corner_radius=10)
    entry_fechaNacimiento.place(relx=0.5, rely=0.82, anchor=tkinter.CENTER)

    
    #boton confirmar
    button_confirmar = customtkinter.CTkButton(
        master=frame,
        width=220,
        text="Confirmar",
        command=lambda: agregar_cliente([entry_nombre.get(),entry_apellido.get(), entry_correo.get(), entry_documento.get(), entry_fechaNacimiento.get(), entry_telefono.get()]),
        corner_radius=6
    )
    button_confirmar.place(relx=0.18, rely=0.90)

    RegistrarCielte.mainloop()

class ProgramaABM:
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

        self.label_precio = tk.Label(frame, text="Precio:")
        self.label_precio.grid(row=2, column=0)
        self.precio_entry = tk.Entry(frame)
        self.precio_entry.grid(row=2, column=1)

        # Crear botones
        self.btn_agregar = tk.Button(frame, text="Agregar", command=self.agregar)
        self.btn_agregar.grid(row=3, column=0)

        self.btn_actualizar = tk.Button(frame, text="Actualizar", command=self.actualizar)
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
            self.lista_programas.insert(tk.END, programa)

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
        _, _, precio, nombre = programa
        self.nombre_entry.delete(0, tk.END)
        self.nombre_entry.insert(0, nombre)
        self.precio_entry.delete(0, tk.END)
        self.precio_entry.insert(0, precio)

    def limpiar_campos(self):
        self.nombre_entry.delete(0, tk.END)
        self.precio_entry.delete(0, tk.END)

    def __del__(self):
        self.conexion.close()

def ventana_AcutalizarPrecios():
    actualizarPrograma = tk.Tk()
    actualizarPrograma.geometry("600x440")
    actualizarPrograma.config(bg="#7f5af0")
    actualizarPrograma.title("Actualizar precios")

        # Cargar una imagen para volver atras
    imagen = tk.PhotoImage(file="./assets/volver.png")

    # Crear un botón con la imagen
    boton_con_imagen = tk.Button(actualizarPrograma, image=imagen, command=lambda: (cambiarVentana(actualizarPrograma, ventana_Programa)))
    boton_con_imagen.place(relx=0.03, rely=0.03)

    frame1=customtkinter.CTkFrame(master=actualizarPrograma, width=320, height=360, corner_radius=15)
    frame1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    

    #FrameClientes
    frame = tk.Frame(actualizarPrograma, width=320, height=360)
    frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    app = ProgramaABM(frame)
    actualizarPrograma.mainloop()



def ventana_Programa():
    jaja()
    
    programa = CTk()
    programa.geometry("600x440")
    programa.config(bg = "#7f5af0") 
    programa.title("clientes")

        # Cargar una imagen para volver atras
    imagen = tk.PhotoImage(file="./assets/volver.png")

    # Crear un botón con la imagen
    boton_con_imagen = tk.Button(programa, image=imagen, command=lambda: (cambiarVentana(programa, ventana_main)))
    boton_con_imagen.place(relx=0.03, rely=0.03)



        #FrameClientes
    frame=customtkinter.CTkFrame(master=programa, width=320, height=360, corner_radius=15)
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    


    #Mensaje
    msjPrincipal=customtkinter.CTkLabel(master=frame, text="Planes",font=('Century Gothic',20))
    msjPrincipal.place(x=50, y=45)
    button_registrarCliente = customtkinter.CTkButton(master=frame, width=220, text="COBRAR PAGO", command=click_boton, corner_radius=6)#clientes
    button_registrarCliente.place(x=50, y=110)


    button_consultarCliente = customtkinter.CTkButton(master=frame, width=220, text="ACTUALIZAR PRECIO", command= lambda : (cambiarVentana(programa, ventana_AcutalizarPrecios)), corner_radius=6)#clientes
    button_consultarCliente.place(x=50, y=220)


    programa.mainloop()



def ventana_pagoCuota():  #pagoCuota
    Cuotas = CTk()
    Cuotas.geometry("600x440")
    Cuotas.config(bg = "#7f5af0") 
    Cuotas.title("cuotas")
    

    # Cargar una imagen para volver atras
    imagen = tk.PhotoImage(file="./assets/volver.png")

    # Crear un botón con la imagen
    boton_con_imagen = tk.Button(Cuotas, image=imagen, command=lambda: (cambiarVentana(Cuotas, ventana_main)))
    boton_con_imagen.place(relx=0.03, rely=0.03)

    #FrameClientes
    frame = customtkinter.CTkFrame(master=Cuotas, width=320, height=360, corner_radius=15)
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    #LABEL TITULO
    label_titulo = customtkinter.CTkLabel(master=frame, text="PAGO DE CUOTA", font=('Century Gothic',20))
    label_titulo.place(relx=0.26, rely=0.1)

    #Entradas
    label_cliente = customtkinter.CTkLabel(master=frame, text="Cliente", font=('Century Gothic',15))
    label_cliente.place(relx=0.32, rely=0.2)
    entry_cliente = customtkinter.CTkEntry(master=frame, width=120, height=25, corner_radius=10)
    entry_cliente.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

    label_programa = customtkinter.CTkLabel(master=frame, text="programa", font=('Century Gothic',15))
    label_programa.place(relx=0.32, rely=0.35)
    entry_programa = customtkinter.CTkEntry(master=frame, width=120, height=25, corner_radius=10)
    entry_programa.place(relx=0.5, rely=0.45, anchor=tkinter.CENTER)

    label_pago = customtkinter.CTkLabel(master=frame, text="pago", font=('Century Gothic',15))
    label_pago.place(relx=0.32, rely=0.5)
    entry_pago = customtkinter.CTkEntry(master=frame, width=120, height=25, corner_radius=10)
    entry_pago.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

    label_profesor = customtkinter.CTkLabel(master=frame, text="profesor", font=('Century Gothic',15))
    label_profesor.place(relx=0.32, rely=0.65)
    entry_profesor = customtkinter.CTkEntry(master=frame, width=120, height=25, corner_radius=10)
    entry_profesor.place(relx=0.5, rely=0.75, anchor=tkinter.CENTER)
    
    #boton confirmar
    button_confirmar = customtkinter.CTkButton(
        master=frame,
        width=220,
        text="Confirmar",
        command=lambda: print(
            "Cliente:", entry_cliente.get(),
            "Programa:", entry_programa.get(),
            "Pago:", entry_pago.get(),
            "Profesor:", entry_profesor.get()
        ),
        corner_radius=6
    )
    button_confirmar.place(relx=0.18, rely=0.85)

    Cuotas.mainloop()


    
def button_function():
        w = customtkinter.CTk()  
        w.geometry("1280x720")
        w.title('Welcome')
        l1=customtkinter.CTkLabel(master=w, text="INFORMACION CLIENTES",font=('Century Gothic',60))
        l1.place(relx=0.5, rely=0.5,  anchor=tkinter.CENTER)
        w.mainloop()
    



def ventana_main():
    app = customtkinter.CTk()  #creating cutstom tkinter window
    app.geometry("600x440")
    app.title('SALUD INTEGRAL')
    app.iconbitmap("./assets/logo.ico")
    img1=ImageTk.PhotoImage(Image.open("./assets/gym1.jpg"))


    l1=customtkinter.CTkLabel(master=app,image=img1)
    l1.pack()

    #creating custom frame
    frame=customtkinter.CTkFrame(master=l1, width=320, height=360, corner_radius=15)
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    l2=customtkinter.CTkLabel(master=frame, text="Bienvenido",font=('Century Gothic',20))
    l2.place(x=50, y=45)

        #Botones
    button_Clientes = customtkinter.CTkButton(master=frame, width=220, text="Clientes", command=lambda: (cambiarVentana(app, ventana_clientes)), corner_radius=6)#clientes
    button_Clientes.place(x=50, y=110)


    button_pagoCuota = customtkinter.CTkButton(master=frame, width=220, text="Pago Cuota", command=lambda: (cambiarVentana(app, ventana_pagoCuota)), corner_radius=6)#pago cuota
    button_pagoCuota.place(x=50, y=165)

    button_programa = customtkinter.CTkButton(master=frame, width=220, text="Programa", command=lambda: (cambiarVentana(app, ventana_Programa)), corner_radius=6)
    button_programa.place(x=50, y=220) 
    button_cerrar= customtkinter.CTkButton(master=frame, width=100, height=20,text="Cerrar", command=lambda: (app.destroy()), compound="left", fg_color='white', text_color='black', hover_color='#AFAFAF')
    button_cerrar.place(x=170, y=290)

        # You can easily integrate authentication system 
    app.mainloop()

ventana_main()
