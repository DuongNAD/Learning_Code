#include <stdio.h>

int main() {
    int n;

    printf("Nhap mot so nguyen duong: ");
    scanf("%d", &n);

    printf("Cac uoc cua %d la: ", n);

    for (int i = 1; i <= n; i++) {
        if (n % i == 0) {
            printf("%d ", i);
        }
    }

    printf("\n");

    printf("Press any key to continue . . .\n");
    getchar();
    getchar();

    return 0;
}