#include <stdio.h>
#include <string.h>
#include <ctype.h>

void chuyenThuongThanhHoa(char chuoi[], int viTri) {
    if (viTri >= 0 && viTri < strlen(chuoi)) {
        chuoi[viTri] = toupper(chuoi[viTri]);
    }
}

int main() {
    char chuoiNhap[100];
    int viTri;

    printf("Nhap chuoi: ");
    fgets(chuoiNhap, sizeof(chuoiNhap), stdin);
    chuoiNhap[strcspn(chuoiNhap, "\n")] = 0; // Loại bỏ ký tự newline

    printf("Nhap vi tri muon chuyen doi: ");
    scanf("%d", &viTri);

    chuyenThuongThanhHoa(chuoiNhap, viTri);

    printf("Chuoi sau khi chuyen doi: %s\n", chuoiNhap);

    return 0;
}