#include <stdio.h>

struct PhanSo {
    int tu;
    int mau;
};

int timUCLN(int a, int b) {
    a = (a < 0) ? -a : a;
    b = (b < 0) ? -b : b;
    while (a != b) {
        if (a > b) {
            a -= b;
        } else {
            b -= a;
        }
    }
    return a;
}

void rutGon(struct PhanSo *ps) {
    if (ps->mau < 0) {
        ps->tu = -ps->tu;
        ps->mau = -ps->mau;
    }
    int ucln = timUCLN(ps->tu, ps->mau);
    ps->tu /= ucln;
    ps->mau /= ucln;
}

void nhapPhanSo(struct PhanSo *ps) {
    printf("Nhap tu so: ");
    scanf("%d", &ps->tu);
    do {
        printf("Nhap mau so (khac 0): ");
        scanf("%d", &ps->mau);
    } while (ps->mau == 0);
}

void xuatPhanSo(struct PhanSo ps) {
    rutGon(&ps);
    if (ps.mau == 1) {
        printf("%d", ps.tu);
    } else {
        printf("%d/%d", ps.tu, ps.mau);
    }
}

struct PhanSo congPhanSo(struct PhanSo ps1, struct PhanSo ps2) {
    struct PhanSo tong;
    tong.tu = ps1.tu * ps2.mau + ps2.tu * ps1.mau;
    tong.mau = ps1.mau * ps2.mau;
    rutGon(&tong);
    return tong;
}

int main() {
    struct PhanSo ps1, ps2, ketQua;

    printf("Nhap phan so thu nhat:\n");
    nhapPhanSo(&ps1);

    printf("Nhap phan so thu hai:\n");
    nhapPhanSo(&ps2);

    ketQua = congPhanSo(ps1, ps2);

    printf("\nKet qua phep cong: ");
    xuatPhanSo(ps1);
    printf(" + ");
    xuatPhanSo(ps2);
    printf(" = ");
    xuatPhanSo(ketQua);
    printf("\n");

    return 0;
}