#include <stdio.h>
#include <string.h>

struct Date {
    int ngay;
    int thang;
    int nam;
};

struct SinhVien {
    char maSV[10];
    char hoTen[50];
    struct Date ngaySinh;
    float diemTB;
};

void nhapSinhVien(struct SinhVien *sv) {
    printf("Nhap ma SV: ");
    scanf("%s", sv->maSV);

    printf("Nhap ho ten: ");
    while (getchar() != '\n'); 
    fgets(sv->hoTen, sizeof(sv->hoTen), stdin);
    sv->hoTen[strcspn(sv->hoTen, "\n")] = 0; 

    printf("Nhap ngay sinh (ngay thang nam): ");
    scanf("%d %d %d", &sv->ngaySinh.ngay, &sv->ngaySinh.thang, &sv->ngaySinh.nam);

    printf("Nhap diem TB: ");
    scanf("%f", &sv->diemTB);
}

void xuatSinhVien(struct SinhVien sv) {
    printf("\n--- Thong tin Sinh Vien ---\n");
    printf("Ma SV: %s\n", sv.maSV);
    printf("Ho ten: %s\n", sv.hoTen);
    printf("Ngay sinh: %02d/%02d/%d\n", sv.ngaySinh.ngay, sv.ngaySinh.thang, sv.ngaySinh.nam);
    printf("Diem TB: %.2f\n", sv.diemTB);
}

int main() {
    struct SinhVien sv1;
    
    nhapSinhVien(&sv1);
    xuatSinhVien(sv1);
    
    return 0;
}