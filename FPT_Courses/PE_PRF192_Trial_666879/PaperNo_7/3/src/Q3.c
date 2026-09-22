#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>


int main() {
  system("cls");
  char chars[4];
    char temp;
    int i, j;

    for (i = 0; i < 4; i++) {
        scanf(" %c", &chars[i]);
    }

    for (i = 0; i < 3; i++) {
        for (j = 0; j < 3 - i; j++) {
            if (chars[j] > chars[j + 1]) {
                temp = chars[j];
                chars[j] = chars[j + 1];
                chars[j + 1] = temp;
            }
        }
    }
  printf("\nOUTPUT:\n");
  for (i = 0; i < 4; i++) {
        printf("%c ", chars[i]);
    }
    printf("\n");

  system ("pause");
  return(0);
}
