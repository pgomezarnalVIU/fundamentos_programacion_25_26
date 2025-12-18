from enum import Enum

# Clase colores del pelo
class ColorPelo(Enum):
    BLANCO = 1
    LEONADO = 2
    NEGRO = 3
    GRIS = 4

# Ejemplo sobre clase

# Clase Perro
# Tiene 2 atributos
# - nombre, str
# - raza, str
#  - pelaje, ColorPelo
# Atrubuto de clase
# -especie
class Perro:
    # Añadimos el atributo de clase denominado especie
    especie = "Canis familiaris"

    # El metodo __init__ se llama al crear el objeto
    def __init__(self,nombre,raza,pelaje):
        print(f"Iniciando la clase Perro {nombre}, {raza}")
        # Atributos de la instancia
        self.nombre = nombre
        self.raza = raza
        self.pelaje = pelaje
        self.num_pasos = 0

    # Metodo ladrar
    def ladrar(self):
        print(f"{self.nombre} dice guau guau")

    # Metodo caminar
    def caminar(self,pasos):
        self.num_pasos += pasos
        print(f"{self.nombre} ha caminado {self.num_pasos} pasos totales")

# Todos los objetos comparten el atributo de clase
Perro.especie = "Canis lupus familiaris"

# Generando de camada
caniche = Perro("Paco","caniche", ColorPelo.LEONADO)
pastor_aleman = Perro("Venus","pastor aleman", ColorPelo.NEGRO)
salchicha = Perro("Thor","salchicha", ColorPelo.GRIS)
salchicha.especie = "Canis slachichus"

# Hacer que los perros ladren
caniche.ladrar()
pastor_aleman.ladrar()
salchicha.ladrar()

# Hacer que camine el pastor aleman
pastor_aleman.caminar(3)
pastor_aleman.caminar(0)
pastor_aleman.caminar(10)
