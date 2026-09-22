#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int a1, b1, c1, a2, b2, c2;
    cout << "nhap gia tri a1: ";
    cin >> a1;
    cout << "nhap gia tri b1: ";
    cin >> b1;
    cout << "nhap gia tri c1: ";
    cin >> c1;
    cout << "nhap gia tri a2: ";
    cin >> a2;
    cout << "nhap gia tri b2: ";
    cin >> b2;
    cout << "nhap gia tri c2: ";
    cin >> c2;
    int D = a1 * b2 - a2 * b1;
    int Dx = c1 * b2 - c2 * b1;
    int Dy = a1 * c2 - a2 * c1;
    if (D == 0) {
        if (Dx == 0 && Dy == 0) {
            cout << "infinite" << endl;
        }
        else {
            cout << "invalid" << endl; 
        }
    }
    else {
        double x = static_cast<double>(Dx) / D;
        double y = static_cast<double>(Dy) / D;
        cout << fixed << setprecision(1);
        cout << "x = " << x << ", y = " << y << endl;
    }
    return 0;
}