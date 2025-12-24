#include <stdio.h>
#include <string.h>

void timTuDaiNhatVaNganNhat(char chuoi[]) {
    char tuDaiNhat[100] = "", tuNganNhat[100] = "";
    char tuHienTai[100] = "";
    int doDaiMax = 0, doDaiMin = 1000, doDaiHienTai = 0;
    int i = 0, j = 0;

    while (chuoi[i] != '\0') {
        if (chuoi[i] == ' ') {
            tuHienTai[j] = '\0';
            doDaiHienTai = strlen(tuHienTai);

            if (doDaiHienTai > doDaiMax) {
                doDaiMax = doDaiHienTai;
                strcpy(tuDaiNhat, tuHienTai);
            }
            if (doDaiHienTai < doDaiMin) {
                doDaiMin = doDaiHienTai;
                strcpy(tuNganNhat, tuHienTai);
            }

            j = 0;
        } else {
            tuHienTai[j++] = chuoi[i];
        }
        i++;
    }

    tuHienTai[j] = '\0';
    doDaiHienTai = strlen(tuHienTai);

    if (doDaiHienTai > doDaiMax) {
        doDaiMax = doDaiHienTai;
        strcpy(tuDaiNhat, tuHienTai);
    }
    if (doDaiHienTai < doDaiMin) {
        doDaiMin = doDaiHienTai;
        strcpy(tuNganNhat, tuHienTai);
    }

    printf("Tu dai nhat: %s\n", tuDaiNhat);
    printf("Tu ngan nhat: %s\n", tuNganNhat);
}

int main() {
    char chuoi[1000];

    printf("Nhap chuoi: ");
    fgets(chuoi, sizeof(chuoi), stdin);

    // Xóa ký tự newline nếu có
    if (chuoi[strlen(chuoi) - 1] == '\n') {
        chuoi[strlen(chuoi) - 1] = '\0';
    }

    timTuDaiNhatVaNganNhat(chuoi);

    return 0;
}