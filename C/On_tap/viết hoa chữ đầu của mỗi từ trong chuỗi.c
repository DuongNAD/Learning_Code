#include <stdio.h>
#include <string.h>
#include <ctype.h>

void vietHoaChuDau(char chuoi[]) {
    int i = 0;
    // Viết hoa chữ cái đầu tiên (nếu có)
    if (islower(chuoi[0])) {
        chuoi[0] = toupper(chuoi[0]);
    }
    i++;
    // Viết hoa chữ cái đầu của các từ tiếp theo
    while (chuoi[i] != '\0') {
        if (isspace(chuoi[i])) { // Nếu gặp khoảng trắng
            i++;
            if (islower(chuoi[i])) { // Viết hoa chữ cái tiếp theo (nếu có)
                chuoi[i] = toupper(chuoi[i]);
            }
        }
        i++;
    }
}

int main() {
    char chuoi[100];

    printf("Nhap chuoi: ");
    fgets(chuoi, sizeof(chuoi), stdin);

    // Loại bỏ ký tự newline nếu có
    if (chuoi[strlen(chuoi) - 1] == '\n') {
        chuoi[strlen(chuoi) - 1] = '\0';
    }

    vietHoaChuDau(chuoi);
    printf("Chuoi sau khi viet hoa: %s\n", chuoi);

    return 0;
}