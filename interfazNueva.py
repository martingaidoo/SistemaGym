import tkinter
import tkinter.messagebox
import customtkinter
from logicaBotones import *
from tkinter import PhotoImage
import customtkinter
import customtkinter as ctk
from customtkinter import CTk, CTkFrame, CTkButton, CTkEntry
import PIL.Image
from PIL import ImageTk,Image
from tkinter import *
import tkinter as tk
import pygame
import sqlite3
from tkcalendar import Calendar
from tkinter import ttk
from tkinter import messagebox
import keyboard
from datetime import datetime
from database_utils import *
from informes import *
import os
import sys


customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Gym Master")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=8, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(8, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Interfaz Gigachad V.1", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=lambda:(controlAcceso(self)), text="Control de acceso")
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, command=lambda:(registrarCliente(self)), text = "Registrar Nuevo Cliente")
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, command=lambda:(actualizarClientes(self)), text = "Actualizar Cliente")
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame, command=lambda:(consultarCuotas(self)), text = "Consultar Cuotas")
        self.sidebar_button_4.grid(row=4, column=0, padx=20, pady=10)
        self.sidebar_button_5 = customtkinter.CTkButton(self.sidebar_frame, command=lambda:(pagoCuotas(self)), text = "Pago de Cuota")
        self.sidebar_button_5.grid(row=5, column=0, padx=20, pady=10)
        self.sidebar_button_6 = customtkinter.CTkButton(self.sidebar_frame, command=lambda:(actualizarPrecio(self)), text = "Actualizar Planes")
        self.sidebar_button_6.grid(row=6, column=0, padx=20, pady=10)
        self.sidebar_button_7 = customtkinter.CTkButton(self.sidebar_frame, command=lambda:(generar_completo()), text = "Generar Exel Clientes")
        self.sidebar_button_7.grid(row=7, column=0, padx=20, pady=10)
        #simplemente se hace invisible este boton para que genere un espacio
        self.sidebar_button_8 = customtkinter.CTkButton(self.sidebar_frame, command=lambda:(self.sidebar_button_event), text="Hace click")
        self.sidebar_button_8.grid(row=8, column=0, padx=20, pady=(5,5))
        self.sidebar_button_8.grid_forget()
        #
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Color fondo", anchor="w")
        self.appearance_mode_label.grid(row=9, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                    command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=10, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="Escala UI:", anchor="w")
        self.scaling_label.grid(row=11, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                            command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=12, column=0, padx=20, pady=(10, 20))

        # create main entry and button
        self.entry = customtkinter.CTkEntry(self, placeholder_text="Input")
        self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.main_button_1 = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        self.main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")


        # create tabview
        self.tabview = customtkinter.CTkTabview(self, width=250)
        self.tabview.grid(row=0, column=3, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.tabview.add("Pestañas")
        self.tabview.add("Pestaña 2")
        self.tabview.add("Pestaña 3")
        self.tabview.tab("Pestañas").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.tabview.tab("Pestaña 2").grid_columnconfigure(0, weight=1)

        self.optionmenu_1 = customtkinter.CTkOptionMenu(self.tabview.tab("Pestañas"), dynamic_resizing=False,
                                                        values=["Opcion 1", "Opcion 2", "Opcion 3"])
        self.optionmenu_1.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.combobox_1 = customtkinter.CTkComboBox(self.tabview.tab("Pestañas"),
                                                    values=["Opcion 1", "Opcion 2", "Opcio n3"])
        self.combobox_1.grid(row=1, column=0, padx=20, pady=(10, 10))
        self.string_input_button = customtkinter.CTkButton(self.tabview.tab("Pestañas"), text="Cuadro de dialogo",
                                                            command=self.open_input_dialog_event)
        self.string_input_button.grid(row=2, column=0, padx=20, pady=(10, 10))
        self.label_tab_2 = customtkinter.CTkLabel(self.tabview.tab("Pestaña 2"), text="Label Pestaña 2")
        self.label_tab_2.grid(row=0, column=0, padx=20, pady=20)

        # create scrollable frame
        self.scrollable_frame = customtkinter.CTkScrollableFrame(self, label_text="Barras")
        self.scrollable_frame.grid(row=1, column=3, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.scrollable_frame.grid_columnconfigure(0, weight=1)
        self.scrollable_frame_switches = []
        for i in range(100):
            switch = customtkinter.CTkSwitch(master=self.scrollable_frame, text=f"Barra {i}")
            switch.grid(row=i, column=0, padx=10, pady=(0, 20))
            self.scrollable_frame_switches.append(switch)

        # set default values
        self.sidebar_button_8.configure(state="disabled", text="Este boton no lo podes clickear")
        self.scrollable_frame_switches[0].select()
        self.scrollable_frame_switches[4].select()
        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")
        self.optionmenu_1.set("Menu")
        self.combobox_1.set("Opciones")

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Escribi algo:", title="Cuadro de dialogo")
        print("El usuario escribio:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)


if __name__ == "__main__":
    app = App()
    app.mainloop()