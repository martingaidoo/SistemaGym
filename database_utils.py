import tkinter
from tkinter import PhotoImage
import customtkinter
from customtkinter import CTk, CTkFrame, CTkButton
from PIL import ImageTk,Image
import tkinter as tk
import pygame
import sqlite3
from datetime import datetime
from dateutil.relativedelta import relativedelta
from tkinter import messagebox

# Obtener la fecha actual
fecha_actual = datetime.now()

fecha_con_mes_adicional = fecha_actual + relativedelta(months=1)

# Formatear la fecha como días/mes/año
actual = fecha_actual.strftime("%d/%m/%Y")
actaulMasMes = fecha_con_mes_adicional.strftime("%d/%m/%Y")
#sirve para destrouit la ventada de la asistencia del cliente
banderaDestroy = True

def buscar_cliente_con_cuotas(documento):
    # Conectar con la base de datos
    conexion = sqlite3.connect('BaseDatos.db')
    cursor = conexion.cursor()

    # Ejecutar la consulta SQL para seleccionar la información del cliente por su documento
    cursor.execute("SELECT * FROM Clientes WHERE Documento = ?", (documento,))
    cliente = cursor.fetchone()  # Obtener el primer cliente que coincida con el documento
    
    if cliente:
        # Obtener las cuotas del cliente
        cursor.execute("SELECT * FROM Cuotas WHERE id_cliente = ?", (cliente[0],))
        cuotas = cursor.fetchone()
    else:
        cuotas = []

    # Cerrar la conexión con la base de datos
    conexion.close()

    return cliente, cuotas






""" en esta funcion registrara la asistencia de un usuario

Args: 
    id (str): describe la id de un cliente.

return:
    registrar: registra la asistencia el la tabla de asistencia con una fecha 
"""
def registrarAsistencia(datos, self): 
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
    id_cliente,apellido,nombre, documento, correo, fecha_nacimiento, telefono, id_cuota, deuda, plan, profesor, fecha, vencimiento, id_cliente2, id_cuota = datos
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
            #esto va a de al dia de abajo
    if (fecha_actual < fecha_vencimiento):
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
                        (id_cliente, actual))
    conn.commit()
    conn.close()

""" en esta funcion registrara un cliente nuevo

Args: 
    cliente_data (lista): describe una informacion que se extrae de las entradas en tkinter y son pasadas como lista

return:
    registrar: registra un nuevo cliente 
"""

def agregar_cliente(cliente_data):
    # Conectar a la base de datos SQLite (asegúrate de que la base de datos exista)
    conn = sqlite3.connect("BaseDatos.db")
    cursor = conn.cursor()
    # Obtener los datos del cliente
    nombre, apellido, correo, documento, fecha_nacimiento, telefono = cliente_data
    # Verificar que ningún dato esté vacío
    if apellido and nombre and documento and correo and fecha_nacimiento and telefono:
        try:
            # Insertar los datos en la tabla
            cursor.execute("INSERT INTO Clientes (Apellido, Nombre, Documento, Correo, Fecha_Nacimiento, Telefono) VALUES (?, ?, ?, ?, ?, ?)",
                        (apellido, nombre, documento, correo, fecha_nacimiento, telefono))
            # Confirmar la transacción
            conn.commit()
            mensaje = f"Registro de Cliente:\n\nNombre: {nombre}\nApellido: {apellido}\nDocumento: {documento}\nCorreo: {correo}\nNacimiento: {fecha_nacimiento}\nTelefono: {telefono}"
            messagebox.showinfo("Cliente Registrado", mensaje)
        except sqlite3.Error as e:
            conn.rollback()
        finally:
            conn.close()

