#include <stdio.h>

int main() {
    int N;
    unsigned long long factorial = 1;
    printf("Enter N: ");
    scanf("%d", &N);
    
    if (N < 0) {
        printf("Factorial of a negative number doesn't exist.\n");
    } else {
        for (int i = 1; i <= N; i++) {
            factorial *= i;
        }
        printf("\nOUTPUT:\n");
        printf("Factorial: %llu\n", factorial);
    }
    
    return 0;
}