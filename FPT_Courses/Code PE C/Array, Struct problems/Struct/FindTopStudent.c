#include <stdio.h>
#include <string.h>

struct Student {
    char id[10];
    char name[50];
    float score;
};

int findTopStudent(struct Student a[], int n) {
    if (n <= 0) {
        return -1; 
    }

    int maxIndex = 0;
    float maxScore = a[0].score;
    int i;

    for (i = 1; i < n; i++) {
        if (a[i].score > maxScore) {
            maxScore = a[i].score;
            maxIndex = i;
        }
    }
    
    return maxIndex;
}

int main() {
    int n;
    struct Student list[50];
    int i;

    scanf("%d", &n);

    for (i = 0; i < n; i++) {
        scanf("%s %s %f", list[i].id, list[i].name, &list[i].score);
    }

    int topIndex = findTopStudent(list, n);

    if (topIndex != -1) {
        printf("%s %s %.1f\n", list[topIndex].id, list[topIndex].name, list[topIndex].score);
    }

    return 0;
}