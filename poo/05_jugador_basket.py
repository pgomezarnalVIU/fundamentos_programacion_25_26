# Clase Jugador de Baloncesto
# Atributos:
# - nombre
# - equipo
# - puntos_partido (promedio)

class JugadorBaloncesto:
    def __init__(self,nombre,equipo):
        self.nombre = nombre
        self.equipo = equipo
        self.puntos_partido = 0

    def mostrar_info(self):
        print(f"Nombre jugador : {self.nombre}, equipo : {self.equipo} y puntos partido : {self.puntos_partido}")

    def anyadir_puntos(self,nuevo_promedio):
        self.puntos_partido = nuevo_promedio

# Ejemplo de uso
jugador1 = JugadorBaloncesto("Lebron James","Los Angeles Lakers")
jugador1.puntos_partido = 25.3

jugador1.mostrar_info()