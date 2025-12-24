#include <stdio.h>

int main() {
    int value;
    
    scanf("%d", &value);

    int *ptr = &value;

    int **doublePtr = &ptr;

    **doublePtr *= 2; 

    printf("%d\n", value);

    return 0;
}