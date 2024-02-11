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
from tkcalendar import Calendar
from tkinter import messagebox
import customtkinter as ctk

fecha_actual = datetime.now()
actualFechaHora = fecha_actual.strftime("%d/%m/%Y %H:%M:%S")
fecha_con_mes_adicional = fecha_actual + relativedelta(months=1)
# Formatear la fecha como días/mes/año
actual = fecha_actual.strftime("%d/%m/%Y")
actaulMasMes = fecha_con_mes_adicional.strftime("%d/%m/%Y")


def registrarCobro(id, cobro, profesor):
    conn = sqlite3.connect("BaseDatos.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Cobro (fecha, cobro, profesor, id_cliente) VALUES (?, ?, ?, ?)",
                        (actual, cobro, profesor, id))
    conn.commit()
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

    documento, Haber, Plan, Profesor, tipoVencimiento= data
    cobro = Haber

    consulta = """
    SELECT * FROM Clientes WHERE Documento = ?;
    """
    cursor.execute(consulta, (documento,)) 

    datos_cliente = cursor.fetchone()
    id_cliente = datos_cliente[0]
    if int(datos_cliente[7]) == 1:
            
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

        #datos de las fechas de la cuota que existe para verificar si esta vencido
        if not (datos_cuota == None):
            fecha_actual = datetime.strptime(actual, "%d/%m/%Y")
            fecha_vencimiento = datetime.strptime(datos_cuota[5], "%d/%m/%Y")

        # Verificar que ningún dato esté vacío
        if id_cliente and Haber and Plan and Profesor and tipoVencimiento:
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
                print("6")
                conexion = sqlite3.connect("BaseDatos.db")
                cursor = conexion.cursor()
                Haber = str(int(datos_programa[2])-int(Haber) + int(datos_cuota[1]))
                if tipoVencimiento == "Fecha actual":
                    cursor.execute("UPDATE Cuotas SET Haber = ?, PLAN = ?, PROFESOR = ?, Fecha = ?, Vencimiento = ?, id_programa = ? WHERE id_cliente = ?",
                                (Haber, Plan, Profesor, actual, actaulMasMes, id_programa, id_cliente))
                    conexion.commit()
                else:
                    fecha_vencimiento_con_mes_adicional = fecha_vencimiento + relativedelta(months=1)
                    vencimientoMasMes = fecha_vencimiento_con_mes_adicional.strftime("%d/%m/%Y")
                    cursor.execute("UPDATE Cuotas SET Haber = ?, PLAN = ?, PROFESOR = ?, Fecha = ?, Vencimiento = ?, id_programa = ? WHERE id_cliente = ?",
                                (Haber, Plan, Profesor, actual, vencimientoMasMes, id_programa, id_cliente))
                    conexion.commit()
            
        #para cuando la cuota no este vencida y exista
            if not (datos_cuota == None) and (fecha_actual < fecha_vencimiento):
                print("7")
                conexion = sqlite3.connect("BaseDatos.db")
                cursor = conexion.cursor()
                Haber = str(-int(Haber) + int(datos_cuota[1]))
                cursor.execute("UPDATE Cuotas SET Haber = ?, PLAN = ?, PROFESOR = ?,  id_programa = ? WHERE id_cliente = ?",
                            (Haber, Plan, Profesor, id_programa, id_cliente))
                conexion.commit()
            mensaje = f"Registro de Cobro:\n\nNombre: {datos_cliente[2]}\nApellido: {datos_cliente[1]}\nDocumento: {documento}\nCobro: {cobro}\nProfesor: {Profesor}\nFecha: {actual}"
            messagebox.showinfo("Cobro Registrado", mensaje)
            
            registrarCobro(id_cliente, cobro, Profesor)
    else:
        mensaje = f"El cliente no esta habilitado, fue dado de baja"
        messagebox.showinfo("Error", mensaje)




