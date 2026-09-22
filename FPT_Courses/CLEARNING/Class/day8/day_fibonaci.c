#include <stdio.h>

int main() {
    int N, count = 0;
    long long t1 = 0, t2 = 1, nextTerm;
    printf("Enter N: ");
    scanf("%d", &N);

    printf("\nOUTPUT:\n");
    while (count < N) {
        printf("%lld ", t1);
        nextTerm = t1 + t2;
        t1 = t2;
        t2 = nextTerm;
        count++;
    }
    printf("\n");

    return 0;
}