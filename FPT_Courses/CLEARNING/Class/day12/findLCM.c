#include<stdio.h>

int findLCM (int a, int b){
	int i, max;
	int LCM = 0;
	if(a<b){
		max = b;
	}
	else {
		max = a;
	}
	for(i = max;i>0;i++ ){
		if(i% a ==0 && i %b ==0){
			LCM = i;
			break;
		}
	}
	return LCM;
}

int main() {
	int a,b,LCM;
	scanf("%d",&a);
	scanf("%d",&b);
	
	LCM = findLCM(a,b);
	printf("\nOUTPUT\n%d",LCM);
	return 0;
}