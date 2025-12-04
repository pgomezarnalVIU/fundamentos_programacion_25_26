// Libreria estandar de entrada y salida
#include <stdio.h>
// Funcion principal
int main() {
    // Definicion de variables
    int entero = 10;               // Variable entera
    float flotante = 5.5f;        // Variable de punto flotante
    double doble = 9.99;          // Variable de doble precision
    char caracter = 'A';          // Variable de tipo caracter

    // Definir edad sin inicializar
    int edad;
    edad = 25; // Asignar valor a la variable edad

    // Imprimir valores de las variables
    printf("Valor entero: %d\n", entero);
    printf("Valor flotante: %.2f\n", flotante);
    printf("Valor doble: %.2lf\n", doble);
    printf("Valor caracter: %c\n", caracter);

    printf("Edad: %d\n", edad);

    // Retornar 0 para indicar que el programa termino correctamente
    return 0;
}