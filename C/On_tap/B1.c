// Hãy tạo các hàm và viết MENU cho các bài sau (1-14).
// Bài 1. In ra màn hình 10 số tự nhiên đầu tiên.
// Bài 2. Nhập vào đoạn [a.b]. In ra màn hình tổng các số từ a đến b.
// Bài 3 Nhập vào đoạn [a.b]. In ra màn hình tổng các số chẵn từ a đến b.
// Bài 4 Tính S(n) = 1 + 2 + 3 + … + n bằng
// Bài 5 Tính S(n) = x^2 + x^4 + … + x^2n
// Bài 6. Tính S(n) = x + x^3 + x^5 + … + x^(2n - 1)
// Bài 7 Liệt kê tất cả các ước số lẻ của số nguyên dương n.
// Bài 8 Viết chương trình tính N giai thừa.
// Bài 9 Viết chương trình in ra màn hình bảng cửu chương N.
// Bài 10 Nhập số từ bàn phím cho tới khi nhập số 28 thì dừng
// Bài 11  Viết chương kiểm tra xem N có phải số nguyên tố hay không.
// Bài 12, Nhập vào số N. in ra số đảo ngược của N. VD: 12345  -> 54321
// Bài 13. Hai số gọi là đảo ngược của nhau nếu viết theo chiều thuận hay chiều ngược cũng có cùng giá trị. VD: 121 = 121, 11111,... Hãy viết chương trình xác định số trên.
// Bài 14. Số tự nhiên được gọi là số đẹp nếu cộng các chữ số của lại ta có một số mà kết thúc bằng 9. Ví dụ một số số đẹp là 18 (1+8=9), 234(2+3+4), 658 (6+5+8=19). Nhập một số N, hãy kiểm tra xem N có phải là số đẹp hay không?

#include <stdio.h>
#include <math.h>

void in_10(int n)
{
    printf("Nhap so tu nhien muon hien: ");
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        printf("%d\t", i);
    }
    printf("\n");
}

void sum_a_b(int a, int b)
{

    printf("Nhap a = ");
    scanf("%d", &a);
    printf("Nhap b = ");
    scanf("%d", &b);
    if (a > b)
    {
        printf("Error");
        return;
    }
    int sum = 0;
    for (int i = a; i <= b; i++)
    {
        sum += i;
    }
    printf("Tong cac so tu  a den b = %d", sum);
}

void sumEven_a_b(int a, int b)
{
    printf("Nhap a = ");
    scanf("%d", &a);
    printf("Nhap b = ");
    scanf("%d", &b);
    if (a > b)
    {
        printf("Error");
        return;
    }
    int sum = 0;
    for (int i = a; i <= b; i++)
    {
        if (i % 2 == 0)
        {
            sum += i;
        }
    }
    printf("Tong cac so chan tu a den b = %d", sum);
}

void Sum_n(int n)
{
    int sum = 0;
    printf("Nhap n = ");
    scanf("%d", &n);
    for (int i = 1; i <= n; i++)
    {
        sum += i;
    }
    printf("S(n) = %d", sum);
}

void Sum_Even_n(int x, int n)
{
    printf("Nhap n = ");
    scanf("%d", &n);
    printf("Nhap x = ");
    scanf("%d", &x);
    int sum = 0;
    for (int i = 1; i <= n; i++)
    {
        sum = sum + pow(x, 2 * n);
    }
    printf("S(n) = %d", sum);
}

void Sum_Odd_n(int x, int n)
{
    printf("Nhap n = ");
    scanf("%d", &n);
    printf("Nhap x = ");
    scanf("%d", &x);
    int sum = 0;
    for (int i = 1; i <= n; i++)
    {
        sum = sum + pow(x, 2 * n - 1);
    }
    printf("S(n) = %d", sum);
}

void Odd_divisor(int n)
{
    printf("Nhap n = ");
    scanf("%d", &n);
    printf("Cac uoc le cua n la: \n");
    for (int i = 1; i < n; i++)
    {
        if (n % i == 0 && i % 2 == 1)
        {
            printf("%d", i);
        }
    }
}

void Sum_giaithua(int n)
{
    printf("Nhap n = ");
    scanf("%d", &n);
    long long sum = 1;
    for (int i = 1; i <= n; i++)
    {
        sum = sum * i;
    }
    printf("n! = %lld", sum);
}

void Bang_cuu_chuong()
{
    for (int i = 1; i <= 10; i++)
    {
        for (int j = 1; j <= 10; j++)
        {
            printf("%d * %d = %d\t", j, i, i * j);
        }
        printf("\n");
    }
}

