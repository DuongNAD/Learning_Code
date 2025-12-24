#include <stdio.h>
#include <string.h>

int main() {
    char chuoiNhap[1000];
    char kyTu1, kyTu2;
    int dem1 = 0, dem2 = 0;

    printf("Nhap chuoi: ");
    fgets(chuoiNhap, sizeof(chuoiNhap), stdin);
    chuoiNhap[strcspn(chuoiNhap, "\n")] = 0; // Loại bỏ ký tự newline

    printf("Nhap ky tu thu nhat: ");
    scanf("%c", &kyTu1);
    getchar(); // Đọc ký tự newline còn lại

    printf("Nhap ky tu thu hai: ");
    scanf("%c", &kyTu2);

    int doDai = strlen(chuoiNhap);
    for (int i = 0; i < doDai; i++) {
        if (chuoiNhap[i] == kyTu1) {
            dem1++;
        }
        if (chuoiNhap[i] == kyTu2) {
            dem2++;
        }
    }

    printf("Ky tu '%c' xuat hien %d lan.\n", kyTu1, dem1);
    printf("Ky tu '%c' xuat hien %d lan.\n", kyTu2, dem2);

    return 0;
}