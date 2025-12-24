#include<stdio.h>

int main () {
    int n, i, j;

    scanf("%d", &n);

    printf("OUTPUT:\n");

    for(i = 0; i < n; i++) {
        char alphabet = 'A' + i; 
        for(j = 0; j <= i; j++) {

            printf("%c ", alphabet);
            alphabet--; 
        }

        printf("\n");
    }
    
    return 0;
}