#include <stdio.h>

int main() {
    int n;
    printf("Nhap so dong cua kim tu thap: ");
    scanf("%d", &n);

    for (int i = n; i >= 1; i--) {
        for (int j = 0; j < i; j++) {
            printf("%c", 'A' + j);
        }
        printf("\n");
    }

    return 0;
}
