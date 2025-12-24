#include <stdio.h>

// Hàm tìm số lớn nhất trong 3 số
int maxOfThree(int a, int b, int c) {
    int max = a;
    if (b > max)
        max = b;
    if (c > max)
        max = c;
    return max;
}

int main() {
    int a, b, c;

    // Nhập 3 số từ bàn phím
    printf("Enter value for a: ");
    scanf("%d", &a);

    printf("Enter value for b: ");
    scanf("%d", &b);

    printf("Enter value for c: ");
    scanf("%d", &c);

    // Gọi hàm và in kết quả
    int result = maxOfThree(a, b, c);
    printf("Output\n%d\n", result);

    return 0;
}
