#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main() {
    char products[1000]; // Mảng để lưu trữ danh sách sản phẩm
    char search[100];    // Mảng để lưu trữ tên sản phẩm cần tìm kiếm
    char *token;
    int count = 0;

    printf("Products: ");
    fgets(products, sizeof(products), stdin);
    products[strcspn(products, "\n")] = 0; // Loại bỏ ký tự '\n'

    printf("Search: ");
    fgets(search, sizeof(search), stdin);
    search[strcspn(search, "\n")] = 0; // Loại bỏ ký tự '\n'

    // Chuyển search sang chữ thường để tìm kiếm không phân biệt hoa thường
    for (int i = 0; search[i]; i++) {
        search[i] = tolower(search[i]);
    }

    // Tách chuỗi products thành các sản phẩm riêng lẻ
    token = strtok(products, ",");
    while (token != NULL) {
        // Loại bỏ khoảng trắng thừa ở đầu và cuối sản phẩm
        while (isspace((unsigned char)*token)) token++;
        char *end = token + strlen(token) - 1;
        while (end > token && isspace((unsigned char)*end)) end--;
        *(end + 1) = '\0';

        // Chuyển sản phẩm sang chữ thường để so sánh không phân biệt hoa thường
        char temp[100];
        strcpy(temp, token);
        for (int i = 0; temp[i]; i++) {
            temp[i] = tolower(temp[i]);
        }

        // So sánh sản phẩm với từ khóa tìm kiếm
        if (strcmp(temp, search) == 0) {
            count++;
        }
        token = strtok(NULL, ",");
    }

    printf("OUTPUT:\n");
    printf("%d\n", count);

    printf("Press any key to continue . . .\n");
    getchar();
    getchar();

    return 0;
}