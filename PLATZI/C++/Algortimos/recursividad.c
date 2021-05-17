#include <stdio.h>

long result;
int n;

long factorial(int n){
    if(n == 0){
        return 1;
    }
    else{ 
        return (n* factorial(n-1));
    }

}

int main(int argc, char const *argv[])
{
    printf("ingrese el numero a calcular\n");
    scanf("%d", &n);
    if(n < 0)
    {
    printf("vamo a calmarno\n");
    }
    else
    {
        result = factorial(n);
        printf("%d! = %ld \n", n, result);
    }
    
    return 0;
}
