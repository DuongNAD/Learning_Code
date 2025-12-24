// Bài 5: Tìm phần tử lớn nhất trong mảng (10 điểm)
// Viết chương trình nhập vào một mảng số nguyên n phần tử và tìm phần tử lớn nhất.

#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n;
    printf("Nhap so gia tri: ");
    scanf("%d", &n);
    int *c = (int *)malloc(n * sizeof(int));
    for (int i = 0; i < n; i++)
    {
        printf("c[%d] = ", i);
        scanf("%d", &c[i]);
    }
    int Max = c[0];
    for (int i = 1; i < n; i++)
    {
        if (c[i] > Max)
        {
            Max = c[i];
        }
    }
    printf("\n");
    printf("Max = %d", Max);
    free(c);
    return 0;
}