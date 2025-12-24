#include <stdio.h>

void nhapmang(int arr[], int *n)
{
    printf("Nhap so phan tu cua mang: ");
    scanf("%d", n);
    for (int i = 0; i < *n; i++)
    {
        printf("arr[%d] = ", i);
        scanf("%d", &arr[i]);
    }
}
void tanxuat(int arr[], int* n)
{
    int counted[n];
    for (int i = 0; i < *n; i++)
    {
        counted[i] =0;
    }
    for (int i = 0; i < *n; i++)
    {
        if (counted[i] == 1)
        {
            continue;
        }
        int count = 1;
        for (int j = i + 1; j < *n; j++)
        {
            if (arr[i] == arr[j])
            {
                count++;
            }
        }
        printf("phan tu %d xuat hien %d lan\n", arr[i], count);
    }
}
int main()
{
    int arr[100];
    int n;
    nhapmang(arr, &n);
    tanxuat(arr, &n);
    return 0;
}