def pagoCuotas(self):
        conexion = sqlite3.connect("BaseDatos.db")
        cursor = conexion.cursor()
        # Consultar la base de datos para obtener la lista
        cursor.execute("SELECT Nombre || ' ' || Apellido || ' ' || Documento AS NombreCompleto FROM Clientes")
        resultados = cursor.fetchall()
        lista_resultante = [tupla[0] for tupla in resultados]
        def mostrar_seleccion3(event):
            selected_indices = lista_resultados_pago.curselection()
            
            if selected_indices:
                selected_item = lista_resultados_pago.get(selected_indices[0])
                entry_cliente.delete(0, tk.END)  # Limpiar el contenido actual
                entry_cliente.insert(0, selected_item[-8:])

        def actualizar_resultados3():
            # Obtiene la entrada actual del cuadro de texto
            entrada = entry_cliente.get()
            # Filtra la lista de nombres y apellidos en función de la entrada
            resultados_filtrados = [nombre_apellido for nombre_apellido in lista_resultante if entrada in nombre_apellido.lower()]
            resultados_filtrados = resultados_filtrados[:4]
            # Borra los elementos actuales en la lista de resultados
            lista_resultados_pago.delete(0, tk.END)
            # Agrega los nuevos resultados filtrados a la lista
            for resultado in resultados_filtrados:
                lista_resultados_pago.insert(tk.END, resultado)
            # Muestra u oculta la lista de resultados en función de si hay resultados
            if not resultados_filtrados or entry_cliente.get() == "":
                lista_resultados_pago.grid_forget()  # Cambiado a grid_forget
            else:
                lista_resultados_pago.grid(row=2, column=2, pady=(0, 0), sticky="nsew")  # Cambiado a grid
                # Ajusta la altura de la lista de resultados
                lista_resultados_pago.config(height=len(resultados_filtrados))
            # Programa la próxima ejecución de la función después de 100 milisegundos
            self.after(100, actualizar_resultados3)

        self.frame_pagoCuota = customtkinter.CTkFrame(self, width=250)
        self.frame_pagoCuota.grid(row=0, rowspan=2, column=1,columnspan=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.frame_pagoCuota.grid_columnconfigure((0,2), weight=1)
        self.frame_pagoCuota.grid_columnconfigure(1, weight=0)
        self.frame_pagoCuota.grid_rowconfigure((0, 1, 2), weight=0)

        global lista_resultados_pago
        lista_resultados_pago = tk.Listbox(self.frame_pagoCuota)
        lista_resultados_pago.config(width=20, height=5)

    #LABEL TITULO
        label_titulo = customtkinter.CTkLabel(self.frame_pagoCuota, text="PAGO DE CUOTA", font=('Century Gothic',20))
        label_titulo.grid(row=0, column=1, padx=(0, 0), pady=(10, 0), sticky="nsew")

        #Entradas
        label_cliente = customtkinter.CTkLabel(self.frame_pagoCuota, text="documento", font=('Century Gothic',15))
        label_cliente.grid(row=1, column=1, padx=(0, 0), pady=(10, 0), sticky="nsew")

        entry_cliente = customtkinter.CTkEntry(self.frame_pagoCuota, width=220, height=25, corner_radius=10)
        entry_cliente.grid(row=2, column=1, padx=(0, 0), pady=(10, 0), sticky="nsew")

        label_programa = customtkinter.CTkLabel(self.frame_pagoCuota, text="Programa", font=('Century Gothic',15))
        label_programa.grid(row=3, column=1, padx=(0, 0), pady=(10, 0), sticky="nsew")

        conexion = sqlite3.connect('BaseDatos.db')
        cursor = conexion.cursor()

        #menu_desplegable = ttk.Combobox(self.frame_pagoCuota, width=35, height=25)

        # Obtener los nombres de los clientes desde la base de datos
        cursor.execute("SELECT Nombre FROM Programa")
        nombres = cursor.fetchall()
        lista_nombres = [tupla[0] for tupla in nombres]

        # Agregar los nombres al menú desplegable
        menu_desplegable = customtkinter.CTkComboBox(self.frame_pagoCuota, values=lista_nombres, variable="")

        # Mostrar el menú desplegable
        menu_desplegable.grid(row=4, column=1, padx=(0, 0), pady=(10, 0), sticky="nsew")

        label_vencimiento = customtkinter.CTkLabel(self.frame_pagoCuota, text="Vencimiento", font=('Century Gothic',15))
        label_vencimiento.grid(row=5, column=1, padx=(0, 0), pady=(10, 0), sticky="nsew")

        # Agregar los nombres al menú desplegable
        lista_vencimiento = ["Fecha actual", "Ultimo vencimiento"]

        menu_vencimiento = customtkinter.CTkComboBox(self.frame_pagoCuota, values=lista_vencimiento, variable="")

        # Mostrar el menú desplegable
        menu_vencimiento.grid(row=6, column=1, padx=(0, 0), pady=(10, 0), sticky="nsew")


        label_pago = customtkinter.CTkLabel(self.frame_pagoCuota, text="Pago $", font=('Century Gothic',15))
        label_pago.grid(row=7, column=1, padx=(0, 0), pady=(10, 0), sticky="nsew")
        entry_pago = customtkinter.CTkEntry(self.frame_pagoCuota, width=120, height=25, corner_radius=10)
        entry_pago.grid(row=8, column=1, padx=(0, 0), pady=(10, 0), sticky="nsew")

        label_profesor = customtkinter.CTkLabel(self.frame_pagoCuota, text="Profesor", font=('Century Gothic',15))
        label_profesor.grid(row=9, column=1, padx=(0, 0), pady=(10, 0), sticky="nsew")
        entry_profesor = customtkinter.CTkEntry(self.frame_pagoCuota, width=220, height=25, corner_radius=10)
        entry_profesor.grid(row=10, column=1, padx=(0, 0), pady=(10, 0), sticky="nsew")

        button_confirmar = customtkinter.CTkButton(
            self.frame_pagoCuota,
            width=220,
            text="Confirmar",
            command=lambda: (registrarPago([entry_cliente.get(), entry_pago.get(), menu_desplegable.get(), entry_profesor.get(), menu_vencimiento.get()]), self.frame_pagos.pack(pady=60),self.frame_pagoCuota.pack_forget()),corner_radius=6)
        button_confirmar.grid(row=11, column=1, padx=(0, 0), pady=(10, 0), sticky="nsew")
        
        actualizar_resultados3()
        lista_resultados_pago.bind("<<ListboxSelect>>", mostrar_seleccion3)