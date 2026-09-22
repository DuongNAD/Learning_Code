#include<iostream>
using namespace std;
int giaithua(int n) {
    if (n <= 1) {
        return 1;
    }
    return n * giaithua(n - 1);
}
int main() {
    int n,kq;
    cout << "Nhap n = ";
    cin >> n;
    kq = giaithua(n);
    cout << "Ket qua = " << kq<<endl;
    return 0;
}