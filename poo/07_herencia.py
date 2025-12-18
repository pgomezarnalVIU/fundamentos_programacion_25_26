# Definimos una clase padre
class Animal:
    def __init__(self):
        print("Creamos un animal")

# Creamos una clase hija que herede de Animal
class Perro(Animal):
    def __init__(self):
        super().__init__()
        print("Creamos un perro")

# Generamos un nuevo perro
husky = Perro()