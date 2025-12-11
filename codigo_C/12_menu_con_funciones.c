#include <stdio.h>

//Prototipo de la función
void imprimir_menu();

//Programa principal
int main() {
    //Llamada a la función para imprimir el menú
    imprimir_menu();
}

//Generar una función para imprimir un menú de opciones
void imprimir_menu() {
    int opcion = 0;
    do {
        printf("Menú de opciones:\n");
        printf("1. Opción 1\n");
        printf("2. Opción 2\n");
        printf("3. Opción 3\n");
        printf("4. Salir\n");
        printf("Introduce una opción (1-4): ");
        scanf("%d", &opcion);
        if (opcion < 1 || opcion > 4) {
            printf("Opción no válida. Por favor, introduce un número entre 1 y 4.\n");
        }
    } while (opcion < 1 || opcion > 4);
    printf("Has seleccionado la opción %d.\n", opcion);
}