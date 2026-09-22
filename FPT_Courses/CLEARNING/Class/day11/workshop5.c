#include<stdio.h>

int main () {
	int n,i,sum = 0, count=0;
	char arrayC[100];
	int arrayN[100];
	int countUP = 0;
	int countL = 0;
	int countN =0;
	int kitu =0;
	fgets(arrayC, sizeof(arrayC), stdin);
	for(i = 0;i < arrayC[i] != '\0';i++){
		
		if(arrayC[i] >='A' && arrayC[i]<='Z'){
			countUP++;
		}
		else if(arrayC[i] >='a' && arrayC[i]<='z'){
			countL++;
		}
		else if(arrayC[i] >='0' && arrayC[i]<='9'){
			countN++;
		}
		else {
			kitu++;
		}
	}
	
	printf("\nOUTPUT\n");
	printf("%d\n",countUP);
	printf("%d\n",countL);
	printf("%d\n",countN);
	printf("%d",kitu);
	
	return 0;
}