
from tkinter import PhotoImage
import customtkinter
import customtkinter as ctk
from customtkinter import CTk, CTkFrame, CTkButton
import PIL.Image
from PIL import ImageTk,Image
from tkinter import *
import tkinter as tk
import pygame
import sqlite3
from tkcalendar import Calendar

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")
#import de utilerias de sqlite
from database_utils import agregar_cliente,registrarPago

conn = sqlite3.connect('BaseDatos.db') #vinculo la base de datos

cursor = conn.cursor() # este es mi curson que me permite realizar consultar y modificaciona a la bd



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
    
    clientes = tk.Tk()
    clientes.attributes("-fullscreen","false")
    clientes.title("clientes")
    clientes.state('zoomed')

            # Cargar una imagen para volver atras
    imagen = ctk.CTkImage(light_image=PIL.Image.open("./assets/volver.png"),
                                dark_image=PIL.Image.open("./assets/volver.png"),
                                size=(30, 30))
    
    img1=ImageTk.PhotoImage(PIL.Image.open("./assets/gym2.png"))


    l1=customtkinter.CTkLabel(master=clientes,image=img1)
    l1.pack()
    boton_con_imagen = ctk.CTkButton(clientes, image=imagen,text="Volver", command=lambda: (cambiarVentana(clientes, ventana_main)))
    boton_con_imagen.place(relx=0.03, rely=0.03)
    
    
        #FrameClientes

    
    frame=customtkinter.CTkFrame(master=clientes, width=320, height=360, corner_radius=15,border_width=12,border_color="black")
    frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    


    #Mensaje
    msjPrincipal=customtkinter.CTkLabel(master=frame, text="Mis Clientes",font=('Century Gothic',20))
    msjPrincipal.place(x=50, y=45)
    button_registrarCliente = customtkinter.CTkButton(master=frame, width=220, text="REGISTRAR NUEVO CLIENTE", command = lambda :cambiarVentana(clientes, ventana_RegistrarCliente), corner_radius=6)#clientes
    button_registrarCliente.place(x=50, y=110)


    button_actualizarCliente = customtkinter.CTkButton(master=frame, width=220, text="ACTUALIZAR CLIENTE", command=lambda: (cambiarVentana(clientes, ventana_ActualizarClientes)), corner_radius=6)#clientes
    button_actualizarCliente.place(x=50, y=165)
    
    button_consultarCliente = customtkinter.CTkButton(master=frame, width=220, text="CONSULTAR CLIENTE", command=click_boton, corner_radius=6)#clientes
    button_consultarCliente.place(x=50, y=220)


    clientes.mainloop()


