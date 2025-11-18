# Creacion de un nuevo diccionario
registro_sara = {
    "Nombre" : "Sara",
    "Edad" : 27,
    "Id" : 1003546
}
registro_paco = dict (
    [
        ('Nombre', 'Paco'),
        ('Edad', 49),
        ("Id", 1004876)
    ]
)
print(registro_sara)
print(registro_paco)

# Imprimir un valor
print(registro_sara["Nombre"])

# Imprimir los valores de un diccionario
for clave in registro_paco:
    print(registro_paco[clave])

# Imprimir clave valor
for clave,valor in registro_paco.items():
    print(f"{clave} = {valor}")