# Ejemplo sobre clase

# Clase Perro
# Tiene 2 atributos
# - nombre, str
# - raza, str
class Perro:
    # El metodo __init__ se llama al crear el objeto
    def __init__(self,nombre,raza):
        print(f"Iniciando la clase Perro {nombre}, {raza}")
        # Atributos de la instancia
        self.nombre = nombre
        self.raza = raza

# Generando de camada
caniche = Perro("Paco","caniche")
pastor_aleman = Perro("Venus","pastor aleman")
salchicha = Perro("Thor","salchicha")

# Imprimir los atributos de los objetos
print(f"El perro {caniche.nombre} es de raza {caniche.raza}")
print(f"El perro {pastor_aleman.nombre} es de raza {pastor_aleman.raza}")
print(f"El perro {salchicha.nombre} es de raza {salchicha.raza}")

# Cambiar el atributo del caniche
caniche.nombre = "Pako"
print(f"El perro {caniche.nombre} es de raza {caniche.raza}")
