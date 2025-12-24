#include <stdio.h>

int main() {
  int n, i, sum = 0;
  int arr[100]; // Giả sử mảng có tối đa 100 phần tử

  printf("Nhập số phần tử của mảng: ");
  scanf("%d", &n);

  printf("Nhập các phần tử của mảng:\n");
  for (i = 0; i < n; i++) {
    printf("Phần tử thứ %d: ", i + 1);
    scanf("%d", &arr[i]);
  }

  // Tính tổng các phần tử lẻ
  for (i = 0; i < n; i++) {
    if (arr[i] % 2 != 0) {
      sum += arr[i];
    }
  }

  printf("Tổng các phần tử lẻ trong mảng là: %d\n", sum);

  return 0;
}