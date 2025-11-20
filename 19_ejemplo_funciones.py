# Funcion sin parametros
def saludar():
    print("Hola como estas")
def saludar_nombre(nombre="Marta"):
    print(f"Hola {nombre}. Como estas")


# Funcion que realice una suma
def suma(a, b):
    print(a + b)


def suma_return(a, b):
    print(a + b)
    return a + b


# Uso de las funcions
saludar()
suma(3, 2)
resultado = suma_return(4, 20)

# Funciones con param con valor predeterminado
saludar_nombre()
saludar_nombre("Paco")

print("Fin de codigo")