""" en esta funcion registrara una cuota de un cliente

Args: 
    data (lista): describe una informacion que se extrae de las entradas en tkinter y son pasadas como lista

return:
    registrar: registra un nuevo cliente y su pago
    modificar: registra un nsu pago cuando la cuota esta venciuda actualizando la fecha de vencimiento y la fecha de emision
    modificar: registra la actualizacin de un pago de un cliente
"""
def registrarPago(data):
    # Conectar a la base de datos SQLite (asegúrate de que la base de datos exista)
    mixconexion = sqlite3.connect("BaseDatos.db")
    cursor = mixconexion.cursor()
    # Obtener los datos del cliente
    print(data)
    documento, Haber, Plan, Profesor= data
    cobro = Haber

    consulta = """
    SELECT * FROM Clientes WHERE Documento = ?;
    """
    cursor.execute(consulta, (documento,)) 


    datos_cliente = cursor.fetchone()
    id_cliente = datos_cliente[0]

    consulta = """
    SELECT * FROM Programa WHERE Nombre = ?;
    """
    cursor.execute(consulta, (Plan,)) 
    datos_programa = cursor.fetchone()
    id_programa = datos_programa[0]

    consulta = """
    SELECT * FROM Cuotas id_cliente WHERE id_cliente = ?;
    """
    cursor.execute(consulta, (id_cliente,)) 
    datos_cuota = cursor.fetchone()

    #datos de las fechas de la cuota que existe para verificar si esta vendico
    if not (datos_cuota == None):
        fecha_actual = datetime.strptime(actual, "%d/%m/%Y")
        fecha_vencimiento = datetime.strptime(datos_cuota[5], "%d/%m/%Y")

    # Verificar que ningún dato esté vacío
    if id_cliente and Haber and Plan and Profesor:
        #variable que verifica si es el primer pago que hace
        if datos_cuota == None:
            try:
                Haber = str(int(datos_programa[2])-int(Haber))
                # Insertar los datos en la tabla
                cursor.execute("INSERT INTO Cuotas (id, Haber, PLAN, PROFESOR, Fecha , Vencimiento, id_cliente, id_programa) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (id_cliente, Haber, Plan, Profesor, actual, actaulMasMes, id_cliente, id_programa))
                # Confirmar la transaccion
                mixconexion.commit()
            except sqlite3.Error as ex:
                mixconexion.rollback()
            finally:
                mixconexion.close()
    #para cuando la cuota este vencida y exista
        if not (datos_cuota == None) and (fecha_actual >= fecha_vencimiento):
            conexion = sqlite3.connect("BaseDatos.db")
            cursor = conexion.cursor()
            Haber = str(int(datos_programa[2])-int(Haber) + int(datos_cuota[1]))
            cursor.execute("UPDATE Cuotas SET Haber = ?, PLAN = ?, PROFESOR = ?, Fecha = ?, Vencimiento = ?, id_programa = ? WHERE id_cliente = ?",
                        (Haber, Plan, Profesor, actual, actaulMasMes, id_programa, id_cliente))
            conexion.commit()
        
    #para cuando la cuota no este vencida y exista
        if not (datos_cuota == None) and (fecha_actual < fecha_vencimiento):
            conexion = sqlite3.connect("BaseDatos.db")
            cursor = conexion.cursor()
            Haber = str(-int(Haber) + int(datos_cuota[1]))
            print("entre")
            cursor.execute("UPDATE Cuotas SET Haber = ?, PLAN = ?, PROFESOR = ?,  id_programa = ? WHERE id_cliente = ?",
                        (Haber, Plan, Profesor, id_programa, id_cliente))
            conexion.commit()
        mensaje = f"Registro de Cobro:\n\nNombre: {datos_cliente[2]}\nApellido: {datos_cliente[1]}\nDocumento: {documento}\nCobro: {cobro}\nProfesor: {Profesor}\nFecha: {actual}"
        messagebox.showinfo("Cobro Registrado", mensaje)
        
        registrarCobro(id_cliente, cobro, Profesor)

""" en esta funcion registrara un cliente nuevo

Args: 
    documento (int): recibe un documento proporcionado por el usuario

return:
    datos_cliente: returna la fila de la tabla de clientes que contenga el documento proporcionado
"""
def obtener_datos_cliente(documento):
    # Consulta SQL para obtener los datos de un cliente por su documento
    conn = sqlite3.connect("BaseDatos.db")
    cursor = conn.cursor()
    consulta = """
    SELECT * FROM Clientes WHERE Documento = ?;
    """
    cursor.execute(consulta, (documento,)) 
    datos_cliente = cursor.fetchone()    
    #id_cliente, apellido, nombre, documento, correo, fecha_nacimiento, telefono = datos_cliente
    consulta = """
    SELECT * FROM Cuotas WHERE id_cliente = ?;
    """
    cursor.execute(consulta, (datos_cliente[0],))
    datos_cliente = datos_cliente + cursor.fetchone()
    conn.close()
    return datos_cliente

def registrarCobro(id, cobro, profesor):
    conn = sqlite3.connect("BaseDatos.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Cobro (fecha, cobro, profesor, id_cliente) VALUES (?, ?, ?, ?)",
                        (actual, cobro, profesor, id))
    conn.commit()
    conn.close()