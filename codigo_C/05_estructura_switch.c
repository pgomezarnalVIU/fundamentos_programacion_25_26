//Libreria standard de entrada y salida
#include <stdio.h>

//Principal
int main(){
    //Definicion de variable
    int a=2;

    //Estructura de control switch
    switch(a){
        case 1: 
            a=a+5; 
            break;
        case 2: 
            a=a+10; 
            break;
        case 3: 
            a--; 
            break;
        default: 
            a++; 
            break;
    }
}