#include <stdio.h>

#define SIZE 5

// Khai báo cấu trúc Point
struct Point {
    int x;
    int y;
};

int main() {
    struct Point points[SIZE];

    // Nhập 5 điểm
    for (int i = 0; i < SIZE; i++) {
        scanf("%d %d", &points[i].x, &points[i].y);
    }

    // Tìm điểm có x lớn nhất
    int maxIndex = 0;
    for (int i = 1; i < SIZE; i++) {
        if (points[i].x > points[maxIndex].x) {
            maxIndex = i;
        }
    }

    // In ra kết quả
    printf("Max X: Point(%d,%d)\n", points[maxIndex].x, points[maxIndex].y);

    return 0;
}