void print_28(int n)
{

    do
    {
        printf("Nhap n = ");
        scanf("%d", &n);
        if (n != 28)
        {
            printf("Moi nhap 28 de thoat chuong chuong trinh\n");
            printf("Moi nhap lai\n");
        }
    } while (n != 28);
    printf("Da thoat chuong trinh\n");
}

void Check_prime_number(int n)
{
    printf("Nhap so n muon kiem tra: ");
    scanf("%d", &n);
    if (n < 2)
    {
        printf("%d khong phai la so nguyen to \n");
        return;
    }
    for (int i = 2; i * i <= n; i++)
    {
        if (n % i == 0)
        {
            printf("%d khong phai la so nguyen to\n", n);
            return;
        }
    }
    printf("%d la so nguyen to\n", n);
}

void print_Reversed_number(int n)
{
    printf("Nhap n = ");
    scanf("%d", &n);
    int prime = n;
    int sum = 0;
    while (n > 0)
    {
        int m = n % 10;
        sum = sum * 10 + m;
        n /= 10;
    }
    printf("So dao nguoc cua %d la %d\n", prime, sum);
}

void check_Reversed_number(int n)
{
    printf("Nhap n = ");
    scanf("%d", &n);
    int prime = n;
    int sum = 0;
    while (n > 0)
    {
        int m = n % 10;
        sum = sum * 10 + m;
        n /= 10;
        if (prime == sum)
        {
            printf("%d la so dao nguoc", sum);
            return;
        }
    }
    printf("%d khong phai la so dao nguoc", sum);
}

void beautiful_number(int n)
{
    printf("Nhap so n = ");
    scanf("%d", &n);
    int prime = n;
    int sum = 0;
    while (n > 0)
    {
        int m = n % 10;
        sum = sum + m;
        n /= 10;
    }
    if (sum % 10 == 9)
    {
        printf("%d la o dep ", prime);
    }
    else
    {
        printf("%d khong phai la so dep", prime);
    }
}
int main()
{
    int n, a, b, luachon;
    int x;
    char Tieptuc;

    do
    {
        printf("================================MENU============================\n");
        printf("1. In ra n so tu nhien dau tien\n");
        printf("2. Tong tu a den b\n");
        printf("3. Tong cac so chan tu a den b\n");
        printf("4. Tinh S(n) = 1+ 2 + ... + n\n");
        printf("5. Tinh S(n) = x^2 + x^4 + ... + x^2n\n");
        printf("6. Tinh S(n) = x + x^3 + x^5 + … + x^(2n - 1)\n");
        printf("7. Liet ke uoc le cua so nguyen n\n");
        printf("8. Tinh n! = \n");
        printf("9. In ra bang cuu chuong \n");
        printf("10. Nhap tu ban phim cho den khi nhap so 28 thi dung\n");
        printf("11. Kiem tra xem n co phai so nguyen to khong\n");
        printf("12. Nhap vao so n in ra so dao nguoc\n");
        printf("13. Kiem tra xem n co phai so dao nguoc khong\n");
        printf("14. Kiem tra xem n co phai so dep khong\n");
        printf("15. Thoat chuong trinh\n");
        printf("==================================================================\n");
        printf("\n");
        printf("Lua chon (1 - 15): ");
        scanf("%d", &luachon);
        printf("\n");
        switch (luachon)
        {
        case 1:
            in_10(n);
            break;
        case 2:
            sum_a_b(a, b);
            break;
        case 3:
            sumEven_a_b(a, b);
            break;
        case 4:
            Sum_n(n);
            break;
        case 5:
            Sum_Even_n(x, n);
            break;
        case 6:
            Sum_Odd_n(x, n);
            break;
        case 7:
            Odd_divisor(n);
            break;
        case 8:
            Sum_giaithua(n);
            break;
        case 9:
            Bang_cuu_chuong();
            break;
        case 10:
            print_28(n);
            break;
        case 11:
            Check_prime_number(n);
            break;
        case 12:
            print_Reversed_number(n);
            break;
        case 13:
            check_Reversed_number(n);
            break;
        case 14:
            beautiful_number(n);
            break;
        case 15:
            return 0;
        default:
            printf("Lua chon khong hop le\n");
            break;
        }
        printf("\n");
        printf("Ban co muon tiep tuc chuong trinh khong y/n: ");
        getchar();
        scanf("%c", &Tieptuc);

    } while (Tieptuc == 'Y' || Tieptuc == 'y');
    return 0;
}