//Incluyendo las librerias necesarias
#include <stdio.h>

//Definiendo la función principal
int main(void) {
    int num1, num2, resultado;

    //Solicitando al usuario que ingrese dos numeros enteros
    printf("Introduce el primer numero entero: ");
    scanf("%d", &num1);
    printf("Introduce el segundo numero entero: ");
    scanf("%d", &num2);
    //Llamando a la funcion de comparacion
    resultado = comparar_enteros(num1, num2);

    return 0;
}

// Funcion de comparacion de dos numeros enteros
int comparar_enteros(int a, int b) {
    if (a < b) {
        printf("%d es menor que %d", a, b);
        return -1; // a es menor que b
    } else if (a > b) {
        printf("%d es menor que %d", b, a);
        return 1;  // a es mayor que b
    } else {
        printf("%d es igual a %d", b, a);
        return 0;  // a es igual a b
    }
}

