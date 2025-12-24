#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main() {
    char str[100];

    printf("Nhap chuoi: ");
    fgets(str, sizeof(str), stdin);
    str[strcspn(str, "\n")] = 0;

    for (int i = 0; str[i] != '\0'; i++) {
        if ((i + 1) % 3 == 0) { // Vị trí chia hết cho 3 (bắt đầu từ 1)
            str[i] = toupper(str[i]);
        }
    }

    printf("Chuoi sau khi xu ly: %s\n", str);

    return 0;
}