//Libreria stdio.h
#include <stdio.h>

//Prototipo de la funcion
float precio_mas_alto(float precios[], int n);

//Principal
int main() {
    //Variable array de precios
    float precios[100];

    //Bucle para generar precios aleatorios
    //entre 5 y 500
    for (int i = 0; i < 100; i++) {
        precios[i] = (float)(rand() % 501);
    }

    //Llamada a la funcion
    float max = precio_mas_alto(precios, 100);
    printf("El precio mas alto es: %.2f\n", max);

    //Aplicar el 10% de descuento
    float descuento = max * 0.10;
    float precio_final = max - descuento;
    printf("El precio final con descuento es: %.2f\n", precio_final);

}

//Funcion para encontrar el precio mas alto de un array
float precio_mas_alto(float precios[], int n) {
    float max = precios[0];
    for (int i = 1; i < n; i++) {
        if (precios[i] > max) {
            max = precios[i];
        }
    }
    return max;
} 