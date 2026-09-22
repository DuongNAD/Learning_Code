#include <stdio.h>

#include <stdio.h>
#include <ctype.h> // Để dùng hàm toupper (chuyển ký tự thường thành hoa)


float TinhTienTaxi(char type, float distance)
{
    float baseFare = 0.0;
    float distanceFare = 0.0;

    switch (toupper(type))
    {
        case 'E':
            baseFare = 3.0;
            break;
        case 'L':
            baseFare = 6.0;
            break;
        default:
            return -1.0; 
    }
    
    if (distance < 0) {
        return -2.0;
    }

    if (distance <= 5)
    {
        distanceFare = distance * 1.5;
    }
    else if (distance <= 10)
    {
        distanceFare = (5 * 1.5) + (distance - 5) * 1.25;
    }
    else
    {
        distanceFare = (5 * 1.5) + (5 * 1.25) + (distance - 10) * 1.0;
    }
    
    return baseFare + distanceFare;
}

int main()
{
    char type;
    float distance; 
    float money;
    
    do
    {
        printf("Nhap loai xe (E/L): ");
        scanf(" %c", &type); 

        printf("Nhap khoang cach (km): ");
        scanf("%f", &distance); 
        
        money = TinhTienTaxi(type, distance);
        
        if (money == -1.0)
        {
            printf("Loi! Loai xe '%c' khong hop le. Vui long nhap lai.\n\n", type);
        }
        else if (money == -2.0)
        {
            printf("Loi! Khoang cach phai la so >= 0. Vui long nhap lai.\n\n");
        }
        
    } while (money < 0); 
    
    printf("--------------------------------\n");
    printf("Loai xe: %c\n", toupper(type));
    printf("Quang duong: %.2f km\n", distance);
    printf("Tong tien cuoc: %.2f USD\n", money);
    
    return 0;
}