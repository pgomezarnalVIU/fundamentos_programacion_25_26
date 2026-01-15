# Definimos la clase empleado
class Empleado:
    def __init__(self, id, nombre, apellidos, edad, correo,departamento):
        self.id = id
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.correo = correo
        self.departamento = departamento

    def __repr__(self):
        return f"Empleado(id={self.id}, nombre={self.nombre}, apellidos={self.apellidos}, edad={self.edad}, correo={self.correo}, departamento={self.departamento})"
