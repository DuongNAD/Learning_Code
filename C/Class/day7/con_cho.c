#include<stdio.h>

int max2(const int *a, const int *b){
	if(*a>*b){
		return *a;
	}
	else{
		return *b;
	}
	return 0;
}

int main () {
	int *a,*b;
	
	a = (int*)malloc(sizeof(int));
	b= (int*)malloc(sizeof(int));
	
	printf("Nhap a = ");
	scanf("%d",a);
	printf("Nhap b = ");
	scanf("%d",b);
	int kq = max2(&a,&b);
	printf("%d",kq);
	free(a);
	free(b);
	return 0;
}