#include <stdio.h>
#include <string.h>

typedef struct Sinh_vien
{
    char ma_sv[50];
    char ten[50];
    char gioitinh[10];
    float diem_toan;
    float diem_li;
    float diem_hoa;
    float GPA;
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
    printf("Ho va ten: %s\n", sv.ten);
    printf("Gioi tinh: %s\n", sv.gioitinh);
    printf("Diem cac mon: \n");
    printf("Toan: %.1f\n", sv.diem_toan);
    printf("Li: %.1f\n", sv.diem_li);
    printf("Hoa: %.1f\n", sv.diem_hoa);
    printf("\n");
}

void nhapdanhsachSV(SV sv[], int n)
{
    for (int i = 0; i < n; i++)
    {
        printf("====================STT-%d====================\n", i + 1);
        nhap(&sv[i]);
        printf("\n");
    }
}

void xuatdanhsachSV(SV sv[], int n)
{
    for (int i = 0; i < n; i++)
    {
        printf("====================STT-%d====================\n", i + 1);
        xuat(sv[i]);
    }
}

void diemtrungbinhMax(SV sv[], int n)
{
    int indexMax = 0;
    float trungbinhMax = (sv[0].diem_toan + sv[0].diem_li + sv[0].diem_hoa) / 3;
    if (n <= 0)
    {
        printf("Danh sach sinh vien rong!\n");
        return;
    }
    for (int i = 0; i < n; i++)
    {
        float trungbinh = (sv[i].diem_toan + sv[i].diem_li + sv[i].diem_hoa) / 3;
        if (trungbinh > trungbinhMax)
        {
            trungbinhMax = trungbinh;
            indexMax = i;
        }
    }
    printf("Sinh vien %s - %s co diem trung binh %.1f cao nhat", sv[indexMax].ten, sv[indexMax].ma_sv, trungbinhMax);
}

void diemtrungbinhMin(SV sv[], int n)
{
    int indexMin = 0;
    float trungbinhMin = (sv[0].diem_toan + sv[0].diem_li + sv[0].diem_hoa) / 3;
    if (n <= 0)
    {
        printf("Danh sach sinh vien rong!\n");
        return;
    }
    for (int i = 0; i < n; i++)
    {
        float trungbinh = (sv[i].diem_toan + sv[i].diem_li + sv[i].diem_hoa) / 3;
        if (trungbinh < trungbinhMin)
        {
            trungbinhMin = trungbinh;
            indexMin = i;
        }
    }
    printf("Sinh vien %s - %s co diem trung binh %.1f thap nhat\n", sv[indexMin].ten, sv[indexMin].ma_sv, trungbinhMin);
}

void tim_ma_soSV(SV sv[], int n)
{
    char find[50];
    printf("Nhap ma sinh vien muon tim: ");
    fgets(find, sizeof(find), stdin);
    find[strcspn(find, "\n")] = '\0';
    int found = 0;
    for (int i = 0; i < n; i++)
    {
        if (strcmp(find, sv[i].ma_sv) == 0)
        {
            printf("Tim thay sinh vien:\n");
            xuat(sv[i]);
            found = 1;
            break;
        }
    }
    if (found == 0)
    {
        printf("Khong tim thay sinh vien co ma %s\n", find);
    }
}

void tim_tenSV(SV sv[], int n)
{
    char find[20];
    printf("Nhap ten sinh vien muon tim: ");
    scanf("%s", find);
    int found = 0;
    for (int i = 0; i < n; i++)
    {
        if (strcmp(find, sv[i].ten) == 0)
        {
            printf("Tim thay sinh vien: \n");
            xuat(sv[i]);
            found = 1;
            break;
        }
    }
    if (found == 0)
    {
        printf("Khong tim thay sinh vien co ten %s", find);
    }
}

