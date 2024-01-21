import tkinter as tk
import webview
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
class CustomApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # create tabview
        self.tabview = customtkinter.CTkTabview(self, width=250)
        self.tabview.grid(row=1, column=3, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.tabview.add("opciones")
        self.tabview.add("WhatsApp")
        self.tabview.add("Configuracion")
        self.tabview.tab("opciones").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.tabview.tab("WhatsApp").grid_columnconfigure(0, weight=1)

        # Botón para abrir el navegador en el tab "WhatsApp"
        abrir_navegador_button = tk.Button(self.tabview.tab("WhatsApp"), text="Abrir Navegador", command=self.abrir_navegador_en_frame)
        abrir_navegador_button.pack(pady=20)

    def abrir_navegador_en_frame(self):
        # Configurar el navegador web
        webview.create_window("Navegador en Tkinter", url="https://web.whatsapp.com/", width=800, height=600)

        # Iniciar el bucle del navegador
        webview.start()

if __name__ == "__main__":
    app = CustomApp()
    app.mainloop()
