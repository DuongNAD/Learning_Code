#include <stdio.h>
#include <string.h>

int main() {
    char chuoi[100];
    int demKyTu[256] = {0}; // Mảng để lưu số lần xuất hiện của từng ký tự
    int soKyTuTrungLap = 0;

    printf("Nhap chuoi: ");
    fgets(chuoi, sizeof(chuoi), stdin);

    // Loại bỏ ký tự newline nếu có
    if (chuoi[strlen(chuoi) - 1] == '\n') {
        chuoi[strlen(chuoi) - 1] = '\0';
    }

    // Đếm số lần xuất hiện của từng ký tự
    for (int i = 0; i < strlen(chuoi); i++) {
        demKyTu[(unsigned char)chuoi[i]]++;
    }

    // Đếm số ký tự trùng lặp
    for (int i = 0; i < 256; i++) {
        if (demKyTu[i] > 1) {
            soKyTuTrungLap += demKyTu[i] - 1; // Mỗi ký tự trùng lặp đóng góp n-1 vào tổng
        }
    }

    printf("So ky tu trung lap trong chuoi la: %d\n", soKyTuTrungLap);

    return 0;
}