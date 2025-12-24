#include <stdio.h>
#include <string.h>

int main() {
    struct SinhVien sv1;

    // Gán giá trị cho các phần tử của struct
    strcpy(sv1.hoTen, "Nguyen Van A");
    sv1.tuoi = 20;
    sv1.diemTrungBinh = 8.5;

    // In ra giá trị của các phần tử
    printf("Ho ten: %s\n", sv1.hoTen);
    printf("Tuoi: %d\n", sv1.tuoi);
    printf("Diem trung binh: %.2f\n", sv1.diemTrungBinh);

    return 0;
}