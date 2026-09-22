#include<stdio.h>
#include<string.h>

typedef struct SanPham{
	int id;
	char name[30];
	float price;
};

int main (){
	int i,n,j;
	int count = 0;
	int sum = 0;
	struct SanPham sp[30];
	printf("Nhap so sinh vien: ");
	scanf("%d",&n);
	printf("Nhap thong tin Sinh vien: \n");
	for(i =0;i<n;i++){
		printf("Thong tin Sinh vien thu %d\n",i+1);
		printf("idStudent: ");
		scanf("%d",&sp[i].id);
		getchar();
		printf("studentName: ");
		fgets(sp[i].name, sizeof(sp[i].name), stdin);
		sp[i].name[strcspn(sp[i].name, "\n")] = 0; 
		printf("scoreStudent: ");
		scanf("%f",&sp[i].price);
		count ++;
		sum = sum +sp[i].price;
	}
	printf("+-----------------+---------------------------+----------+\n");
    printf("| Ma sinh vien           | Ten sinh vien        |   Diem   |\n");
    printf("+-----------------+---------------------------+----------+\n");

    for (i = 0; i < n; i++) {
        printf("| %-15d | %-25s | %-8.2f |\n", sp[i].id, sp[i].name, sp[i].price);
    }

    printf("+-----------------+---------------------------+----------+\n");

    struct SanPham max = sv[0];
    struct SanPham min =sv[0];
    
    for(int i =1;i<n;i++){
    	if(sp.price >= max.price){
    		max = sp[i];
		}
		else{
			min = sp[i];
		}
	}
    printf("Diem cao nhat %d - %s - %f\n",sp[min].id,sp[min].name,sp[min].price);
    printf("Diem thap nhat %d - %s - %f\n",sp[max].id,sp[max].name,sp[max].price);
	return 0;	
}