#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdbool.h>

bool kiemTraChuoiDoiXung(char str[]) {
    int len = strlen(str);
    int i = 0, j = len - 1;

    while (i < j) {
        // Bỏ qua các ký tự không phải chữ cái và chữ số từ đầu chuỗi
        while (i < len && !isalnum(str[i])) {
            i++;
        }

        // Bỏ qua các ký tự không phải chữ cái và chữ số từ cuối chuỗi
        while (j >= 0 && !isalnum(str[j])) {
            j--;
        }

        // Nếu đã duyệt hết chuỗi
        if (i >= j) {
            break;
        }

        // So sánh các ký tự (không phân biệt chữ hoa/thường)
        if (tolower(str[i]) != tolower(str[j])) {
            return false;
        }

        i++;
        j--;
    }

    return true;
}

int main() {
    char str[100];
    printf("Nhap chuoi: ");
    fgets(str, sizeof(str), stdin);

    // Loại bỏ ký tự newline từ fgets
    str[strcspn(str, "\n")] = 0;

    if (kiemTraChuoiDoiXung(str)) {
        printf("Chuoi \"%s\" la chuoi doi xung.\n", str);
    } else {
        printf("Chuoi \"%s\" khong la chuoi doi xung.\n", str);
    }

    return 0;
}