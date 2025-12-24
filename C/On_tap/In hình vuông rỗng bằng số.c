#include <stdio.h>

int main() {
    int R;
    scanf("%d", &R); // Nhập kích thước hình vuông
    
    for (int i = 1; i <= R; i++) {
        for (int j = 1; j <= R; j++) {
            // Điều kiện in số: ở viền ngoài hoặc đường chéo
            if (i == 1 || i == R || j == 1 || j == R) {
                printf("%d ", j);
            } else {
                printf("  "); // Hai khoảng trắng để căn chỉnh
            }
        }
        printf("\n"); // Xuống dòng sau mỗi hàng
    }
    
    return 0;
}