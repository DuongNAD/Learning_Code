// Bài 1: Nhập/Xuất số nguyên (5 điểm)
// Viết chương trình C nhập vào một số nguyên n, sau đó in ra màn hình số đó và bình phương của nó.

#include <stdio.h>

int main()
{
    int n;
    printf("Nhap so nguyen n: ");
    
    if (scanf("%d", &n) != 1)
    {
        printf("Error");
        return 0;
    }
    int m = n * n;
    printf("binh phuong cua %d = %d", n, m);
    return 0;
}