//Libreria standard de entrada y salida
#include <stdio.h>

//Definición del tamaño del array
#define TAMANIO 5

//Programa principal
int main() {
    //Declaración del array de números enteros
    int numeros[TAMANIO];
    int num_usuario=0;

    //Inicialización del array a cero (opcional)
    for (int i = 0; i < TAMANIO; i++) {
        numeros[i] = 0;
    }
    //Bucle para pedir al usuario que introduzca los números
    for (int i = 0; i < TAMANIO; i++) {
        printf("Introduce el número %d: ", i + 1);
        //scanf("%d", &numeros[i]);
        scanf("%d", &num_usuario);
        numeros[i] = num_usuario;
    }
    //Impresión de los números introducidos
    printf("Los números introducidos son:\n");
    for (int i = 0; i < TAMANIO; i++) {
        printf("%d ", numeros[i]);
    }
    printf("\n");
    return 0;
}