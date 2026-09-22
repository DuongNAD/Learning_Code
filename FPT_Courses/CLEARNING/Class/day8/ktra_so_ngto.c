#include <stdio.h>
#include <math.h>

int main() {
    int num, isPrime = 1;
    printf("Enter a number: ");
    scanf("%d", &num);

    if (num <= 1) {
        isPrime = 0;
    } else {
        for (int i = 2; i * i <= num; i++) {
            if (num % i == 0) {
                isPrime = 0;
                break;
            }
        }
    }
    
    printf("\nOUTPUT:\n");
    if (isPrime) {
        printf("Prime Number\n");
    } else {
        printf("Not a Prime Number\n");
    }

    return 0;
}