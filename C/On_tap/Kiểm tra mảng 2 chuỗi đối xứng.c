#include <stdio.h>
#include <string.h>
#include <stdbool.h>

bool isSymmetricStringArrays(char arr1[][100], char arr2[][100], int n) {
    if (n <= 0) {
        return true; // Mảng rỗng được coi là đối xứng
    }

    for (int i = 0; i < n; i++) {
        if (strcmp(arr1[i], arr2[n - i - 1]) != 0) {
            return false;
        }
    }

    return true;
}

int main() {
    char arr1[][100] = {"abc", "def", "ghi"};
    char arr2[][100] = {"ghi", "def", "abc"};
    int n = sizeof(arr1) / sizeof(arr1[0]);

    if (isSymmetricStringArrays(arr1, arr2, n)) {
        printf("Hai mang chuoi doi xung.\n");
    } else {
        printf("Hai mang chuoi khong doi xung.\n");
    }

    return 0;
}