#include<iostream>
using namespace std;
int main() {
    double a;
    cout << "Nhap diem: ";
    cin >> a;
    string ketqua = (a >= 8) ? "Gioi" : (((a >= 6.5 && a < 8)) ? "Kha" : ((a >= 5 && a < 6.5) ? "Trung binh" : "yeu"));
    cout << ketqua;
    return 0;
}