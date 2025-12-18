# Ejemplo sobre clase

# Clase Perro
# Tiene 2 atributos
# - nombre, str
# - raza, str
# Atrubuto de clase
# -especie
class Perro:
    # Añadimos el atributo de clase denominado especie
    especie = "Canis familiaris"

    # El metodo __init__ se llama al crear el objeto
    def __init__(self,nombre,raza):
        print(f"Iniciando la clase Perro {nombre}, {raza}")
        # Atributos de la instancia
        self.nombre = nombre
        self.raza = raza

# Todos los objetos comparten el atributo de clase
Perro.especie = "Canis lupus familiaris"

# Generando de camada
caniche = Perro("Paco","caniche")
pastor_aleman = Perro("Venus","pastor aleman")
salchicha = Perro("Thor","salchicha")
salchicha.especie = "Canis slachichus"


# Imprimir los atributos de los objetos
print(f"El perro {caniche.nombre} es de raza {caniche.raza}")
print(f"El perro {pastor_aleman.nombre} es de raza {pastor_aleman.raza}")
print(f"El perro {salchicha.nombre} es de raza {salchicha.raza}")

# Imprimir la especie
print(f"El perro {caniche.nombre} es de especie {caniche.especie}")
print(f"El perro {pastor_aleman.nombre} es de especie {pastor_aleman.especie}")
print(f"El perro {salchicha.nombre} es de especie {salchicha.especie}")

