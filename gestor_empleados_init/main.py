import tkinter as tk
from tkinter import ttk
from presentacion import *

def ventana_principal(root):
    root.title("Gestor de Empleados")
    root.geometry("1280x720")
    root.resizable(False, False)

def crear_pestanyas(root):
    pestanyas = ttk.Notebook(root)
    pestanyas.pack(expand=1, fill='both')

    # Pestaña de Presentación
    p_presentacio = ttk.Frame(pestanyas)
    pestanyas.add(p_presentacio, text='Presentación')


    # Pestaña de Empleados
    p_empleados = ttk.Frame(pestanyas)
    pestanyas.add(p_empleados, text='Empleados')

    # Pestaña de Departamentos
    p_departamentos = ttk.Frame(pestanyas)
    pestanyas.add(p_departamentos, text='Departamentos')

    return pestanyas

def main():
    ventana = tk.Tk()
    # Configuración de la ventana principal
    ventana_principal(ventana)
    # Creación de las pestañas
    pestanyas = crear_pestanyas(ventana)
    # Crear el contenideo de la pestaña de presentación
    crear_presentacion(pestanyas)

    ventana.mainloop()

if __name__ == "__main__":
    main()