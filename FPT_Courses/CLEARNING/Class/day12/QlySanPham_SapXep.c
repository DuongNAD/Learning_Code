#include <stdio.h>
#include <string.h>

struct Product {
    char name[50];
    int price;
    int quantity;
};

void swap(struct Product *a, struct Product *b) {
    struct Product temp = *a;
    *a = *b;
    *b = temp;
}

int main() {
    struct Product list[5] = {
        {"Laptop Dell", 20000, 5},
        {"Mouse Logitech", 500, 20},
        {"Keyboard Coo", 800, 15},
        {"USB 32GB", 250, 30},
        {"Monitor Samsung", 4000, 10}
    };
    int n = 5;
    int i, j;

    for (i = 0; i < n - 1; i++) {
        for (j = 0; j < n - i - 1; j++) {
            if (list[j].price < list[j + 1].price) {
                swap(&list[j], &list[j + 1]);
            }
        }
    }

    printf("--- Danh sach san pham (da sap xep theo gia giam dan) ---\n");
    printf("%-20s %-10s %-10s\n", "Ten SP", "Gia", "So luong");
    for (i = 0; i < n; i++) {
        printf("%-20s %-10d %-10d\n", list[i].name, list[i].price, list[i].quantity);
    }

    return 0;
}