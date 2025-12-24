#include <stdio.h>

int main() {
    int n;
    printf("Nhap so luong so Fibonacci can in: ");
    scanf("%d", &n);

    int a = 0, b = 1;

    printf("Cac so Fibonacci dau tien la:\n");

    for (int i = 0; i < n; i++) {
        printf("%d ", a);
        int next = a + b;
        a = b;
        b = next;
    }

    return 0;
}
