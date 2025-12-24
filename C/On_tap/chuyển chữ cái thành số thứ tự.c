#include <stdio.h>
#include <ctype.h>

int main() {
    char ch;

    printf("Nhap mot ky tu: ");
    scanf("%c", &ch);

    if (isalpha(ch)) {
        ch = tolower(ch); // Chuyển đổi thành chữ thường để thống nhất
        int position = ch - 'a' + 1;
        printf("Vi tri cua '%c' trong bang chu cai la: %d\n", ch, position);
    } else {
        printf("Ky tu khong phai la chu cai.\n");
    }

    return 0;
}