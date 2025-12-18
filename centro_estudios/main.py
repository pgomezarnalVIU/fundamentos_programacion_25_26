import personas
import curriculum

# Crea una nueva asignatura
asignatura_math = curriculum.Asignatura("Matemáticas", "MATH101")

#Crea contenidos y exámenes
contenido1 = curriculum.Contenido("Álgebra", "Introducción al álgebra", "algebra.pdf")
examen1 = curriculum.Examen("Examen 1", "Primer examen de matemáticas", "examen1.pdf")
contenido2 = curriculum.Contenido("Geometría", "Introducción a la geometría", "geometria.pdf")
examen2 = curriculum.Examen("Examen 2", "Segundo examen de matemáticas", "examen2.pdf")

# Añade contenidos y exámenes a la asignatura
asignatura_math.nuevo_contenido(contenido1)
asignatura_math.nuevo_contenido(contenido2)
asignatura_math.nuevo_examen(examen1)
asignatura_math.nuevo_examen(examen2)

# Crea un estudiante y lo matricula en la asignatura
estudiante1 = personas.Estudiante("Juan Pérez", "juan.perez@example.com", "E001")
estudiante1.matricular_asignatura(asignatura_math)
estudiante1.asignaturas[0].examenes[0].asignar_calificacion(85)
estudiante1.asignaturas[0].examenes[1].asignar_calificacion(90)

# Muestra la información del estudiante
print(estudiante1.mostrar_informacion())

# Calcula y muestra el promedio de calificaciones del estudiante
promedio = estudiante1.calcular_promedio()
print(f"Promedio de calificaciones: {promedio}")

# Crea un profesor y le asigna una nueva asignatura
profesor1 = personas.Profesor("Ana Gómez", "ana.gomez@example.com", "Matematicas", 40)
profesor1.nueva_asignatura(asignatura_math)
# Muestra la información del profesor
print(profesor1.mostrar_informacion())
