# Suma
def suma(a, b):
    return a + b


# Resta
def resta(a, b):
    return a - b


# Multiplicacion
def multiplica(a, b):
    return a * b


# Division
def division(a, b):
    return a / b


# Interfaz
def interfaz():
    # Interfaz de usuario
    print("Seleccionar la operacion")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("----------")
    print("0. Salir")


# Bucle infinito
while True:
    interfaz()

    # Pedir opcion
    opcion = int(input("Introduce opcion [0,1,2,3,4]: "))

    if opcion == 0:
        break
    #elif opcion > 0 and opcion < 5:
    elif 0 < opcion < 5:
        numero1 = int(input("Introduce el primer numero: "))
        numero2 = int(input("Introduce el segundo numero: "))

        # Realizo el cálcuculo
        if opcion == 1:
            print(f"La suma de los dos numeros es {suma(numero1, numero2)}")
        elif opcion == 2:
            print(f"La resta de los dos numeros es {resta(numero1, numero2)}")
        elif opcion == 3:
            print(f"La multiplicacion de los dos numeros es {multiplica(numero1, numero2)}")
        elif opcion == 4:
            print(f"La division de los dos numeros es {division(numero1, numero2)}")
    else:
        print("Opcion no es valida")

# FIN DEL BUCLE
print("Muchas gracias por utilizar mi calculadora")
