#include <stdio.h>
#include <string.h>

int main() {
    char s[101];
    char result[101];
    int j = 0;

    printf("Nhap chuoi S (toi da 100 ky tu):\n");
    fgets(s, sizeof(s), stdin);
    s[strcspn(s, "\n")] = 0;

    for (int i = 0; i < strlen(s); i++) {
        int isDuplicate = 0;
        for (int k = 0; k < j; k++) {
            if (s[i] == result[k]) {
                isDuplicate = 1;
                break;
            }
        }
        if (!isDuplicate) {
            result[j++] = s[i];
        }
    }
    result[j] = '\0'; // Kết thúc chuỗi result

    printf("OUTPUT:\n");
    printf("%s\n", result);

    printf("Press any key to continue . . .\n");
    getchar();
    getchar();

    return 0;
}