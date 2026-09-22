#include <stdio.h>

/* 1. Ham tu viet thay the cho strcmp */
int my_string_compare(char s1[], char s2[]) {
    int i = 0;
    
    while (s1[i] == s2[i]) {
        if (s1[i] == '\0') {
            return 0; /* Hai chuoi giong het nhau */
        }
        i++;
    }
    
    /* * Tra ve hieu cua ky tu khac biet dau tien.
     * Neu s1 > s2, ket qua > 0.
     * Neu s1 < s2, ket qua < 0.
     */
    return s1[i] - s2[i];
}

/* 2. Ham tu viet thay the cho strcpy */
void my_string_copy(char dest[], char src[]) {
    int i = 0;
    while (src[i] != '\0') {
        dest[i] = src[i];
        i++;
    }
    dest[i] = '\0'; /* Phai dam bao co ky tu ket thuc chuoi */
}


int main() {
    char names[5][50];
    char temp[50];
    int i, j;

    for (i = 0; i < 5; i++) {
        scanf("%s", names[i]);
    }

    /* 3. Sap xep Bubble Sort dung ham tu viet */
    for (i = 0; i < 4; i++) {
        for (j = 0; j < 4 - i; j++) {
            
            /* Thay vi dung: if (strcmp(names[j], names[j+1]) > 0) */
            if (my_string_compare(names[j], names[j + 1]) > 0) {
                
                /* Thuc hien doi cho (swap) */
                
                /* Thay vi dung: strcpy(temp, names[j]) */
                my_string_copy(temp, names[j]);
                
                /* Thay vi dung: strcpy(names[j], names[j+1]) */
                my_string_copy(names[j], names[j + 1]);
                
                /* Thay vi dung: strcpy(names[j+1], temp) */
                my_string_copy(names[j + 1], temp);
            }
        }
    }

    printf("OUTPUT:\n");
    for (i = 0; i < 5; i++) {
        printf("%s ", names[i]);
    }
    printf("\n");

    return 0;
}