#include <stdio.h>
#include <string.h>

struct Student {
    char id[10];
    char name[50];
    float score;
};

/*
 * Ham nay tra ve VI TRI (index) cua sinh vien
 * DAU TIEN dat diem cao nhat.
 */
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

    /* Buoc 1: Tim ra diem so cao nhat la bao nhieu */
    int firstTopIndex = findTopStudent(list, n);
    
    if (firstTopIndex != -1) {
        float maxScore = list[firstTopIndex].score;

        /* * Buoc 2: Duyet lai ca danh sach, 
         * in ra bat ky ai co diem bang maxScore
         */
        for (i = 0; i < n; i++) {
            if (list[i].score == maxScore) {
                printf("%s %s %.1f\n", list[i].id, list[i].name, list[i].score);
            }
        }
    }

    return 0;
}