void decreasing(SV sv[], int n)
{
    float GPA;
    for (int i = 0; i < n; i++)
    {
        sv[i].GPA = (sv[i].diem_toan + sv[i].diem_li + sv[i].diem_hoa) / 3;
    }
    for (int i = 0; i < n - 1; i++)
    {
        for (int j = 0; j < n - 1; j++)
        {
            if (sv[j].GPA < sv[j + 1].GPA)
            {
                SV temp = sv[j];
                sv[j] = sv[j + 1];
                sv[j + 1] = temp;
            }
        }
    }
    printf("Danh sach sinh vien theo diem GPA giam dan: \n");
    for (int i = 0; i < n; i++)
    {
        printf("Sinh vien %s co diem GPA %.1f\n", sv[i].ten, sv[i].GPA);
    }
}

void update(SV sv[], int n)
{
    char update[50];

    printf("Nhap ma sinh vien ban muon cap nhat: ");
    fgets(update, sizeof(update), stdin);
    update[strcspn(update, "\n")] = '\0';
    char Newname[20], NewMSV[20], NewGT[20];
    float NewToan, NewLi, NewHoa;
    int found = 0;
    for (int i = 0; i < n; i++)
    {
        if (strcmp(update, sv[i].ma_sv) == 0)
        {
            found = 1;
            int luachon;
            do
            {
                printf("1. Ma sinh vien\n");
                printf("2. Ho va ten\n");
                printf("3. Gioi tinh\n");
                printf("4. Diem\n");
                printf("5. Thoat chuong trinh\n");
                printf("Chon phan muon cap nhat (1 - 5): ");
                scanf("%d", &luachon);
                clearBuffer();
                switch (luachon)
                {
                case 1:
                    printf("Cap nhat ma sinh vien moi: ");
                    fgets(sv[i].ma_sv, sizeof(sv[i].ma_sv), stdin);
                    sv[i].ma_sv[strcspn(sv[i].ma_sv, "\n")] = '\0';
                    break;
                case 2:
                    printf("Cap nhat ho va ten moi: ");
                    fgets(sv[i].ten, sizeof(sv[i].ten), stdin);
                    sv[i].ten[strcspn(sv[i].ten, "\n")] = '\0';
                    break;
                case 3:
                    printf("Cap nhat gioi tinh moi: ");
                    fgets(sv[i].gioitinh, sizeof(sv[i].gioitinh), stdin);
                    sv[i].gioitinh[strcspn(sv[i].gioitinh, "\n")] = '\0';
                    break;
                case 4:
                    printf("Cap nhat diem:\n");
                    printf("Nhap diem toan moi: ");
                    scanf("%f", &sv[i].diem_toan);
                    printf("Nhap diem li moi: ");
                    scanf("%f", &sv[i].diem_li);
                    printf("Nhap diem hoa moi: ");
                    scanf("%f", &sv[i].diem_hoa);
                    clearBuffer();
                    break;
                case 5:
                    printf("Thoat cap nhat\n");
                    break;
                default:
                    printf("Lua chon khong hop le\n");
                    printf("Moi nhap lai");
                    break;
                }
            } while (luachon != 5);
            break;
        }
    }
    if (!found)
    {
        printf("Khong tim thay sinh vien voi ma %s\n", update);
    }
}

void xoaSV(SV sv[], int *n)
{
    char xoa[20];
    int found = 0;
    printf("Nhap ma sinh vien cua sinh vien ban muon xoa: ");
    scanf("%s", &xoa);
    clearBuffer();
    for (int i = 0; i < *n; i++)
    {
        if (strcmp(xoa, sv[i].ma_sv) == 0)
        {
            for (int j = i; j < *n - 1; j++)
            {
                sv[j] = sv[j + 1];
            }
            (*n)--;
            found = 1;
            break;
        }
        if (strcmp(xoa, sv[i].ma_sv) != 0)
        {
            printf("Khong tim thay sinh vien co ma %s\n", xoa);
        }
    }
}

