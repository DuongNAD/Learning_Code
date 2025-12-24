#include <stdio.h>
#include <string.h>
#include <ctype.h>

int countOccurrences(char *products, char *search) {
    int count = 0;
    char *token = strtok(products, ", "); // Tách chuỗi thành các từ
    while (token != NULL) {
        // So sánh không phân biệt chữ hoa/thường
        if (strcasecmp(token, search) == 0) {
            count++;
        }
        token = strtok(NULL, ", ");
    }
    return count;
}

int main() {
    char products[] = "Apple, Orange, Banana, apple, apple, Orange";
    char search[] = "APPLE";
    printf("OUTPUT:\n");
    printf("%d\n", countOccurrences(products, search));
    printf("Press any key to continue . . .");
    getchar(); // Dừng màn hình để xem kết quả
    return 0;
}