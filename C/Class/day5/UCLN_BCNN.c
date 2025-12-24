#include<stdio.h>

int main () {
	int a;
	printf("Nhap a = ");
	scanf("%d",&a);
	int b;
	printf("Nhap b = ");
	scanf("%d",&b);
	int UCLN;
	int BCNN;
	for(int i = (a > b ? b : a); i>0;i-- ){
		if (a%i==0 && b%i ==0){
			UCLN = i;
			break;
		}
	}
	long long BCNN = (long long)a * b / UCLN; 
	
	printf("Uoc chung lon nhat = %d\n",UCLN);
	printf("Boi chung nho nhat = %lld5\n",BCNN);
	return 0;
}