#include <stdio.h>

int kiemTraExponent(char str[]) {
    int i = 0, dauCham = 0, e = 0, so = 0;

    // Kiểm tra phần số nguyên
    if (str[i] == '+' || str[i] == '-') {
        i++;
    }
    while (str[i] >= '0' && str[i] <= '9') {
        i++;
        so = 1;
    }
    if (str[i] == '.') {
        dauCham = 1;
        i++;
        while (str[i] >= '0' && str[i] <= '9') {
            i++;
            so = 1;
        }
    }
    if (!so) {
        return 0; // Không có phần số
    }

    // Kiểm tra phần exponent
    if (str[i] == 'e' || str[i] == 'E') {
        e = 1;
        i++;
        if (str[i] == '+' || str[i] == '-') {
            i++;
        }
        so = 0;
        while (str[i] >= '0' && str[i] <= '9') {
            i++;
            so = 1;
        }
        if (!so) {
            return 0; // Không có phần số sau e/E
        }
    }

    return str[i] == '\0'; // Kiểm tra kết thúc chuỗi
}

int main() {
    char str[] = "123.45e+6";

    printf("Chuoi %s %s exponent.\n", str, kiemTraExponent(str) ? "hop le" : "khong hop le");

    return 0;
}