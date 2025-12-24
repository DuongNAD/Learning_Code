#include <stdio.h>
#include <string.h>

int findFrequency(char str[], char ch) {
    int count = 0;
    int length = strlen(str);

    for (int i = 0; i < length; i++) {
        if (str[i] == ch) {
            count++;
        }
    }

    return count;
}

int main() {
    char str[101]; // Chuỗi có tối đa 100 ký tự + ký tự null kết thúc chuỗi
    char ch;

    // Nhập chuỗi
    printf("INPUT:\n");
    printf("Enter a string: ");
    fgets(str, sizeof(str), stdin); // Dùng fgets để đọc cả dấu cách

    // Xóa ký tự newline cuối chuỗi (nếu có)
    int len = strlen(str);
    if (len > 0 && str[len - 1] == '\n') {
        str[len - 1] = '\0';
    }

    // Nhập ký tự
    printf("Enter the character: ");
    scanf("%c", &ch);

    // Tìm tần suất
    int frequency = findFrequency(str, ch);

    // In kết quả
    printf("OUTPUT:\n");
    printf("The frequency of '%c' in the string is: %d\n", ch, frequency);

    return 0;
}