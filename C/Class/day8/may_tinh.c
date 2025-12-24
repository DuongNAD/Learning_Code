#include <stdio.h>

int main() {
    float num1, num2, result;
    char op;
    printf("Enter an expression (e.g., 5 + 3): ");
    scanf("%f %c %f", &num1, &op, &num2);

    printf("\nOUTPUT:\n");
    switch (op) {
        case '+':
            result = num1 + num2;
            printf("Result: %.2f\n", result);
            break;
        case '-':
            result = num1 - num2;
            printf("Result: %.2f\n", result);
            break;
        case '*':
            result = num1 * num2;
            printf("Result: %.2f\n", result);
            break;
        case '/':
            if (num2 != 0) {
                result = num1 / num2;
                printf("Result: %.2f\n", result);
            } else {
                printf("Error: Division by zero.\n");
            }
            break;
        default:
            printf("Error: Invalid operator.\n");
    }

    return 0;
}