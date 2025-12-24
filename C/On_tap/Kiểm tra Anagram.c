#include <stdio.h>
#include <string.h>
#include <stdbool.h>

bool isAnagram(char str1[], char str2[]) {
    if (strlen(str1) != strlen(str2)) return false;
    int count[256] = {0};
    for (int i = 0; str1[i] != '\0'; i++) {
        count[str1[i]]++;
    }
    for (int i = 0; str2[i] != '\0'; i++) {
        count[str2[i]]--;
    }
    for (int i = 0; i <