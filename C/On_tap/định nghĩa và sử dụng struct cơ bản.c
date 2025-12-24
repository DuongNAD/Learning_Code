#include <stdio.h>
#include <string.h>

// Định nghĩa struct SinhVien
struct SinhVien {
    int maSV;
    char hoTen[50];
    float diemTB;
};

int main() {
    // Khai báo biến kiểu struct SinhVien
    struct SinhVien sv1;

    // Gán giá trị cho các thành viên của struct
    sv1.maSV = 101;
    strcpy(sv1.hoTen, "Nguyen Van A");
    sv1.diemTB = 8.5;

    // In thông tin sinh viên
    printf("Ma SV: %d\n", sv1.maSV);
    printf("Ho ten: %s\n", sv1.hoTen);
    printf("Diem TB: %.2f\n", sv1.diemTB);

    return 0;
}