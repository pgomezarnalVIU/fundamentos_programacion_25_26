#include <stdio.h>

// Función principal
int main() {
    // Definicion de una variable entera
    int a=10,b=20;

    // Estructura de control if-else
    if(a > b) {
        printf("a es mayor que b\n");
        printf("Esto se ejecuta si la condicion es verdadera\n");
    } else {
        printf("a no es mayor que b\n");
    }

    //Estructura de control if else if else
    if(a > b) {
        printf("a es mayor que b\n");
    } else if(a == b) {
        printf("a es igual a b\n");
    } else {
        printf("a es menor que b\n");
    }   

    return 0;
}