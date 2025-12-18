# Clase Gato
# Atributos
# - nombre
# - raza
# - edad

class Gato:
    def __init__(self,nombre,raza,edad):
        self.__nombre = nombre
        self.raza = raza
        self.__edad = edad

    # mostrar la información
    def mostrar_info(self):
        return f"Gato: {self.__nombre}, {self.raza}, {self.__edad}"

    # metodo para conocer el nombre
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self,nombre):
        if isinstance(nombre,str):
            self.__nombre = nombre
        else:
            print("El nombre tiene que ser string")
        return self.__nombre

    # metodos para conocer y modificar la edad
    def get_edad(self):
        return self.__edad

    def set_edad(self,edad):
        if edad >0:
            self.__edad = edad
        else:
            print("Edad debe ser mayor que 0")

# --------------> El usuario
# Ejemplo de uso
gato_paco = Gato("Marte","callejero",5)
info_gato_paco = gato_paco.mostrar_info()
gato_paco.set_nombre(5)
gato_paco.set_edad(-20)
print(gato_paco.mostrar_info())

# Ejemplo de cambio nombre
# Visibilidad de el atributo nombre es publica
# gato_paco.nombre = "Leon"