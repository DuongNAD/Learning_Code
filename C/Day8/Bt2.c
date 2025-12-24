#include <stdio.h>
#include <stdlib.h>

void nhapmang(int arr[], int *n)
{
    for (int i = 0; i < *n; i++)
    {
        printf("arr[%d] = ", i);
        scanf("%d", &arr[i]);
    }
}

void inmang(int arr[], int *n)
{
    for (int i = 0; i < *n; i++)
    {
        printf("arr[%d] = %d\n", i, arr[i]);
    }
}

void kiemtra(int arr[], int n, int *min, int *max)
{
    *min = arr[0];
    *max = arr[0];

    for (int i = 0; i < n; i++)
    {
        if (arr[i] < *min)
        {
            *min = arr[i];
        }
        if (arr[i] > *max)
        {
            *max = arr[i];
        }
    }
    printf("Min = %d\n", *min);
    printf("Max = %d\n", *max);
}

int main()
{
    int n, *q;
    int max, min;
    printf("Nhap kich thuoc mang ");
    scanf("%d", &n);
    q = (int *)malloc(n * sizeof(int));
    nhapmang(q, &n);
    printf("Ham da nhap la \n");
    inmang(q, &n);
    kiemtra(q, n, &max, &min);
    free(q);
    return 0;
}