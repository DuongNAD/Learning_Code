#include<stdio.h>
#include<stdbool.h>

int main () {
    unsigned int numberOfBooks, idOfBooks; 
    bool isAvailable;
    float priceOfBooks;
    char bookGenre;
    int tempBoolInput;
    printf("Nhap so luong sach ");
    scanf("%u",&numberOfBooks);

    printf("Nhap gia tien trung binh 1 cuon sach ");
    scanf("%f",&priceOfBooks);

    printf("Nhap the loai cuon sach ");
    scanf(" %c",&bookGenre);

    printf("Nhap ID cuon sach ");
    scanf("%u", &idOfBooks);

    printf("Ton tai hoac khong (1 la co, 0 la khong) ");
    scanf("%d", &tempBoolInput);
    isAvailable = (bool)tempBoolInput;

    printf("\n");
    printf("ID sách: %u\n", idOfBooks);
    printf("Số lượng: %u\n", numberOfBooks);
    printf("Giá trung bình: %.2f VND\n", priceOfBooks);
    printf("Thể loại: %c\n", bookGenre);
    printf("Tình trạng: %s\n", isAvailable ? "Có sẵn trong kho" : "Tạm thời đã hết");

    return 0;
}