#include <stdio.h>
#include <ctype.h>

int kiemTraTenHopLe(char ten[]) {
    if (!isalpha(ten[0])) {
        return 0; // Tên phải bắt đầu bằng chữ cái
    }
    for (int i = 1; ten[i] != '\0'; i++) {
        if (!isalpha(ten[i]) && ten[i] != ' ') {
            return 0; // Tên chỉ chứa chữ cái và khoảng trắng
        }
    }
    return 1;
}

int main() {
    char ten[] = "Nguyen Van A";

    printf("Ten hop le: %d\n", kiemTraTenHopLe(ten));

    return 0;
}