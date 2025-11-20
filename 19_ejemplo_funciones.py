# Funcion sin parametros
def saludar():
    print("Hola como estas")


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

print("Fin de codigo")