void themSV(SV sv[], int *n)
{
    int viTri;
    printf("Nhap vi tri muon them: ");
    scanf("%d", &viTri);
    getchar();
    if (viTri < 0 || viTri > *n)
    {
        printf("Vi tri khong hop le!\n");
        return;
    }

    for (int i = *n; i > viTri; i--)
    {
        sv[i] = sv[i - 1];
    }

    printf("Nhap thong tin sinh vien moi:\n");
    nhap(&sv[viTri]);
    (*n)++;
}

void XoaNam_Nu(SV sv[], int *n)
{
    printf("Ban muon xoa Nam hay Nu\n");
    printf("1. Xoa nam\n");
    printf("2. Xoa nu\n");
    printf("3. Thoat\n");
    int luachon;
    scanf("%d", &luachon);
    getchar();
    char XoaNam[20] = "Nam";
    char XoaNu[20] = "Nu";
    switch (luachon)
    {
    case 1:
        for (int i = 0; i < *n; i++)
        {
            if (strcmp(XoaNam, sv[i].gioitinh) == 0)
            {
                for (int j = i; j < *n; j++)
                {
                    sv[j] = sv[j + 1];
                }
                (*n)--;
                i--;
            }
            xuatdanhsachSV(sv, *n);
        }
        break;
    case 2:

        for (int i = 0; i < *n; i++)
        {
            if (strcmp(XoaNu, sv[i].gioitinh) == 0)
            {
                for (int j = i; j < *n; j++)
                {
                    sv[j] = sv[j + 1];
                }
                (*n)--;
                i--;
            }
            xuatdanhsachSV(sv, *n);
        }
        break;
    case 3:
        return;
        break;
    default:
        printf("Lua chon khong hop le");
        break;
    }
}

int main()
{
    int n, luachon;
    char tieptuc;
    printf("Nhap so luong sinh vien: ");
    scanf("%d", &n);
    getchar();
    SV sv[n];
    nhapdanhsachSV(sv, n);
    do
    {
        printf("=============================MENU==========================\n");
        printf("1. Nhap va xuat ra thong tin ca tat ca sinh vien.\n");
        printf("2. Xuat sinh vien co diem trung binh cao nhat.\n");
        printf("3. Xuat sinh vien co diem trung binh thap nhat.\n");
        printf("4. Tim sinh vien co ma sinh vien la 123.\n");
        printf("5. Tim tat ca sinh vien co ten Nam.\n");
        printf("6. Sap xep sinh vien thu tu giam dan theo diem GPA.\n");
        printf("7. Cap nhat thong tin cua sinh vien co ma sinh vien 123.\n");
        printf("8. Xoa sinh vien co ma sinh vien 123.\n");
        printf("9. Them sinh vien o vi tri thu i.\n");
        printf("10. Xoa tat ca sinh vien co gioi tinh Nam\n");
        printf("11. Thoat chuong trinh\n");
        printf("=============================================================\n");
        printf("\n");
        printf("Lua chon (1 - 11): ");
        scanf("%d", &luachon);
        clearBuffer();

        switch (luachon)
        {
        case 1:
            xuatdanhsachSV(sv, n);
            break;
        case 2:
            diemtrungbinhMax(sv, n);
            break;
        case 3:
            diemtrungbinhMin(sv, n);
            break;
        case 4:
            tim_ma_soSV(sv, n);
            break;
        case 5:
            tim_tenSV(sv, n);
            break;
        case 6:
            decreasing(sv, n);
            break;
        case 7:
            update(sv, n);
            break;
        case 8:
            xoaSV(sv, &n);
            break;
        case 9:
            themSV(sv, &n);
            break;
        case 10:
            XoaNam_Nu(sv, &n);
            break;
        case 11:
            printf("Da thoat chuong trinh\n");
            return 0;
        default:
            printf("Lua chon khong hop le. Vui long thu lai.\n");
        }
        printf("\nBan co muon tiep tuc chuong trinh khong (y/n)? ");
        tieptuc = getchar();
        clearBuffer();
    } while (tieptuc == 'y' || tieptuc == 'Y');

    printf("Chuong trinh da ket thuc\n");
    return 0;
}