#include <stdio.h>
#include <string.h>
#include <stdbool.h>

bool isSymmetricStringArray(char arr[][100], int n) {
    if (n <= 0) {
        return true; // Mảng rỗng được coi là đối xứng
    }

    for (int i = 0; i < n / 2; i++) {
        if (strcmp(arr[i], arr[n - i - 1]) != 0) {
            return false;
        }
    }

    return true;
}

int main() {
    char arr[][100] = {"abc", "def", "abc"};
    int n = sizeof(arr) / sizeof(arr[0]);

    if (isSymmetricStringArray(arr, n)) {
        printf("Mang chuoi doi xung.\n");
    } else {
        printf("Mang chuoi khong doi xung.\n");
    }

    return 0;
}