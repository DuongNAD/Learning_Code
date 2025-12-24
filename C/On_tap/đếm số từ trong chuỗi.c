#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main() {
    char s[101];
    int count = 0;
    int inWord = 0; // Biến cờ để kiểm tra xem có đang ở trong một từ hay không

    printf("Nhap chuoi S (toi da 100 ky tu):\n");
    fgets(s, sizeof(s), stdin);
    s[strcspn(s, "\n")] = 0;

    for (int i = 0; i < strlen(s); i++) {
        if (isalnum(s[i])) { // Nếu ký tự là chữ cái hoặc chữ số
            if (!inWord) { // Nếu chưa ở trong một từ
                count++;  // Tăng số lượng từ
                inWord = 1; // Đặt cờ là đang ở trong một từ
            }
        } else {
            inWord = 0; // Đặt cờ là không ở trong một từ
        }
    }

    printf("OUTPUT:\n");
    printf("%d\n", count);

    printf("Press any key to continue . . .\n");
    getchar();
    getchar();

    return 0;
}