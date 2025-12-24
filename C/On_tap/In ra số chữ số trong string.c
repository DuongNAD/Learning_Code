#include <stdio.h>

int demChuSoTrongChuoi(char str[]) {
    int dem = 0;
    for (int i = 0; str[i] != '\0'; i++) {
        if (str[i] >= '0' && str[i] <= '9') {
            dem++;
        }
    }
    return dem;
}

int main() {
    char str[] = "Hello123World456";

    printf("So chu so trong chuoi: %d\n", demChuSoTrongChuoi(str));

    return 0;
}