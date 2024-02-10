import tkinter as tk
import tkinter
import tkinter.messagebox
import customtkinter

class CustomEntry(customtkinter.CTkEntry):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bind("<KeyRelease>", self.actualizar_resultados)
    def actualizar_resultados(self, event):
        # Obtiene la entrada actual del cuadro de texto
        entrada = self.get()
        # Filtra la lista de nombres y apellidos en función de la entrada
        resultados_filtrados = [nombre_apellido for nombre_apellido in lista_nombres_apellidos if entrada in nombre_apellido.lower()]
        # Borra los elementos actuales en la lista de resultados
        lista_resultados.delete(0, tk.END)
        # Agrega los nuevos resultados filtrados a la lista
        for resultado in resultados_filtrados:
            lista_resultados.insert(tk.END, resultado)
        # Muestra u oculta la lista de resultados en función de si hay resultados
        if not resultados_filtrados or self.get() == "":
            lista_resultados.pack_forget()
        else:
            lista_resultados.pack(pady=10)
            # Ajusta la altura de la lista de resultados
            lista_resultados.config(height=len(resultados_filtrados))
# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Búsqueda de Nombres y Apellidos")
# Lista de nombres y apellidos (puedes cargarla desde una base de datos o cualquier otra fuente)
lista_nombres_apellidos = ["Juan Pérez", "María García", "Luis Rodríguez", "Ana Martínez", "Pedro López", "Laura Sánchez"]
# Crear un cuadro de entrada personalizado (CustomEntry)
entry = CustomEntry(ventana, placeholder_text="Input")
entry.pack(pady=10)
# Crear una lista para mostrar los resultados
lista_resultados = tk.Listbox(ventana)
lista_resultados.config(width=20, height=5)  # Configurar el ancho y alto de la lista de resultados
# Iniciar el bucle principal de la aplicación
ventana.mainloop()