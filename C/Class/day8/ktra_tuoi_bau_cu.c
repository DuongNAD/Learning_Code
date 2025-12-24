#include <stdio.h>

int main() {
    int age;
    printf("Enter your age: ");
    scanf("%d", &age);

    printf("\nOUTPUT:\n");
    if (age >= 18) {
        printf("Eligible to vote\n");
    } else {
        printf("Not eligible to vote\n");
    }

    return 0;
}