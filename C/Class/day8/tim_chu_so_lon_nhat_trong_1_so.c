#include <stdio.h>
#include <stdlib.h> // For abs()

int main() {
    int num, maxDigit = 0, remainder;
    printf("Enter a number: ");
    scanf("%d", &num);
    
    int temp = abs(num); // Xử lý cho cả số âm
    if (temp == 0) {
        maxDigit = 0;
    }

    while (temp > 0) {
        remainder = temp % 10;
        if (remainder > maxDigit) {
            maxDigit = remainder;
        }
        temp /= 10;
    }

    printf("\nOUTPUT:\n");
    printf("Largest digit: %d\n", maxDigit);

    return 0;
}