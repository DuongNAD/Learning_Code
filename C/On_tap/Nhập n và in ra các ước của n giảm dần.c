#include <stdio.h>

int main() {
    int m;
    printf("Nhập số nguyên M: ");
    scanf("%d", &m);

    printf("Các ước của %d theo thứ tự giảm dần: ", m);
    for (int i = m; i >= 1; i--) {
        if (m % i == 0) {
            printf("%d ", i);
        }
    }

    return 0;
}