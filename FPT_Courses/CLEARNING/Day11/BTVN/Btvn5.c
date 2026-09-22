#include <stdio.h>
#include <string.h>
#include <ctype.h>

typedef struct Sinh_vien
{
    char ma_sv[50];
    char ten[50];
    char gioitinh[10];
    float diem_toan;
    float diem_li;
    float diem_hoa;
} SV;

void clearBuffer()
{
    while ((getchar()) != '\n')
        ;
}

void nhap(SV *sv)
{
    printf("Nhap ma sinh vien: ");
    fgets(sv->ma_sv, sizeof(sv->ma_sv), stdin);
    sv->ma_sv[strcspn(sv->ma_sv, "\n")] = '\0';

    printf("Nhap ho va ten: ");
    fgets(sv->ten, sizeof(sv->ten), stdin);
    sv->ten[strcspn(sv->ten, "\n")] = '\0';

    printf("Nhap gioi tinh: ");
    fgets(sv->gioitinh, sizeof(sv->gioitinh), stdin);
    sv->gioitinh[strcspn(sv->gioitinh, "\n")] = '\0';

    printf("Nhap diem: \n");
    printf("Toan: ");
    scanf("%f", &sv->diem_toan);
    printf("Li: ");
    scanf("%f", &sv->diem_li);
    printf("Hoa: ");
    scanf("%f", &sv->diem_hoa);
    clearBuffer();
}

void xuat(SV sv)
{
    printf("Ma sinh vien: %s\n", sv.ma_sv);
    printf("ho va ten %s\n", sv.ten);
    printf("Diem cac mon: \n");
    printf("Toan: %.2f\n", sv.diem_toan);
    printf("li: %.2f\n", sv.diem_li);
    printf("Hoa: %.2f\n", sv.diem_hoa);
    printf("\n");
}

void nhapdanhsachsv(SV sv[], int n)
{
    for (int i = 0; i < n; i++)
    {
        printf("Nhap thong tin sinh vien thu %d: \n", i + 1);
        nhap(&sv[i]);
        printf("\n");
    }
}

void xuatdanhsachsv(SV sv[], int n)
{
    for (int i = 0; i < n; i++)
    {
        printf("Thong tin sinh vien thu %d: ", i + 1);
        xuat(sv[i]);
    }
}

void xuatthongtin_file(SV sv[], int n)
{
    FILE *file = fopen("Thong_tin_sinh_vien.txt", "w");
    if (file == NULL)
    {
        printf("Loi mo file!\n");
        return;
    }

    for (int i = 0; i < n; i++)
    {
        fprintf(file, "Thong tin sinh vien thu %d:\n", i + 1);
        fprintf(file, "Ma sinh vien: %s\n", sv[i].ma_sv);
        fprintf(file, "Ho va ten: %s\n", sv[i].ten);
        fprintf(file, "Gioi tinh: %s\n", sv[i].gioitinh);
        fprintf(file, "Toan: %.2f\n", sv[i].diem_toan);
        fprintf(file, "Li: %.2f\n", sv[i].diem_li);
        fprintf(file, "Hoa: %.2f\n\n", sv[i].diem_hoa);
    }

    fclose(file);
    printf("Da ghi thong tin sinh vien vao file!\n");
}

void xuatFILE()
{
    FILE *file = fopen("Thong_tin_sinh_vien.txt", "r");
    if (file == NULL)
    {
        printf("Loi mo file de doc!\n");
        return;
    }

    char buffer[200];
    while (fgets(buffer, sizeof(buffer), file))
    {
        printf("%s", buffer);
    }
    fclose(file);
}

int main()
{
    int luachon, n;
    char tieptuc;
    char c[100];
    SV sv[100];
    FILE *file = fopen("Thong_tin_sinh_vien.txt", "w");

    do
    {
        printf("================================MENU============================\n");
        printf("1. Nhap thong tin tat ca sinh vien\n");
        printf("2. Xuat thong tin tat ca cac sinh vien\n");
        printf("3. Xuat thong tin tat ca cac sinh vien vao FILE\n");
        printf("4. Danh sach sinh vien\n");
        printf("5. Thoat chuong trinh\n");
        printf("=================================================================\n");
        printf("\n");
        printf("Lua chon (1 - 4): ");
        printf("\n");
        scanf("%d", &luachon);
        clearBuffer();
        switch (luachon)
        {
        case 1:
            printf("Nhap so luong sinh vien: ");
            scanf("%d", &n);
            getchar();
            nhapdanhsachsv(sv, n);
            break;
        case 2:
            xuatdanhsachsv(sv, n);
            break;
        case 3:
            xuatthongtin_file(sv, n);
            break;
        case 4:
            xuatFILE();
            break;
        case 5:
            printf("Da thoat chuong trinh\n");
            return 0;
        default:
            printf("Lua chon khong hop le. Vui long nhap lai.\n");
            break;
        }
        printf("Ban co muon tiep tuc chuong trinh khong(y/n)?\n");
        tieptuc = getchar();
        clearBuffer();
    } while (tieptuc == 'Y' || tieptuc == 'y');
    printf("Chuong trinh da ket thuc\n");
    return 0;
}