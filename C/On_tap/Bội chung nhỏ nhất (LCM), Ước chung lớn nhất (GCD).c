#include <stdio.h>

int timUCLN(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

int timBCNN(int a, int b) {
    return (a * b) / timUCLN(a, b);
}

int main() {
    int a, b;
    printf("Nhap hai so nguyen: ");
    scanf("%d %d", &a, &b);

    printf("UCLN cua %d va %d la: %d\n", a, b, timUCLN(a, b));
    printf("BCNN cua %d va %d la: %d\n", a, b, timBCNN(a, b));

    return 0;
}