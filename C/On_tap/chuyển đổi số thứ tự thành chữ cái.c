#include <stdio.h>

int main() {
    int position;

    printf("Nhap mot so (1-26): ");
    scanf("%d", &position);

    if (position >= 1 && position <= 26) {
        char ch = 'a' + position - 1;
        printf("Chu cai tai vi tri %d la: %c\n", position, ch);
    } else {
        printf("So khong hop le.\n");
    }

    return 0;
}