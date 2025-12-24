#include <stdio.h>
#include <ctype.h>
#include <string.h>

void vietHoaNuaChuoi(char str[]) {
    int doDai = strlen(str);
    for (int i = 0; i < doDai / 2; i++) {
        str[i] = toupper(str[i]);
    }
}

int main() {
    char str[] = "hello world";

    vietHoaNuaChuoi(str);

    printf("Chuoi sau khi viet hoa nua dau: %s\n", str);

    return 0;
}