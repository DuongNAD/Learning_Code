#include <stdio.h>
#include <string.h>
#include <limits.h>

int main() {
    char s[101];
    int count[256] = {0}; // Mảng để lưu trữ số lần xuất hiện của từng ký tự (ASCII)
    int maxCount = 0;
    char maxChar;

    printf("Nhap chuoi S (toi da 100 ky tu):\n");
    fgets(s, sizeof(s), stdin);
    s[strcspn(s, "\n")] = 0;

    for (int i = 0; i < strlen(s); i++) {
        count[(unsigned char)s[i]]++; // Tăng số lần xuất hiện của ký tự
    }

    for (int i = 0; i < 256; i++) {
        if (count[i] > maxCount) {
            maxCount = count[i];
            maxChar = (char)i;
        }
    }

    printf("OUTPUT:\n");
    printf("Ky tu '%c' xuat hien nhieu nhat (%d lan)\n", maxChar, maxCount);

    printf("Press any key to continue . . .\n");
    getchar();
    getchar();

    return 0;
}