def ventana_RegistrarCliente():
    RegistrarCliente = tk.Tk()
    RegistrarCliente.geometry("1200x600")
    RegistrarCliente.title("cuotas")
    RegistrarCliente.state('zoomed')
    

    imagen = ctk.CTkImage(light_image=PIL.Image.open("./assets/volver.png"),
                                dark_image=PIL.Image.open("./assets/volver.png"),
                                size=(30, 30))
    
    img1=ImageTk.PhotoImage(PIL.Image.open("./assets/gym2.png"))


    l1=customtkinter.CTkLabel(master=RegistrarCliente,image=img1)
    l1.pack()
    # Crear un botón con la imagen
    boton_con_imagen = ctk.CTkButton(RegistrarCliente, image=imagen,text="Volver", command=lambda: (cambiarVentana(RegistrarCliente, ventana_main)))
    boton_con_imagen.place(relx=0.03, rely=0.03)
    #FrameClientes

    
    frame = customtkinter.CTkFrame(master=RegistrarCliente, width=800, height=800, corner_radius=15, border_color="black",border_width=12)
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
        command=lambda: agregar_cliente([entry_nombre.get(),entry_apellido.get(), entry_correo.get(), entry_documento.get(), cal.get_date(), entry_telefono.get()]),
        corner_radius=6
    )
    button_confirmar.place(relx=0.18, rely=0.90)

    RegistrarCliente.mainloop()

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

        self.label_Documento = ctk.CTkLabel(frame, text="Documento:")
        self.label_Documento.grid(row=2, column=0)
        self.Documento_entry = ctk.CTkEntry(frame)
        self.Documento_entry.grid(row=2, column=1)

        self.label_Correo = ctk.CTkLabel(frame, text="Correo:")
        self.label_Correo.grid(row=2, column=2)
        self.Correo_entry = ctk.CTkEntry(frame)
        self.Correo_entry.grid(row=2, column=3)

        self.label_FechaNacimiento = ctk.CTkLabel(frame, text="Fecha de nacimiento:")
        self.label_FechaNacimiento.grid(row=3, column=0)
        self.FechaNacimiento_entry = ctk.CTkEntry(frame)
        self.FechaNacimiento_entry.grid(row=3, column=1)

        self.label_Telefono = ctk.CTkLabel(frame, text="Telefono:")
        self.label_Telefono.grid(row=3, column=2)
        self.Telefono_entry = ctk.CTkEntry(frame)
        self.Telefono_entry.grid(row=3, column=3)




        # Crear botones
        self.btn_agregar = ctk.CTkButton(frame, text="Agregar", command=self.agregar)
        self.btn_agregar.grid(row=4, column=0)

        self.btn_actualizar = ctk.CTkButton(frame, text="Actualizar", command=self.actualizar)
        self.btn_actualizar.grid(row=4, column=2)



        # Crear una lista para mostrar los datos de la base de datos
        self.lista_programas = tk.Listbox(frame)
        self.lista_programas.grid(row=5, column=0, columnspan=4, sticky=tk.W + tk.E + tk.N + tk.S)
        self.mostrar_programas()

        # Asignar una función para manejar la selección en la lista
        self.lista_programas.bind('<<ListboxSelect>>', self.seleccionar_programa)

    def mostrar_programas(self):
        self.lista_programas.delete(0, ctk.END)
        programas = self.cursor.execute('SELECT * FROM Clientes').fetchall()
        for programa in programas:
            _, nombre, apellido, correo, documento, fechaNacimiento, telefono = programa  # Obtener los dos últimos elementos de la tupla
            self.lista_programas.insert(ctk.END, (apellido, nombre, correo, documento, fechaNacimiento, telefono))


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

    def limpiar_campos(self):
        self.Apellido_entry.delete(0, ctk.END)
        self.nombre_entry.delete(0, ctk.END)
        self.FechaNacimiento_entry.delete(0, tk.END)
        self.Correo_entry.delete(0, ctk.END)
        self.Documento_entry.delete(0, ctk.END)
        self.Telefono_entry.delete(0, ctk.END)

    def __del__(self):
        self.conexion.close()

def ventana_ActualizarClientes():
    actualizarClientes = tk.Tk()
    actualizarClientes.attributes("-fullscreen","false")
    actualizarClientes.title("Actualizar precios")
    actualizarClientes.state('zoomed')

    imagen = customtkinter.CTkImage(light_image=PIL.Image.open("./assets/volver.png"),
                                dark_image=PIL.Image.open("./assets/volver.png"),
                                size=(30, 30))
    
    img1=ImageTk.PhotoImage(PIL.Image.open("./assets/gym2.png"))


    l1=customtkinter.CTkLabel(master=actualizarClientes,image=img1)
    l1.pack()
    boton_con_imagen = ctk.CTkButton(text="Volver", master=actualizarClientes, image=imagen, command=lambda: (cambiarVentana(actualizarClientes, ventana_clientes)))
    boton_con_imagen.place(relx=0.03, rely=0.03)

    frame1=customtkinter.CTkFrame(master=actualizarClientes, width=600, height=440, corner_radius=15, border_width=12, border_color="black")
    frame1.place(relx=0.5, rely=0.5, anchor="center")

    #FrameClientes
    frame = ctk.CTkFrame(master=actualizarClientes, width=300, height=100)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    ProgramaABM_Clientes(frame)
    actualizarClientes.mainloop()


class ProgramaABM:
    def __init__(self, frame):
        self.frame = frame

        # Conectarse a la base de datos SQLite
        self.conexion = sqlite3.connect("BaseDatos.db")
        self.cursor = self.conexion.cursor()
        self.conexion.commit()

        # Crear etiquetas y campos de entrada
        self.label_nombre = customtkinter.CTkLabel(frame, text="Nombre:")
        self.label_nombre.grid(row=1, column=0)
        self.nombre_entry = customtkinter.CTkEntry(frame)
        self.nombre_entry.grid(row=1, column=1)

        self.label_precio = customtkinter.CTkLabel(frame, text="Precio:")
        self.label_precio.grid(row=2, column=0)
        self.precio_entry = customtkinter.CTkEntry(frame)
        self.precio_entry.grid(row=2, column=1)

        # Crear botones
        self.btn_agregar = customtkinter.CTkButton(frame, text="Agregar", command=self.agregar)
        self.btn_agregar.grid(row=3, column=0)

        self.btn_actualizar = customtkinter.CTkButton(frame, text="Actualizar", command=self.actualizar)
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
            _, _, precio, nombre = programa  # Obtener los dos últimos elementos de la tupla
            self.lista_programas.insert(tk.END, (precio, nombre))

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
        precio, nombre = programa
        self.nombre_entry.delete(0, tk.END)
        self.nombre_entry.insert(0, nombre)
        self.precio_entry.delete(0, tk.END)
        self.precio_entry.insert(0, precio)

    def limpiar_campos(self):
        self.nombre_entry.delete(0, tk.END)
        self.precio_entry.delete(0, tk.END)

    def __del__(self):
        self.conexion.close()

