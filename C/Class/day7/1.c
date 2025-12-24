#include <stdio.h>

int main() {

    int number1 = 10;
    int number2 = 20;

    int *ptr1;
    int *ptr2;

    ptr1 = &number1;
    ptr2 = &number2;

    if (ptr1 == ptr2) {
        printf("Equal");
    } else {
        printf("Not Equal");
    }

    return 0;
}