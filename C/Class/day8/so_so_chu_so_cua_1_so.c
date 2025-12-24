#include <stdio.h>

int main() {
    int num;
    int count = 0;
    printf("Enter an integer: ");
    scanf("%d", &num);

    // Xử lý trường hợp đặc biệt khi đầu vào là 0
    if (num == 0) {
        count = 1;
    } else {
        int temp = num;
        while (temp != 0) {
            temp /= 10;
            count++;
        }
    }

    printf("\nOUTPUT:\n");
    printf("Number of digits: %d\n", count);

    return 0;
}