#include<stdio.h>
#include<math.h>
unsigned long long ipow(int a, int b){
	if(b==0){
		return 1;
	}
	if(a == 0){
		return 0;
	}
	
	
	unsigned long long mu = pow(a,b);
	return mu;
}

int main () {
	int a,b;
	printf("Nhap a = ");
	scanf("%d",&a);
	printf("Nhap b = ");
	scanf("%d",&b);
	if (a <0 || b< 0){
		printf("So nhap vao khong hop le");
		return;
	}
	unsigned long long kq = ipow(a,b);
	printf("%d^%d = %llu",a,b,kq);
	return 0;
}