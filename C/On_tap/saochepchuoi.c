#include <stdio.h>
#include <string.h>

int main() {
    char source[] = "Đây là chuỗi gốc.";
    char destination[50];

    strcpy(destination, source); // Sao chép source vào destination

    printf("Chuỗi sao chép: %s\n", destination);

    return 0;
}