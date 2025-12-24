#include <stdio.h>
#include <string.h>

int main() {
    char str[1000];
    int counts[256] = {0}; // Mảng để lưu số lần xuất hiện của từng ký tự (ASCII)
    int maxCount1 = 0, maxCount2 = 0;
    char maxChar1 = '\0', maxChar2 = '\0';

    printf("Nhap chuoi: ");
    fgets(str, sizeof(str), stdin);
    // Loại bỏ ký tự newline nếu có
    if (str[strlen(str) - 1] == '\n') {
        str[strlen(str) - 1] = '\0';
    }

    // Đếm số lần xuất hiện của từng ký tự
    for (int i = 0; str[i] != '\0'; i++) {
        counts[(unsigned char)str[i]]++; // Ép kiểu sang unsigned char để xử lý ký tự mở rộng
    }

    // Tìm 2 ký tự xuất hiện nhiều nhất
    for (int i = 0; i < 256; i++) {
        if (counts[i] > maxCount1) {
            maxCount2 = maxCount1;
            maxChar2 = maxChar1;
            maxCount1 = counts[i];
            maxChar1 = (char)i;
        } else if (counts[i] > maxCount2 && counts[i] <= maxCount1) {
            maxCount2 = counts[i];
            maxChar2 = (char)i;
        }
    }

    printf("2 ky tu xuat hien nhieu nhat:\n");
    if (maxChar1 != '\0') {
        printf("'%c': %d lan\n", maxChar1, maxCount1);
    }
    if (maxChar2 != '\0') {
        printf("'%c': %d lan\n", maxChar2, maxCount2);
    }

    return 0;
}