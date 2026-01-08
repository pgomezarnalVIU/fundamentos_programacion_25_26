import tkinter as tk
from tkinter import ttk

def crear_presentacion(pestanyas):
    # Contenedor con un texto largo de presentacion
    contenedor = ttk.Frame(pestanyas.nametowidget(pestanyas.tabs()[0]))    
    contenedor.pack(fill='both', expand=True, padx=20, pady=20)

    scroll_y = tk.Scrollbar(contenedor, orient='vertical')
    scroll_y.pack(side='right', fill='y')   

    texto_presentacion = tk.Text(contenedor, wrap='word', yscrollcommand=scroll_y.set)
    texto_presentacion.pack(fill='both', expand=True)
    scroll_y.config(command=texto_presentacion.yview)

    texto = ("Bienvenido al Gestor de Empleados.\n\n"
            "Este sistema está diseñado para\n"
            "facilitar la gestión eficiente de los empleados dentro de una organización. "
            "Aquí podrás agregar, modificar y eliminar registros de empleados, así como "
            "asignarlos a departamentos y gestionar su información personal.")
    texto_presentacion.insert('1.0', texto*100)

    # Deshabilitar la edición del texto
    texto_presentacion.config(state='disabled')
