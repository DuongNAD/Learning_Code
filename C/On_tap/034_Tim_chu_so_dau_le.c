#include <stdio.h>

int firstDigit(int n) {
    n = (n < 0) ? -n : n;
    while (n >= 10) {
        n /= 10;
    }
    return n;
}

int main() {
    int n, found = 0;
    scanf("%d", &n);
    int arr[n];

    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
        if (firstDigit(arr[i]) % 2 != 0) {
            printf("Phan tu co chu so dau la le: %d", arr[i]);
            found = 1;
            break;
        }
    }

    if (!found)
        printf("Khong co phan tu nao co chu so dau la so le");

    return 0;
}
