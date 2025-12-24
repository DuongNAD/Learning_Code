#include<stdio.h>
#include<ctype.h>

int main () {
	char c[100];
	printf("Nhap chuoi: ");
	
	fgets(c, sizeof(c), stdin);
	c[strcspn(c, "\n")] = '\0';
	
	int chu =0;
	int so=0;
	int ki_tu=0;S
	for(int i =0;c[i] != '\0';i++){
		if(isalpha(c[i])){
			chu = chu +1;
		}
		else if(isdigit(c[i])){
			so = so +1;
		}
		else {
			ki_tu = ki_tu +1;
		}
	}
	printf("Chu %d\n",chu);
	printf("So %d\n",so);
	printf("ki_tu %d",ki_tu);
	return 0;
}