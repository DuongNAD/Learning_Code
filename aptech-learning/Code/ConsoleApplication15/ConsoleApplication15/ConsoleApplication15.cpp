#include<stdio.h>

int main() {
	int a, b, c, s;
	printf("Nhap a = ");
	scanf_s("%d",&a);

	printf("Nhap b = ");
	scanf_s("%d",&b);

	printf("Nhap c = ");
	scanf_s("%d", &c);

	s = (a + b + c) / 2;
	printf("s = %d", s);
	return 0;
}