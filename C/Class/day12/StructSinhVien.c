#include<stdio.h>
#include<ctype.h>

struct Student {
    char id[10];
    char name[50];
    float score;
};

int findTopStudent(struct Student sv[], int n){
	float max = sv[0].score;
	int index=0;
    int i;
	for(i = 0 ;i<n;i++){
		if(sv[i].score > max){
			max = sv[i].score;
			index  = i;
		}
	}
	return index;
}

int main () {
    int n, i;
    scanf("%d", &n);
    struct Student sv[100];
	for (i = 0; i < n; i++) {
	scanf("%s", sv[i].id); 
	scanf(" %[^\n]", sv[i].name);
    scanf("%f", &sv[i].score);
    }
	
	int topIndex = findTopStudent(sv, n);

    if (topIndex != -1) {
        printf("\n--- SINH VIEN DIEM CAO NHAT ---\n");
        printf("ID: %s\n", sv[topIndex].id);
        printf("Ten: %s\n", sv[topIndex].name);
        printf("Diem: %.2f\n", sv[topIndex].score);
    }

    return 0;
}