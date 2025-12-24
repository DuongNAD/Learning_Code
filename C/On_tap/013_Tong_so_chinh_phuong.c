#include <stdio.h>
#include <math.h>

int isPerfectSquare(int n) {
    int root = sqrt(n);
    return root * root == n;
}

int main() {
    int n, sum = 0;
    scanf("%d", &n);
    int arr[n];

    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
        if (isPerfectSquare(arr[i])) sum += arr[i];
    }

    printf("Tong cac so chinh phuong: %d", sum);
    return 0;
}
