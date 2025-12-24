#include <stdio.h>
int main()
{
    int n;
    printf("Nhap kich thuoc cua mang n = ");
    scanf("%d", &n);
    if (n < 0)
    {
        printf("kich thuoc cua mang khong hop le\n");
        return 0;
    }

    int arr[n];
    printf("Nhap cac phan tu cua mang\n");
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &arr[i]);
    }
    for (int i = 0; i < n; i++)
    {
        printf("arr[%d] = %d", i, arr[i]);
    }
    return 0;
}