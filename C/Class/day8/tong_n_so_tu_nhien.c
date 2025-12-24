#include <stdio.h>

int main() {
    int N, i;
    long long sum = 0; // Sử dụng long long để tránh tràn số với N lớn
    printf("Enter N: ");
    scanf("%d", &N);

    for (i = 1; i <= N; i++) {
        sum += i;
    }

    printf("\nOUTPUT:\n");
    printf("Sum: %lld\n", sum);

    return 0;
}