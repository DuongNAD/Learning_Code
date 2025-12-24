#include <stdio.h>

// Hàm kiểm tra số nguyên tố
int isPrime(int num) {
    if (num <= 1) return 0;
    for (int i = 2; i * i <= num; i++) {
        if (num % i == 0) return 0;
    }
    return 1;
}

int main() {
    int n;
    scanf("%d", &n); // Nhập số phần tử mảng
    int arr[n];

    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]); // Nhập từng phần tử
    }

    int hasPrime = 0;
    for (int i = 0; i < n; i++) {
        if (isPrime(arr[i])) {
            printf("%d ", arr[i] * arr[i]); // In bình phương nếu là số nguyên tố
            hasPrime = 1;
        }
    }

    if (!hasPrime) printf("No primes"); // Không có số nguyên tố nào
    return 0;
}