def ventana_ActualizarPrecios():
    actualizarPrograma = tk.Tk()
    actualizarPrograma.attributes("-fullscreen","false")
    actualizarPrograma.title("Actualizar precios")
    actualizarPrograma.state('zoomed')

    imagen = ctk.CTkImage(light_image=PIL.Image.open("./assets/volver.png"),
                                  dark_image=PIL.Image.open("./assets/volver.png"),
                                  size=(30, 30))
    

    img1=ImageTk.PhotoImage(PIL.Image.open("./assets/gym2.png"))


    l1=customtkinter.CTkLabel(master=actualizarPrograma,image=img1)
    l1.pack()
    boton_con_imagen = ctk.CTkButton(master=actualizarPrograma, image=imagen,text="Volver", command=lambda: (cambiarVentana(actualizarPrograma, ventana_main)))
    boton_con_imagen.place(relx=0.03, rely=0.03)
    frame1=customtkinter.CTkFrame(master=actualizarPrograma, width=320, height=360, corner_radius=15, border_width=12)
    frame1.place(relx=0.5, rely=0.5, anchor="center")
    

    #FrameClientes
    frame = CTkFrame(master=actualizarPrograma, width=320, height=360, corner_radius=15)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    ProgramaABM(frame)
    actualizarPrograma.mainloop()



def ventana_Programa():
    jaja()
    
    programa = tk.Tk()
    programa.attributes("-fullscreen","false")
    programa.title("clientes")

    imagen = ctk.CTkImage(light_image=PIL.Image.open("./assets/volver.png"),
                                  dark_image=PIL.Image.open("./assets/volver.png"),
                                  size=(30, 30))
    

    # Crear un botón con la imagen
    boton_con_imagen = ctk.CTkButton(programa, image=imagen,text="Volver", command=lambda: (cambiarVentana(programa, ventana_main)))
    boton_con_imagen.place(relx=0.03, rely=0.03)



        #FrameClientes
    frame=customtkinter.CTkFrame(master=programa, width=320, height=360, corner_radius=15)
    frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    


    #Mensaje
    msjPrincipal=customtkinter.CTkLabel(master=frame, text="Planes",font=('Century Gothic',20))
    msjPrincipal.place(x=50, y=45)
    button_registrarCliente = customtkinter.CTkButton(master=frame, width=220, text="COBRAR PAGO", command=click_boton, corner_radius=6)#clientes
    button_registrarCliente.place(x=50, y=110)


    button_consultarCliente = customtkinter.CTkButton(master=frame, width=220, text="ACTUALIZAR PRECIO", command= lambda : (cambiarVentana(programa, ventana_ActualizarPrecios)), corner_radius=6)#clientes
    button_consultarCliente.place(x=50, y=220)


    programa.mainloop()



