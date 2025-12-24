#include <stdio.h>
#include <string.h> // Thêm thư viện string.h để sử dụng strlen

int main() {
    char s[100];
    char kyTuCanThayThe, kyTuThayThe;
    int viTri;

    printf("Nhập chuỗi: ");
    fgets(s, sizeof(s), stdin);

    // Loại bỏ ký tự newline nếu có
    s[strcspn(s, "\n")] = 0; 

    printf("Nhập vị trí ký tự cần thay thế (bắt đầu từ 0): ");
    scanf("%d", &viTri);

    printf("Nhập ký tự cần thay thế: ");
    scanf(" %c", &kyTuCanThayThe); // Thêm khoảng trắng để bỏ qua ký tự newline trước đó

    printf("Nhập ký tự thay thế: ");
    scanf(" %c", &kyTuThayThe); // Thêm khoảng trắng để bỏ qua ký tự newline trước đó

    // Kiểm tra vị trí hợp lệ
    if (viTri >= 0 && viTri < strlen(s)) {
        if (s[viTri] == kyTuCanThayThe) {
            s[viTri] = kyTuThayThe;
            printf("Chuỗi sau khi thay thế: %s\n", s);
        } else {
            printf("Ký tự tại vị trí %d không phải là '%c'.\n", viTri, kyTuCanThayThe);
        }
    } else {
        printf("Vị trí không hợp lệ.\n");
    }

    return 0;
}