import curriculum
# Clase que representa una persona con los atributos nombre, email.
# Incluye un método para mostrar la información de la persona.
class Persona:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

    def mostrar_informacion(self):
        return f"Nombre: {self.nombre}, Email: {self.email}"

# Clase que representa a un estudiante, que hereda de Persona.
# Incluye un atributo adicional con un identificadorde de estudiante
# Incluye un atributo con las asignaturas inscritas
# y un método para mostrar la información del estudiante.
# y un método para matricularse en una asignatura.
# y un metodo para calcular el promedio de calificaciones de sus examenes.

class Estudiante(Persona):
    def __init__(self, nombre, email, id_estudiante):
        super().__init__(nombre, email)
        self.id_estudiante = id_estudiante
        self.asignaturas = []

    def mostrar_informacion(self):
        info_persona = super().mostrar_informacion()
        return f"{info_persona}, ID Estudiante: {self.id_estudiante}"
    
    def matricular_asignatura(self, asignatura):
        self.asignaturas.append(asignatura)
    
    def calcular_promedio(self):
        total_calificaciones = 0
        total_examenes = 0
        for asignatura in self.asignaturas:
            for examen in asignatura.examenes:
                total_calificaciones += examen.calificacion
                total_examenes += 1
        if total_examenes == 0:
            return 0
        return total_calificaciones / total_examenes
    
# Clase que representa a un profesor, que hereda de Persona.
# Incluye un atributo adicional con el departamento del profesor
# un atributo adicional con el número de horas trabajadas y un método para mostrar la información del profesor.
class Profesor(Persona):
    def __init__(self, nombre, email, departamento, horas_trabajadas):
        super().__init__(nombre, email)
        self.departamento = departamento
        self.horas_trabajadas = horas_trabajadas
        self.asignaturas = []

    def mostrar_informacion(self):
        info_persona = super().mostrar_informacion()
        return f"{info_persona}, Departamento: {self.departamento}, Horas Trabajadas: {self.horas_trabajadas}"
    
    def nueva_asignatura(self, asignatura):
        self.asignaturas.append(asignatura)