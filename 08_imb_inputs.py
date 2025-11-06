"""
Programa calculo imc preguntando peso y altura
"""

# Pedir el peso y la altura
print("Introduce tu peso en Kg")
peso = float(input())
#peso_num = float(peso)

altura = float(input("Introduce tu altura en m"))

# Calculo del IMC
# imc = peso / (altura * altura)
imc = peso / (altura ** 2)
print(imc)

# Clasificar el resultado
if imc < 18.5:
    print("Déficit de peso")
#elif imc >= 18.5 and imc < 24.9:
elif 18.5 <= imc < 24.9:
    print("Peso normal")
elif 24.9 <= imc < 29.9:
    print("Sobrepeso")
elif imc >= 29.9:
    print("Obeso")
else:
    print("Error")