#include <stdio.h>

int main() {
    int year, month;

    // Nhập năm và tháng
    printf("Nhap nam: ");
    scanf("%d", &year);
    printf("Nhap thang: ");
    scanf("%d", &month);

    int days;

    // Xác định số ngày trong tháng
    if (month == 2) {
        // Tháng 2 có 28 ngày hoặc 29 ngày (nếu là năm nhuận)
        if ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0)) {
            days = 29;
        } else {
            days = 28;
        }
    } else if (month == 4 || month == 6 || month == 9 || month == 11) {
        // Các tháng 4, 6, 9, 11 có 30 ngày
        days = 30;
    } else if (month >= 1 && month <= 12) {
        // Các tháng còn lại có 31 ngày
        days = 31;
    } else {
        printf("Thang khong hop le.\n");
        return 1; // Kết thúc chương trình với mã lỗi
    }

    // In số ngày
    printf("OUTPUT:\n");
    printf("%d\n", days);
    printf("Press any key to continue . . .");
    getchar(); // Dừng màn hình để xem kết quả
    getchar(); // Đọc ký tự thừa từ bộ đệm

    return 0;
}