#include<stdio.h>
#include<math.h>
int isTriangle(int a, int b,int c){
	if(pow(a,2)+pow(b,2)==pow(c,2)){
		return 1;
	}
	else if(a==b && b==c &&a==c){
		return 2;
	}
	else if((a==b && c != a) || (b==c && a !=c) || (c==a && c != b)){
		return 3;
	}
	else if(((a+b) <c) || ((b+c) <a) || ((a+c)<b)){
		return 5;
	}
	else{
		return 4;
	}
	
	return 0;
}

int main () {
	int a,b,c;
	printf("Nhap a = ");
	scanf("%d",&a);
	printf("Nhap b = ");
	scanf("%d",&b);
	printf("Nhap c = ");
	scanf("%d",&c);
	int kq = isTriangle(a,b,c);
	if(kq ==1){
		printf("Vuong");
	}
	else if(kq ==2){
		printf("Deu");
	}
	else if(kq == 3){
		printf("Can");
	}
	else if(kq ==4){
		printf("Thuong");
	}
	else if(kq ==5){
		printf("Khong phai la tam giac");
	}
	
	return 0;
}