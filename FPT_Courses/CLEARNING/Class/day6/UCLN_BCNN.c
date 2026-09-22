#include<stdio.h>

int UC_LN (int a, int b){
	int i, tempt;
	int UCLN;
	if(a<b){
		tempt = a;
	}
	else{
		tempt =b;
	}
	for (i = tempt;i>2;i--){
		if(b%i == 0 && a%i ==0){
			UCLN = i;
			break;
		}
	}
	return UCLN;
}

int BC_NN (int a, int b){
	long long BCNN = (a*b)/UC_LN(a,b);
	return BCNN;
}

int main () {
	int a,b;
	printf("a = ");
	scanf("%d",&a);
	printf("b = ");
	scanf("%d",&b);
	int UCLN = UC_LN(a,b);
	unsigned long long BCNN = BC_NN(a,b);
	
	printf("UCLN = %d\n",UCLN);
	printf("BCNN = %llu\n",BCNN);
	return 0;  
}