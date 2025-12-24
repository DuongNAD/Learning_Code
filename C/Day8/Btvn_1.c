#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
void nhapmang(int arr[], int *n)
{
    printf("Nhap kich thuoc mang: ");
    scanf("%d", n);
    for (int i = 0; i < *n; i++)
    {
        printf("arr[%d] = ", i);
        scanf("%d", &arr[i]);
    }
}
void inmang(int arr[], int *n)
{
    printf("In mang: ");
    for (int i = 0; i < *n; i++)
    {
        printf("arr[%d] = %d\t", i, arr[i]);
    }
    printf("\n");
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
    printf("Max = %d", max);
}
void minM(int arr[], int *n)
{
    int min = arr[0];
    for (int i = 0; i < *n; i++)
    {
        if (min > arr[i])
        {
            min = arr[i];
        }
    }
    printf("Min = %d", min);
}
void trungbinhcong(int arr[], int *n)
{
    int tong = 0;
    if (*n == 0)
    {
        printf("Mang rong, khong the tinh trung binh cong");
        return;
    }
    for (int i = 0; i < *n; i++)
    {
        tong = tong + arr[i];
    }
    int trungbinhcong = tong / (*n);
    printf("Trung binh cong = %d", trungbinhcong);
}
void sothuannghich(int arr[], int *n)
{
    int dem = 0;
    printf("Cac so thuan nghich trong mang la: \n");
    for (int i = 0; i < *n; i++)
    {
        if (arr[i] < 0)
        {
            continue;
        }
        int songhichdao = 0;
        int thuc = arr[i];
        while (thuc != 0)
        {
            int tong = thuc % 10;
            thuc /= 10;
            songhichdao = songhichdao * 10 + tong;
        }
        if (arr[i] == songhichdao)
        {
            dem = dem + 1;
            printf("arr[%d] = %d\n", i, arr[i]);
        }
    }
    printf("Tong so thuan nghich = %d", dem);
}
void songuyento(int arr[], int *n)
{
    int count = 0;
    printf("Cac so nguyen to la: \n");
    for (int i = 0; i < *n; i++)
    {

        if (arr[i] <= 1)
        {
            continue;
        }
        int isPrime = 1;
        for (int j = 2; j * j <= arr[i]; j++)
        {
            if (arr[i] % j == 0)
            {
                isPrime = 0;
                break;
            }
        }
        if (isPrime == 1)
        {
            count++;
            printf("arr[%d] = %d\t", i, arr[i]);
        }
    }
    printf("\n");
    printf("\nTong so so nguyen to = %d", count);
}
void tangdan(int arr[], int *n)
{
    if (*n < 0)
    {
        printf("Error\n");
        return;
    }

    for (int i = 0; i < *n - 1; i++)
    {
        for (int j = 0; j < *n - i - 1; j++)
        {
            if (arr[j] > arr[j + 1])
            {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
    printf("Mang sau khi sap xep tang dan: \n");
    for (int i = 0; i < *n; i++)
    {
        printf("arr[%d] = %d\t", i, arr[i]);
    }
}
void giamdan(int arr[], int *n)
{
    if (*n < 0)
    {
        printf("Error\n");
        return;
    }

    for (int i = 0; i < *n - 1; i++)
    {
        for (int j = 0; j < *n - i - 1; j++)
        {
            if (arr[j] < arr[j + 1])
            {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
    printf("Mang sau khi sap xep giam dan: \n");
    for (int i = 0; i < *n; i++)
    {
        printf("arr[%d] = %d\t", i, arr[i]);
    }
}
void count(int arr[], int *n)
{
    int V;
    printf("Nhap gia tri ban muon kiem tra: ");
    scanf("%d", &V);
    int countV = 0;
    for (int i = 0; i < *n; i++)
    {
        if (arr[i] == V)
        {
            countV = countV + 1;
        }
    }
    printf("count = %d", countV);
}
void them(int arr[], int *n)
{
    int V, k;
    printf("Nhap vi tri ban muon them: ");
    scanf("%d", &k);
    if (k < 0 || k > *n)
    {
        printf("Vi tri khong hop le");
        return;
    }
    printf("Nhap gia tri ban muon them: ");
    scanf("%d", &V);
    for (int i = *n; i > k - 1; i--)
    {
        arr[i] = arr[i - 1];
    }
    arr[k] = V;
    (*n)++;
    printf("Phan tu %d da duoc them o vi tri %d\n", V, k);
    inmang(arr, n);
}
void xoa(int arr[], int *n)
{
    int V, k;
    printf("Nhap vi tri ban muon xoa: ");
    scanf("%d", &k);
    if (k < 0 || k > *n)
    {
        printf("Vi tri khong hop le");
        return;
    }
    for (int i = k; i < *n - 1; i++)
    {
        arr[i] = arr[i + 1];
    }
    (*n)--;
    printf("Phan tu %d da duoc xoa o vi tri %d\n", V, k);
    inmang(arr, n);
}

void tangdanY_N(int arr[], int *n)
{
    int c = 1;
    for (int i = 0; i < *n - 1; i++)
    {
        if (arr[i] > arr[i + 1])
        {
            c = 0;
            break;
        }
    }
    if (c == 1)
    {
        printf("Yes");
        return;
    }
    if (c == 0)
    {
        printf("No");
        return;
    }
}
void daonguoc(int arr[], int *n)
{
    for (int i = *n - 1; i >= 0; i--)
    {
        printf("arr[%d] = %d\t", i, arr[i]);
    }
}
void count_number(int arr[], int *n)
{
    bool visited[*n]; // Mảng đánh dấu
    for (int i = 0; i < *n; i++)
    {
        visited[i] = false; // Ban đầu chưa phần tử nào được xử lý
    }
    printf("\n");
    for (int i = 0; i < *n; i++)
    {
        if (!visited[i])
        {                  // Nếu chưa xử lý phần tử này
            int count = 1; // Tần suất của phần tử này
            for (int j = i + 1; j < *n; j++)
            {
                if (arr[i] == arr[j])
                {
                    count++;
                    visited[j] = true; // Đánh dấu phần tử trùng lặp
                }
            }
            printf("So %d xuat hien %d lan \n", arr[i], count);
        }
    }
}
void xoaV(int arr[], int *n)
{
    int V, k;
    int count = 0;
    printf("Nhap gia tri ban muon xoa: ");
    scanf("%d", &V);
    for (int i = 0; i < *n; i++)
    {
        if (V == arr[i])
        {
            for (int j = i; j < *n - 1; j++)
            {
                arr[j] = arr[j + 1];
            }
            (*n)--;
            i--;
        }
    }
    printf("Mang sau khi xoa: ");
    for (int i = 0; i < *n; i++)
    {
        printf("arr[%d] = %d\t", i, arr[i]);
    }
}
int main()
{
    int luachon, n;
    int *arr = (int *)malloc(100 * sizeof(int));
    nhapmang(arr, &n);
    inmang(arr, &n);
    printf("\n");
    char tieptuc;
    do
    {
        printf("============================MENU==========================\n");
        printf("1. Tim max\n");
        printf("2. Tim min\n");
        printf("3. Tinh trung binh cong\n");
        printf("4. Dem va liet ke cac so thuan nghich trong mang\n");
        printf("5. Dem va liet ke cac so nguyen to trong trong mang\n");
        printf("6. Sap xep theo thu tu tang dan\n");
        printf("7. Sap xep theo thu tu giam dan\n");
        printf("8. Dem so lan xuat hien cua gia tri V\n");
        printf("9. Hien thi tan suat xuat hien cac gia tri trong mang\n");
        printf("10. Them phan tu V tai vi tri k\n");
        printf("11. Xoa phan tu tai vi tri k\n");
        printf("12. Xoa tat ca phan tu co gia tri V\n");
        printf("13. Dao nguoc mang\n");
        printf("14. Kiem tra mang co tang dan khong\n");
        printf("15. Thoat chuong trinh\n");
        printf("==========================================================\n");
        printf("\n");
        printf("Chon tu 1 - 15: ");
        scanf("%d", &luachon);

        switch (luachon)
        {
        case 1:
            maxM(arr, &n);
            break;
        case 2:
            minM(arr, &n);
            break;
        case 3:
            trungbinhcong(arr, &n);
            break;
        case 4:
            sothuannghich(arr, &n);
            break;
        case 5:
            songuyento(arr, &n);
            break;
        case 6:
            tangdan(arr, &n);
            break;
        case 7:
            giamdan(arr, &n);
            break;
        case 8:
            count(arr, &n);
            break;

        case 9:
            count_number(arr, &n);
            break;

        case 10:
            them(arr, &n);
            break;
        case 11:
            xoa(arr, &n);
            break;
        case 12:
            xoaV(arr, &n);
            break;
        case 13:
            daonguoc(arr, &n);
            break;
        case 14:
            tangdanY_N(arr, &n);
            break;
        case 15:
            printf("Chuong trinh da ket thuc. \n");
            return 0;
        default:
            printf("Lua chon khong hop le\nMoi chon lai\n");
            break;
        }
        printf("\nBan co muon thuc hien tiep (y/n)? ");
        scanf(" %c", &tieptuc);
    } while (tieptuc == 'y' || tieptuc == 'Y');
    printf("Chuong trinh da ket thuc. \n");
    free(arr);
    return 0;
}