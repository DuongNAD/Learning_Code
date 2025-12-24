#include <stdio.h>

int main()
{
    float n;

start:
    printf("Nhap vao 1 so n >= 20: ");
    scanf("%f", &n);

    if (n>=20)
    {
        printf("So ban da nhap: %.2f\n", n);
    }
    else
    {
        goto start;
    }

    return 0;
}
