#include<stdio.h>

int main() {
	int a, b, c, s;

	printf("Nhap a = ");

	scanf("%d",&a);
	printf("Nhap b = ");
	scanf("%d",&b);
	printf("Nhap c = ");
	scanf("%d",&c);

	s = (a + b + c) / 2;
	printf("s = %d", s);
	return 0;
}