import pandas as pd
from empleado import Empleado

# Cargar datos desde CSV
df = pd.read_csv('empleados.csv')

# Crear lista de objetos Empleado
empleados = []
for _, fila in df.iterrows():
    empleado = Empleado(
        id=int(fila['id']),
        nombre=fila['nombre'],
        apellidos=fila['apellidos'],
        edad=int(fila['edad']),
        correo=fila['correo'],
        departamento=fila['departamento']
    )
    empleados.append(empleado)

# Mostrar los datos cargados
for emp in empleados:
    print(emp)