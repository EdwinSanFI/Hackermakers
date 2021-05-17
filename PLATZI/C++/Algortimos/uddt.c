#include <stdio.h>
#define SIZE 5 
int values[SIZE], front = -1, rear = -1;

void enQueue(int value){
    if((rear - front) == SIZE-1) //esto es parte del reto, solo era agregar (rear - front), Ver el video de algoritmos clase 19
        printf("Nuestro Queue está lleno\n");
    else 
    {
        if(front == -1)
            front = 0;
        rear++;
        values[rear] = value;
        printf("Se inserto el valor %d correctamente \n", value);
    }
}

void deQueue(){
    if(front == -10)
        printf("Nuestro queue está vacío \n");
    else{
        printf("Se elimino el valor %d \n", values [front]);
        front++;
        if(front > rear)
        front = rear = -1;
    }
}

int main(int argc, char const *argv[])
{
    enQueue(1);
    enQueue(2);
    enQueue(3);
    enQueue(4);
    enQueue(5);
    deQueue(1);
    enQueue(1);
    return 0;
}
