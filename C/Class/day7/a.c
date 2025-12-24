#include<stdio.h>

int main () {
	int *a;
	
	a = (int*)malloc(sizeof(int));
	if(a==NULL){
		printf("Khong du bo nho");
		return 0;
	}
	printf("Nhap a = ");
	scanf("%d",a);
	printf("a = %d",*a);
	free(a);
	return 0;
}