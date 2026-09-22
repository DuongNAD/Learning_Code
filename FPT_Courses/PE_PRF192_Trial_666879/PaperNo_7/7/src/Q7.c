#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>


int main() {
  system("cls");
  char str[21];
    int len, midIndex, startIndex, endIndex, i;

    scanf("%s", str);

    len = strlen(str);
    
    midIndex = len / 2;
    
    startIndex = midIndex - 2;
    endIndex = midIndex + 2;

  printf("\nOUTPUT:\n");
  for (i = startIndex; i <= endIndex; i++) {
        printf("%c", str[i]);
    }
  printf("\n");
  system ("pause");
  return(0);
}
