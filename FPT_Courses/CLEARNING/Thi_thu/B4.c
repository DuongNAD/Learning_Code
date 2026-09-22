// Bài 4: Đảo ngược mảng số nguyên (10 điểm)
// Viết chương trình nhập vào một mảng số nguyên gồm n phần tử, sau đó đảo ngược mảng và in ra kết quả.

#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n;
    printf("Nhap so gia tri: ");
    scanf("%d", &n);
    int *c = (int *)malloc(n * sizeof(int));
    if (c == NULL)
    {
        printf("Error");
        return 1;
    }
    printf("Nhap mang:\n");
    for (int i = 0; i < n; i++)
    {
        printf("c[%d] = ", i);
        scanf("%d", &c[i]);
    }
    printf("\n");
    printf("Mang truoc khi dao nguoc:\n");
    for (int i = 0; i < n; i++)
    {
        printf("%d\t", c[i]);
    }
    printf("\n");

    for (int i = 0; i < n/2; i++)
    {
        int temp = c[i];
        c[i] = c[n - i - 1];
        c[n - i - 1] = temp;
    }

    printf("Mang sau khi dao nguoc: \n");
    for (int i = 0; i < n; i++)
    {
        printf("%d\t", c[i]);
    }
    return 0;
}