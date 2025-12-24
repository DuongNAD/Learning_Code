#include <stdio.h>
#include <stdlib.h>
int main()
{
    int luachon;
    do
    {
        printf("====================MENU====================\n");
        printf("1. In ra man hinh 10 so tu nhien dau tien\n");
        printf("2. Nhap vao doan [a,b]. In ra man hinh\n");
        printf("3. Tinh S(n) 1 + 2 + 3 + 4 + ... + n =\n");
        printf("4. Viet vhuong trinh tinh N giai thua\n");
        printf("5. Thoat chuong trinh\n");
        printf("============================================\n");
        printf("\nChon tu (1 - 5): ");
        scanf("%d", &luachon);
        if (luachon == 1)
        {

            system("cls");
            printf("Man hinh da duoc xoa");
            printf("Chuc nang 1\n");
        }
        else if (luachon == 2)
        {

            system("cls");
            printf("Man hinh da duoc xoa");
            printf("Chuc nang 2\n");
        }
        else if (luachon == 3)
        {

            system("cls");
            printf("Man hinh da duoc xoa");
            printf("Chuc nang 3\n");
        }
        else if (luachon == 4)
        {

            system("cls");
            printf("Man hinh da duoc xoa");
            printf("Chuc nang 4\n");
        }
        else if (luachon == 5)
        {
            printf("Thoat chuong trinh\n");
        }
        system("cls");
        printf("Man hinh da duoc xoa");
    } while (luachon != 5);
    return 0;
}