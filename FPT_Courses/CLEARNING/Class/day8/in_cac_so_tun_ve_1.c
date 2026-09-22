#include <stdio.h>

int main() {
    int N;
    printf("Enter N: ");
    scanf("%d", &N);
    
    int i = N;
    printf("\nOUTPUT:\n");
    while (i >= 1) {
        printf("%d ", i);
        i--;
    }
    printf("\n");

    return 0;
}