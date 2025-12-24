#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main() {
    char names[100][50]; // Mảng 2 chiều để lưu tên (tối đa 100 tên, mỗi tên tối đa 50 ký tự)
    int n;
    char searchChar;

    printf("Nhap so luong ten: ");
    scanf("%d", &n);
    getchar(); // Đọc ký tự newline còn sót lại từ scanf

    printf("Nhap cac ten:\n");
    for (int i = 0; i < n; i++) {
        fgets(names[i], sizeof(names[i]), stdin);
        // Loại bỏ ký tự newline nếu có
        if (names[i][strlen(names[i]) - 1] == '\n') {
            names[i][strlen(names[i]) - 1] = '\0';
        }
    }

    printf("Nhap ky tu can tim: ");
    scanf(" %c", &searchChar); // Dấu cách trước %c để bỏ qua ký tự whitespace

    printf("Cac ten chua ky tu '%c':\n", searchChar);
    for (int i = 0; i < n; i++) {
        for (int j = 0; names[i][j] != '\0'; j++) {
            if (tolower(names[i][j]) == tolower(searchChar)) { // So sánh không phân biệt hoa thường
                printf("%s\n", names[i]);
                break; // Tìm thấy ký tự, không cần kiểm tra tiếp trong tên này
            }
        }
    }

    return 0;
}