#include <stdio.h>
#include <graphics.h>

int main() {
    int gd;

    // Khai triển hình tam giác
    gd = graph();
    rectangle(gd, 100, 100, 100, 200);

    // Xác định màu của tam giác
    set_color(WHITE);
    fill();

    // Vẽ đường chéo của tam giác
    line(gd, 100, 100, 100, 200);

    // Kết thúc hình
    graph_close();

    return 0;
}
