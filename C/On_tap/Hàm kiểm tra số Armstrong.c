#include <stdio.h>

int kiemTraNamNhuan(int nam) {
    if ((nam % 4 == 0 && nam % 100 != 0) || nam % 400 == 0) {
        return 1; // Năm nhuận
    } else {
        return 0; // Không phải năm nhuận
    }
}

int main() {
    int nam;
    printf("Nhap nam: ");
    scanf("%d", &nam);

    if (kiemTraNamNhuan(nam)) {
        printf("%d la nam nhuan.\n", nam);
    } else {
        printf("%d khong phai nam nhuan.\n", nam);
    }

    return 0;
}