#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int my_string_compare(char s1[], char s2[]) {
    int i = 0;
    
    while (s1[i] == s2[i]) {
        if (s1[i] == '\0') {
            return 0; 
        }
        i++;
    }
    
    return s1[i] - s2[i];
}

void my_string_copy(char dest[], char src[]) {
    int i = 0;
    while (src[i] != '\0') {
        dest[i] = src[i];
        i++;
    }
    dest[i] = '\0';
}

int main() {
  system("cls");
  char names[5][50];
    char temp[50];
    int i, j;

    for (i = 0; i < 5; i++) {
        scanf("%s", names[i]);
    }

    for (i = 0; i < 4; i++) {
        for (j = 0; j < 4 - i; j++) {

            if (my_string_compare(names[j], names[j + 1]) > 0) {

                my_string_copy(temp, names[j]);

                my_string_copy(names[j], names[j + 1]);

                my_string_copy(names[j + 1], temp);
            }
        }
    }
  printf("\nOUTPUT:\n");
  for (i = 0; i < 5; i++) {
        printf("%s ", names[i]);
    }
  printf("\n");
  system ("pause");
  return(0);
}
