#include <stdio.h>
#include <string.h>
#include <ctype.h>

int demKyTuInHoa(char chuoi[]) {
    int dem = 0;
    for (int i = 0; i < strlen(chuoi); i++) {
        if (isupper(chuoi[i])) {
            dem++;
        }
    }
    return dem;
}

int main() {
    char chuoi[100];

    printf("Nhap chuoi: ");
    fgets(chuoi, sizeof(chuoi), stdin);

    // Loại bỏ ký tự newline nếu có
    if (chuoi[strlen(chuoi) - 1] == '\n') {
        chuoi[strlen(chuoi) - 1] = '\0';
    }

    int soKyTuInHoa = demKyTuInHoa(chuoi);
    printf("So ky tu in hoa trong chuoi la: %d\n", soKyTuInHoa);

    return 0;
}