#include <stdio.h>
#include <string.h>

struct SinhVien {
    int maSV;
    char hoTen[50];
    float diemTB;
};

int main() {
    // Mảng struct SinhVien
    struct SinhVien danhSachSV[3];

    // Nhập thông tin sinh viên
    for (int i = 0; i < 3; i++) {
        printf("Nhap thong tin sinh vien thu %d:\n", i + 1);
        printf("Ma SV: ");
        scanf("%d", &danhSachSV[i].maSV);
        printf("Ho ten: ");
        scanf(" %[^\n]s", danhSachSV[i].hoTen); // Đọc cả dòng có dấu cách
        printf("Diem TB: ");
        scanf("%f", &danhSachSV[i].diemTB);
    }

    // Tìm kiếm sinh viên theo mã SV
    int maSVTimKiem;
    printf("Nhap ma SV can tim: ");
    scanf("%d", &maSVTimKiem);

    int timThay = 0;
    for (int i = 0; i < 3; i++) {
        if (danhSachSV[i].maSV == maSVTimKiem) {
            printf("Thong tin sinh vien tim thay:\n");
            printf("Ma SV: %d\n", danhSachSV[i].maSV);
            printf("Ho ten: %s\n", danhSachSV[i].hoTen);
            printf("Diem TB: %.2f\n", danhSachSV[i].diemTB);
            timThay = 1;
            break;
        }
    }

    if (!timThay) {
        printf("Khong tim thay sinh vien co ma SV %d\n", maSVTimKiem);
    }

    return 0;
}