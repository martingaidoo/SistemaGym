import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
import sqlite3
from datetime import datetime
import customtkinter

class TablaDatos(tk.Tk):
    def __init__(self):
        super().__init__()

        # Conexión a la base de datos
        self.conexion = sqlite3.connect("BaseDatos.db")
        self.cursor = self.conexion.cursor()

        # Configuración de la ventana
        self.title("Tabla de Cobros")
        self.geometry("800x600")

        # Configurar el peso de la fila y la columna de la tabla
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(3, weight=1)

        # Calendario para la fecha de inicio
        self.lbl_fecha_inicio = customtkinter.CTkLabel(self, text="Fecha de inicio:")
        self.lbl_fecha_inicio.grid(column=0, row=0, padx=(20,20), pady=(20, 20))

        self.cal_inicio = Calendar(self, date_pattern="yyyy-mm-dd", width=180, height=120)
        self.cal_inicio.grid(column=0, row=1, padx=(20,20), pady=(20, 20))

        # Calendario para la fecha final
        self.lbl_fecha_fin = customtkinter.CTkLabel(self, text="Fecha de fin:", fg_color="transparent")
        self.lbl_fecha_fin.grid(column=1, row=0, padx=(20,20), pady=(20, 20))

        self.cal_fin = Calendar(self, date_pattern="yyyy-mm-dd", width=180, height=120)
        self.cal_fin.grid(column=1, row=1, padx=(20,20), pady=(20, 20))

        # Botón para actualizar la tabla
        self.btn_actualizar = customtkinter.CTkButton(self, text="Actualizar", command=self.actualizar_tabla)
        self.btn_actualizar.grid(column=0, columnspan=2, row=2, padx=(20,20), pady=(20, 20))

        # Crear tabla
        self.tree = ttk.Treeview(self, columns=("Nombre", "Cobro", "Fecha", "Profesor"), show="headings")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Cobro", text="Cobro")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Profesor", text="Profesor")
        self.tree.grid(column=0, columnspan=2, row=3, sticky="nsew")

        # Obtener datos de la base de datos
        self.obtener_datos()

    def obtener_datos(self):
        # Obtener fechas seleccionadas
        print("entreee")
        fecha_inicio = self.cal_inicio.get_date()
        fecha_fin = self.cal_fin.get_date()

        # Ejecutar consulta para obtener datos de la tabla Cobro en el rango de fechas
        self.cursor.execute("SELECT id_cliente, cobro, fecha, profesor  FROM Cobro ORDER BY fecha DESC")

        # Limpiar tabla antes de actualizar
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Recorrer resultados y añadirlos a la tabla en orden inverso
        for row in reversed(self.cursor.fetchall()):
            # Buscar el nombre del cliente usando el id_cliente

            fecha1_datetime = datetime.strptime(fecha_inicio, "%Y-%m-%d")
            fecha2_datetime = datetime.strptime(fecha_fin, "%Y-%m-%d")
            fechaCobro = datetime.strptime(row[2], "%d/%m/%Y")          
            if fecha1_datetime <= fechaCobro >= fecha1_datetime:
                id_cliente = row[0]
                self.cursor.execute("SELECT Nombre, Apellido FROM Clientes WHERE id=?", (id_cliente,))
                nombre_cliente, apellido_cliente = self.cursor.fetchone()
                nombre_completo = nombre_cliente + " " + apellido_cliente
                # Añadir datos a la tabla
                self.tree.insert("", 0, values=(nombre_completo, row[1], row[2], row[3]))

    def actualizar_tabla(self):
        # Obtener y actualizar datos según el rango de fechas seleccionado
        self.obtener_datos()

if __name__ == "__main__":
    app = TablaDatos()
    app.mainloop()
