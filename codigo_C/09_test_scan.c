/*EJEMPLO SOBRE SCANF*/
#include <stdio.h>

/*Programa que lee varios tipos de datos usando scanf*/
int main()
{
    int entero;
    float flotante;
    char caracter;
    char cadena[50];

    // Solicitar y leer datos del usuario
    printf("Introduzca un numero entero: ");
    scanf("%d", &entero);

    printf("Introduzca un numero flotante: ");
    scanf("%f", &flotante);

    printf("Ingrese un caracter: ");
    scanf(" %c", &caracter);  // Espacio antes de %c para consumir cualquier espacio en blanco

    printf("Ingrese una cadena de texto: ");
    scanf("%s", cadena);  // No se necesita el & para cadenas

    printf("-----------------------------\n");
    printf("\nLos datos introducidos son:\n");
    printf("Entero: %d\n", entero);
    printf("Flotante: %.2f\n", flotante);
    printf("Caracter: %c\n", caracter);
    printf("Cadena: %s\n", cadena);

    return 0;
}