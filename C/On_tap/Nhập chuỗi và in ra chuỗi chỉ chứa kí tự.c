#include <stdio.h>
#include <string.h>
#include <ctype.h>

void inChuoiKhongDacBietVaSo(char chuoi[]) {
    int doDai = strlen(chuoi);
    char ketQua[doDai + 1]; // +1 cho ký tự null
    int indexKetQua = 0;

    for (int i = 0; i < doDai; i++) {
        if (isalpha(chuoi[i])) {
            ketQua[indexKetQua] = chuoi[i];
            indexKetQua++;
        }
    }

    ketQua[indexKetQua] = '\0'; // Kết thúc chuỗi kết quả

    printf("%s\n", ketQua);
}

int main() {
    char chuoiNhap[1000];

    printf("Nhap chuoi: ");
    fgets(chuoiNhap, sizeof(chuoiNhap), stdin);

    // Loại bỏ ký tự newline từ fgets
    chuoiNhap[strcspn(chuoiNhap, "\n")] = 0;

    inChuoiKhongDacBietVaSo(chuoiNhap);

    return 0;
}