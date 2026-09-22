// Bài 9: Cấp phát động với mảng số nguyên (10 điểm)
// Viết chương trình nhập vào n số nguyên, dùng cấp phát động (malloc hoặc calloc) để lưu mảng, sau đó tính tổng các phần tử trong mảng.

#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n;
    int *c = (int *)malloc(100 * sizeof(int));
    if (c == NULL)
    {
        printf("Error");
        return 1;
    }
    printf("So nguyen muon nhap: ");
    scanf("%d", &n);

    int sum = 0;
    for (int i = 0; i < n; i++)
    {
        printf("c[%d] = ", i);
        scanf("%d", &c[i]);
    }
    for (int i = 0; i < n; i++)
    {
        sum = sum + c[i];
    }
    printf("Tong cac phan tu trong mang = %d\n", sum);
    free(c);
    return 0;
}