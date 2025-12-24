#include <stdio.h>
#include <string.h>

int main() {
    char s[100];
    char kyTuThayThe = 'X'; // Ký tự thay thế cố định là 'X'
    char kyTuCanTim;

    printf("Nhập chuỗi: ");
    fgets(s, sizeof(s), stdin);

    // Loại bỏ ký tự newline nếu có
    s[strcspn(s, "\n")] = 0;

    printf("Nhập ký tự cần tìm và thay thế: ");
    scanf(" %c", &kyTuCanTim);

    for (int i = 0; i < strlen(s); i++) {
        if (s[i] == kyTuCanTim) {
            s[i] = kyTuThayThe;
        }
    }

    printf("Chuỗi sau khi thay thế: %s\n", s);

    return 0;
}