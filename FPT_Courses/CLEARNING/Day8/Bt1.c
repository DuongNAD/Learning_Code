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

void maxM(int arr[], int *n)
{
    int max = arr[0];
    for (int i = 0; i < *n; i++)
    {
        if (max < arr[i])
        {
            max = arr[i];
        }
    }
}
int main()
{
    int n, *q;
    int *arr = (int *)malloc(100 * sizeof(int));
    printf("Nhap kich thuoc mang ");
    scanf("%d", &n);
    q = (int *)malloc(n * sizeof(int));
    nhapmang(q, &n);
    printf("Ham da nhap la \n");
    inmang(q, &n);
    maxM(arr, &n);
    free(q);
    return 0;
}