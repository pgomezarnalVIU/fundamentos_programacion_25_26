#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    //Inicializar la semilla para números aleatorios
    srand(time(NULL));
    int temperatura = rand() % 46; // Número aleatorio entre 0 y 45
    printf("Temperatura generada: %d\n", temperatura);

    // Evaluar la temperatura usando switch
    switch (temperatura / 10) {
        case 0:
            printf("Hace mucho frio\n");
            break;
        case 1:
            printf("Hace fresquito\n");
            break;
        case 2:
            printf("No se está mal\n");
            break;
        case 3:
            printf("Comienza a hacer calor\n");
            break;
        default:
            printf("Muero achicharrado\n");
            break;
    }

    return 0;
}