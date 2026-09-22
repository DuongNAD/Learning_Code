#include <stdio.h>

int main()
{
    int arr[100];
    int n;
    printf("Nhap so luong hoc sinh: ");
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {

        do
        {
            printf("Nhap tuoi cua hoc sinh thu %d (6 den 17 tuoi): ", i + 1);
            scanf("%d", &arr[i]);
            if (arr[i] <= 5 || arr[i] >= 18)
            {
                printf("Tuoi khong hop le. Moi nhap lai\n");
            }
        } while (arr[i] < 6 || arr[i] > 17);
    }

    // printf("\nDanh sach tuoi hoc sinh:\n");
    // for (int i = 0; i < n; i++)
    // {
    //     printf("Tuoi hoc sinh thu %d la: %d\n", i + 1, arr[i]);
    // }
    int max = 0, sum = 0, maxOld, minOld;
    int min = arr[0];
    float trungbinh;

    for (int i = 0; i < n; i++)
    {
        if (arr[i] < min)
        {
            min = arr[i];
            minOld = i + 1;
        }
    }

    for (int i = 0; i < n; i++)
    {
        if (arr[i] > max)
        {
            max = arr[i];
            maxOld = i + 1;
        }
    }
    for (int i = 0; i < n; i++)
    {
        sum = sum + arr[i];
    }
    printf("Nguoi thu %d co tuoi nho nhat la %d\n", minOld, min);
    printf("Nguoi thu %d co tuoi lon nhat la %d\n", maxOld, max);
    printf("Tuoi trung binh = %.2f\n", (float)sum / n);
    return 0;
}