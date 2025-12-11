//Libreria estandar de entrada y salida
#include <stdio.h>

//Funcion principal
int main() {
    //Declaracion de un array de caracteres
    char nombre[20];

    //Pedir al usuario que ingrese su nombre
    printf("Ingrese su nombre: ");
    //Leer el nombre ingresado por el usuario
    scanf("%s", nombre);

    //Imprimir el nombre ingresado
    printf("Hola, %s!\n", nombre);

    //Retornar 0 para indicar que el programa finalizo correctamente
    return 0;
}