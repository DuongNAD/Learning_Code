#include<stdio.h>

int main () {
	int n;
	printf("Nhap n = ");
	scanf("%d",&n);
	printf("n truoc thay doi %d\n",n);
	
	int *pn = &n;
	
	*pn = 10;
	
	printf("n sau hay doi %d",n);
	return 0;
}