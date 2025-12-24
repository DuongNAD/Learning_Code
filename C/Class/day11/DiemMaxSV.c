#include <stdio.h>

struct SinhVien {
	int id;
    char ten[50];
    float diem;
};

int main() {
    int n;
    printf("Nhap so sinh vien: ");
    scanf("%d", &n);
    struct SinhVien sv[n];

    for (int i = 0; i < n; i++) {
    	printf("Nhap id: ");
    	scanf("%d",&sv[i].id);
        printf("Nhap ten: ");
        fflush(stdin);
        gets(sv[i].ten);
        printf("Nhap diem: ");
        scanf("%f", &sv[i].diem);
    }

    int maxIndex = 0;
    float max =sv[0].diem;
    for (int i = 1; i < n; i++) {
        if (max < sv[i].diem)
            max =sv[i].diem;
            maxIndex = i;
            break;
    }

    printf("Sinh vien co diem cao nhat: %d %s %.2f\n",sv[maxIndex].id, sv[maxIndex].ten, sv[maxIndex].diem);
    return 0;
}