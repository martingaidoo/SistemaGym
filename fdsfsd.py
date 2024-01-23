import tkinter as tk

def funcion_despues_del_temporizador():
    print("¡El temporizador ha finalizado!")

# Crear la ventana principal
ventana = tk.Tk()

# Establecer la función a ejecutar después de 8 segundos
ventana.after(8000, funcion_despues_del_temporizador)

# Iniciar el bucle principal de Tkinter
ventana.mainloop()
