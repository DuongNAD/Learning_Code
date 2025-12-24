#include <stdio.h>

void fibonacci(int n) {
    int first = 0, second = 1, next;
    printf("Day Fibonacci: %d %d ", first, second);
    for (int i = 2; i < n; i++) {
        next = first + second;
        printf("%d ", next);
        first = second;
        second = next;
    }
}

int main() {
    int n;
    printf("Nhap so luong so Fibonacci: ");
    scanf("%d", &n);
    fibonacci(n);
    return 0;
}