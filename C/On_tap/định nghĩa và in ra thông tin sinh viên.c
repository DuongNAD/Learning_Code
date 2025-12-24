#include <stdio.h>

struct SinhVien {
    int maSV;
    char ten[50];
    float diemTB;
};

int main() {
    struct SinhVien sv;

    printf("Nhap ma sinh vien: ");
    scanf("%d", &sv.maSV);

    printf("Nhap ten sinh vien: ");
    scanf(" %[^\n]s", sv.ten); // Đọc cả dòng văn bản

    printf("Nhap diem trung binh: ");
    scanf("%f", &sv.diemTB);

    printf("\nThong tin sinh vien:\n");
    printf("Ma SV: %d\n", sv.maSV);
    printf("Ten: %s\n", sv.ten);
    printf("Diem TB: %.2f\n", sv.diemTB);

    return 0;
}