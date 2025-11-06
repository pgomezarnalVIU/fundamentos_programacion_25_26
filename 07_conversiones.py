# Conversiones de numeros
a = 1
b = 12.3
ponderacion = 2
edad = "32"
peso="50.6"
separador = "-"

# Conversion implicita
num_convertido = a + b
print (num_convertido)

print(separador*10)

# Error
# print(edad+ponderacion)

# Conversion explicita
edad_doblada = ponderacion * int(edad)
print(edad_doblada)
print(type(edad_doblada))
print(ponderacion * int(edad))

# Conversiones explicitas
#print(int(peso))
print(int(float(peso)))
print(int(float(edad)))