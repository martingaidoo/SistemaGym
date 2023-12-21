import tkinter as tk

def funcion_al_presionar_tecla(event):
    print(f"Tecla presionada: {event.keysym}")

# Crear la ventana
ventana = tk.Tk()

# Asociar la función a la pulsación de la tecla "Enter"
ventana.bind("<Return>", funcion_al_presionar_tecla)

# Iniciar el bucle principal
ventana.mainloop()
