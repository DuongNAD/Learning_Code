    #include<stdio.h>
    #include<math.h>

    int main () {
        float a,b;
        char c;
        printf("Nhap a = ");
        scanf("%f",&a);
        printf("Nhap a = ");
        scanf("%f",&b);
        printf("Nhap dau: ");
        scanf(" %c",&c);
        switch (c)
        {
        case '+':
            printf("%f + %f = %f",a,b,a+b );
            break;
        case '-':
            printf("%f - %f = %f",a,b,a-b );
            break;
        case '*':
            printf("%f * %f = %f",a,b,a*b );
            break;
        case '/':
            printf("%f / %f = %f",a,b,a/b );
            break;
        default:
            printf("Day khong phai bieu thuc");
            break;
        }

        return 0;
    }