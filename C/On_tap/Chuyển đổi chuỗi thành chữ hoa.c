#include <stdio.h>
#include <string.h>
#include <ctype.h>

void chuyenChuoiThanhHoa(char str[]) {
    for (int i = 0; str[i] != '\0'; i++) {
        str[i] = toupper(str[i]);
    }
}

int main() {
    char str[100];
    printf("Nhap chuoi: ");
    fgets(str, sizeof(str), stdin);
    chuyenChuoiThanhHoa(str);
    printf("Chuoi sau khi chuyen thanh chu hoa: %s", str);
    return 0;
}