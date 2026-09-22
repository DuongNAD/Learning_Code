#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>


int main() {
  system("cls");
  int n;
    int sum = 0;
    int count = 0;
    int i;
    scanf("%d", &n);
	
    for (i = n; i >= 0; i--) {
        if (i % 2 == 0) {
            sum += i;
            count++;
        }
        
        if (count == 3) {
            break;
        }
    }
    printf("\nOUTPUT:\n");
    if(n<0){
		printf("Error. n >= 0");
		return;
	}
    printf("%d",sum);
    printf("\n");
    system ("pause");
    return(0);
}
