#include <iostream>
using namespace std;

void printArrow(int n, bool left) {
    if (!left) {
        // Mũi tên hướng phải
        for (int i = 0; i < n; i++) {  // Phần đầu
            for (int j = 0; j < n - i; j++) {
                cout << "*";
            }
            cout << endl;
        }
        for (int i = 2; i <= n; i++) {  // Phần cuối
            for (int j = 0; j < i; j++) {
                cout << "*";
            }
            cout << endl;
        }
    }
    else {
        // Mũi tên hướng trái
        for (int i = 0; i < n; i++) {  // Phần đầu
            for (int j = 0; j < i; j++) {
                cout << " ";
            }
            for (int j = 0; j < n - i; j++) {
                cout << "*";
            }
            cout << endl;
        }
        for (int i = 1; i < n; i++) {  // Phần cuối
            for (int j = 0; j < n - i - 1; j++) {
                cout << " ";
            }
            for (int j = 0; j <= i; j++) {
                cout << "*";
            }
            cout << endl;
        }
    }
}
int main() {
    int n;
    bool left;

    cout << "Nhap so bac cua mui ten (n): ";
    cin >> n;
    cout << "Nhap huong cua mui ten (0: phai, 1: trai): ";
    cin >> left;

    printArrow(n, left);

    return 0;
}