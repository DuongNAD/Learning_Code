#include<stdio.h>

unsigned long long giai_thua(int n){
	int i;
	unsigned long long ket_qua =1;
	if(n<1){
		printf("n phai la so >0");
		return 0;
	}
	if(n == 0){
		return 1;	
	}
	for (i=1;i<=5;i++){
		ket_qua = ket_qua * i;
	}
	return ket_qua;
}

int main () {
	int n;
	printf("Nhap n! = ");
	scanf("%d",&n);
	unsigned long long kq = giai_thua(n);
	if(n >=0){
	
	printf("%d! = %llu",n,kq);
}
	return 0;
}