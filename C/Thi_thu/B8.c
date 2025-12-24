// Bài 8: Quản lý sinh viên với struct (10 điểm)
// Viết chương trình sử dụng struct để quản lý danh sách sinh viên gồm tên, tuổi, điểm trung bình. Nhập vào danh sách n sinh viên, sau đó in ra danh sách theo thứ tự điểm giảm dần.

#include <stdio.h>
#include <string.h>

typedef struct Sinhvien
{
    char ten[50];
    int tuoi;
    float Diem;
} sv;

void Input(sv *SV)
{
    printf("Ho va ten: ");
    getchar();
    fgets(SV->ten, 50, stdin);
    size_t size = strlen(SV->ten);

    if (size > 0 && SV->ten[size - 1] == '\n')
    {
        SV->ten[size - 1] = '\0';
    }

    do
    {
        printf("Tuoi: ");
        scanf("%d", &SV->tuoi);
        if (SV->tuoi < 0)
        {
            printf("Error. Moi nhap lai\n");
        }
    } while (SV->tuoi < 0);
    do
    {
        printf("Diem ");
        scanf("%f", &SV->Diem);
        if (SV->Diem < 0 || SV->Diem > 10)
        {
            printf("Error. Moi nhap lai\n");
        }

    } while (SV->Diem < 0 || SV->Diem > 10);
}

void Output(sv *SV)
{
    printf("Ho va ten: %s\n", SV->ten);
    printf("Tuoi: %d\n", SV->tuoi);
    printf("Diem: %.1f\n", SV->Diem);
    printf("\n");
}

void sapxep(sv student[], int n)
{
    for (int i = 0; i < n - 1; i++)
    {
        for (int j = i + 1; j < n; j++)
        {
            if (student[i].Diem < student[j].Diem)
            {
                sv temp = student[i];
                student[i] = student[j];
                student[j] = temp;
            }
        }
    }
}

int main()
{
    int n;
    printf("Nhap so luong sinh vien: ");
    scanf("%d", &n);
    sv student[n];
    for (int i = 0; i < n; i++)
    {
        printf("Nhap thong tin sinh vien thu %d\n", i + 1);
        Input(&student[i]);
        printf("\n");
    }
    for (int i = 0; i < n; i++)
    {
        printf("Thong tin sinh vien thu %d\n", i + 1);
        Output(&student[i]);
    }
    printf("Sap xep sinh vien theo diem tu cao toi thap\n");
    sapxep(student, n);
    for (int i = 0; i < n; i++)
    {
        printf("Thong tin sinh vien thu %d\n", i + 1);
        Output(&student[i]);
    }
    return 0;
}
