class Animal:
    def __init__(self,especie, edad):
        self.especie = especie
        self.edad = edad

        #Atributo marca
        self.__marca_padre = "X"

    # Metodo hablar
    def hablar(self):
        print("No se como hablo")

    def moverse(self):
        pass

    def cambio_marca(self):
        self.__marca_padre = ""

    def mostrar_info(self):
        print(self.especie,self.edad,self.__marca_padre)

# Clase Perro
class Perro(Animal):
    def __init__(self,especie,edad):
        super().__init__(especie,edad)
        super().cambio_marca()

    def hablar(self):
        print("Guau!")

    def vigilar(self):
        print("Vigila la casa")

    def moverse(self):
        print("Caminando con 4 patas")


#Clase Abeja que hereda de Animal
class Abeja(Animal):
    def hablar(self):
        print("Bzzzz!")
    def moverse(self):
        print("Volando")

    # Nuevo método
    def picar(self):
        print("Picar!")

# Uso de animal
animal = Animal("mamifero",5)
# No existe el metodo vigilar
animal.mostrar_info()

perro = Perro("mamifero" ,2 )
perro.moverse()
perro.vigilar()
perro.mostrar_info()

