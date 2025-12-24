#include <stdio.h>

void decimalToBinary(int n) {
    int binary[32];
    int i = 0;
    while (n > 0) {
        binary[i] = n % 2;
        n /= 2;
        i++;
    }
    printf("He nhi phan: ");
    for (int j = i - 1; j >= 0; j--) {
        printf("%d", binary[j]);
    }
}

int main() {
    int num;
    printf("Nhap mot so he thap phan: ");
    scanf("%d", &num);
    decimalToBinary(num);
    return 0;
}