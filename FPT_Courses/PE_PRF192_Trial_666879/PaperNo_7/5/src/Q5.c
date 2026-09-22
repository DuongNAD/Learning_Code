#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>


int main() {
  system("cls");
  int n;
    int arr[20];
    int i;
    int isSymmetric = 1; 


    scanf("%d", &n);

    for (i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    for (i = 0; i < n / 2; i++) {
        if (arr[i] != arr[n - 1 - i]) {
            isSymmetric = 0; 
            break;           
        }
    }
  printf("\nOUTPUT:\n");
  printf("%d",isSymmetric);
  printf("\n");
  system ("pause");
  return(0);
}
