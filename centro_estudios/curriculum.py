# Clase Contenido que representa un contenido del currículo con título,descripción y archivo.
# Incluye un método para mostrar la información del contenido.
# Incluye un método para añadir un nuevo archivo al contenido.
class Contenido:
    def __init__(self, titulo, descripcion, archivo):
        self.titulo = titulo
        self.descripcion = descripcion
        self.archivo = archivo

    def mostrar_informacion(self):
        return f"Título: {self.titulo}, Descripción: {self.descripcion}, Archivo: {self.archivo}"

    def anyadir_archivo(self, nuevo_archivo):
        self.archivo = nuevo_archivo

# Clase Examen que representa un examen con título, descripción, archivo y calificación.
# Incluye un método para mostrar la información del examen.
class Examen:
    def __init__(self, titulo, descripcion, archivo):
        self.titulo = titulo
        self.descripcion = descripcion
        self.archivo = archivo
        self.calificacion = 0

    def mostrar_informacion(self):
        return f"Título: {self.titulo}, Descripción: {self.descripcion}, Archivo: {self.archivo}, Calificación: {self.calificacion}"
    
    def anyadir_archivo(self, nuevo_archivo):
        self.archivo = nuevo_archivo

    def asignar_calificacion(self, calificacion):
        self.calificacion = calificacion

# Clase Asignatura que representa una asignatura con nombre, código, contenidos y exámenes.
# Incluye métodos para añadir contenidos y exámenes, y para mostrar la información de la asignatura.
class Asignatura:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo
        self.contenidos = []
        self.examenes = []

    def nuevo_contenido(self, contenido):
        self.contenidos.append(contenido)

    def nuevo_examen(self, examen):
        self.examenes.append(examen)

    def mostrar_informacion(self):
        info = f"Asignatura: {self.nombre}, Código: {self.codigo}\n"
        info += "Contenidos:\n"
        for contenido in self.contenidos:
            info += f"  - {contenido.mostrar_informacion()}\n"
        info += "Exámenes:\n"
        for examen in self.examenes:
            info += f"  - {examen.mostrar_informacion()}\n"
        return info