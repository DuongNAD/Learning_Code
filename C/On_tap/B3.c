#include <stdio.h>

void increment(int *a)
{
    int n;
    printf("Nhap gia tri a = ");
    scanf("%d", a);
    printf("Nhap gia tri n muon them: ");
    scanf("%d", &n);
    printf("Gia tri a ban dau: %d\n", *a);

    *a = *a + n;
    printf("Gia tri a sau khi tang them %d: %d", n, *a);
}

int main()
{
    int a;
    increment(&a);
    return 0;
}