def ventana_pagoCuota():  #pagoCuota
    Cuotas = tk.Tk()
    Cuotas.attributes("-fullscreen","false")
    Cuotas.geometry("1200x800")
    Cuotas.title("cuotas")
    Cuotas.state('zoomed')
    

    # Cargar una imagen para volver atras
    imagen = ctk.CTkImage(light_image=PIL.Image.open("./assets/volver.png"),
                            dark_image=PIL.Image.open("./assets/volver.png"),
                            size=(30, 30))
    

    img1=ImageTk.PhotoImage(PIL.Image.open("./assets/gym2.png"))


    l1=customtkinter.CTkLabel(master=Cuotas,image=img1)
    l1.pack()
    boton_con_imagen = ctk.CTkButton(Cuotas, image=imagen,text="Volver", command=lambda: (cambiarVentana(Cuotas, ventana_main)))
    boton_con_imagen.place(relx=0.03, rely=0.03)
    #FrameClientes

    frame = customtkinter.CTkFrame(master=Cuotas, width=600, height=700, corner_radius=15)
    frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


    #LABEL TITULO
    label_titulo = customtkinter.CTkLabel(master=frame, text="PAGO DE CUOTA", font=('Century Gothic',20))
    label_titulo.place(relx=0.36, rely=0.1)

    #Entradas
    label_cliente = customtkinter.CTkLabel(master=frame, text="Cliente", font=('Century Gothic',15))
    label_cliente.place(relx=0.45, rely=0.2)
    entry_cliente = customtkinter.CTkEntry(master=frame, width=220, height=25, corner_radius=10)
    entry_cliente.place(relx=0.5, rely=0.26, anchor=tk.CENTER)

    label_programa = customtkinter.CTkLabel(master=frame, text="Programa", font=('Century Gothic',15))
    label_programa.place(relx=0.44, rely=0.3)
    entry_programa = customtkinter.CTkEntry(master=frame, width=220, height=25, corner_radius=10)
    entry_programa.place(relx=0.5, rely=0.36, anchor=tk.CENTER)

    label_pago = customtkinter.CTkLabel(master=frame, text="Pago $", font=('Century Gothic',15))
    label_pago.place(relx=0.44, rely=0.4)
    entry_pago = customtkinter.CTkEntry(master=frame, width=120, height=25, corner_radius=10)
    entry_pago.place(relx=0.5, rely=0.46, anchor=tk.CENTER)

    label_profesor = customtkinter.CTkLabel(master=frame, text="Profesor", font=('Century Gothic',15))
    label_profesor.place(relx=0.44, rely=0.5)
    entry_profesor = customtkinter.CTkEntry(master=frame, width=220, height=25, corner_radius=10)
    entry_profesor.place(relx=0.5, rely=0.56, anchor=tk.CENTER)
    
    label_fecha= customtkinter.CTkLabel(master=frame, text="Fecha", font=('Century Gothic',15)) 
    label_fecha.place(relx=0.45, rely=0.6)
    frameCalendario = customtkinter.CTkFrame(master=frame, width=300, height=300)
    frameCalendario.place(relx=0.5, rely=0.75, anchor=tk.CENTER)
    
    # Crear un objeto Calendar
    cal = Calendar(frameCalendario, selectmode="day", year=2023, month=10, day=23)

    # Colocar los widgets en la ventana
    cal.pack(pady=10)


    
    button_confirmar = customtkinter.CTkButton(
        master=frame,
        width=220,
        text="Confirmar",
        command=lambda: registrarPago([entry_cliente.get(), entry_pago.get(), entry_programa.get(), entry_profesor.get(), cal.get_date()]),
            
        corner_radius=6
    )
    button_confirmar.place(relx=0.33, rely=0.9)

    Cuotas.mainloop()


    
def button_function():
        w = customtkinter.CTk()  
        w.geometry("1280x720")
        w.title('Welcome')
        l1=customtkinter.CTkLabel(master=w, text="INFORMACION CLIENTES",font=('Century Gothic',60))
        l1.place(relx=0.5, rely=0.5,  anchor=tk.CENTER)
        w.mainloop()
    



def ventana_main():
    app = tk.Tk()  #creating cutstom tkinter window

    app.title('SALUD INTEGRAL')
    app.iconbitmap("./assets/logo.ico")
    app.state('zoomed')
    img1=ImageTk.PhotoImage(PIL.Image.open("./assets/gym2.png"))

    
    l1=customtkinter.CTkLabel(master=app,image=img1)
    l1.pack()

    #creating custom frame
    frame=customtkinter.CTkFrame(master=l1, width=320, height=360, corner_radius=15)
    frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    l2=customtkinter.CTkLabel(master=frame, text="Welcome",font=('Century Gothic',20))
    l2.place(x=50, y=45)

        #Botones
    button_Clientes = customtkinter.CTkButton(master=frame, width=220, text="Customer", command=lambda: (cambiarVentana(app, ventana_clientes)), corner_radius=6)#clientes
    button_Clientes.place(x=50, y=110)


    button_pagoCuota = customtkinter.CTkButton(master=frame, width=220, text="Payment", command=lambda: (cambiarVentana(app, ventana_pagoCuota)), corner_radius=6)#pago cuota
    button_pagoCuota.place(x=50, y=165)


    button_cerrar= customtkinter.CTkButton(master=frame, width=100, height=20,text="Close this", command=lambda: (app.destroy()), compound="left", fg_color='white', text_color='black', hover_color='#AFAFAF')
    button_cerrar.place(x=110, y=220)


    app.mainloop()

ventana_main()