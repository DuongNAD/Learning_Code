#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main() {
    char s[101];
    char temp[101];
    int j = 0;

    printf("Nhap chuoi S (toi da 100 ky tu):\n");
    fgets(s, sizeof(s), stdin);
    s[strcspn(s, "\n")] = 0;

    // Loại bỏ ký tự không phải chữ cái hoặc chữ số và chuyển sang chữ thường
    for (int i = 0; i < strlen(s); i++) {
        if (isalnum(s[i])) {
            temp[j++] = tolower(s[i]);
        }
    }
    temp[j] = '\0'; // Kết thúc chuỗi temp

    // Kiểm tra palindrome
    int isPalindrome = 1;
    for (int i = 0; i < strlen(temp) / 2; i++) {
        if (temp[i] != temp[strlen(temp) - i - 1]) {
            isPalindrome = 0;
            break;
        }
    }

    printf("OUTPUT:\n");
    if (isPalindrome) {
        printf("Chuoi la palindrome\n");
    } else {
        printf("Chuoi khong la palindrome\n");
    }

    printf("Press any key to continue . . .\n");
    getchar();
    getchar();

    return 0;
}