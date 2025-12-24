#include<stdio.h>

int main () {
	int n;
	
	int countA = 0;
	int countB = 0;
	int countC = 0;
	int countD = 0;
	
	float score;
	
	do{
		printf("Nhap tong so sinh vien: ");
		scanf("%d",&n);
		if(n<=0){
			printf("So luong khong hop le\n");
		}
	}
	while(n<=0);
	for(int i = 1;i <=n;i++){
			printf("Nhap diem cho sinh vien thu %d: ",i);
			scanf("%f",&score);
			
				if(score <5 && score >=0){
					countD = countD +1;
				}
				else if(score>=5 && score <6.5){
					countC++;
				}
				else if(score>=6.5 && score <8){
					countB++;
				}
				else if(score>=8 && score <=10){
					countA++;
				}
				else{
					printf("Diem khong hop le\n");
					i--;
		}
	}
	
	printf("So hoc sinh diem A = %d\n",countA);
	printf("So hoc sinh dien B = %d\n",countB);
	printf("So hoc sinh dien C = %d\n",countC);
	printf("So hoc sinh dien D = %d\n",countD);
	return 0;
}