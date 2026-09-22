#include <iostream>
#include <iomanip>
using namespace std;
int main()
{
    double a, b,d;
    char c;
    cin >> a >> b >> c;
    switch (c) {
    case '+':
        d = a + b;
        cout << fixed << setprecision(1)<< d<< endl;
        break;
    case '-':
        d = a - b;
        cout << fixed << setprecision(1) << d << endl;
        break;
    case '*': 
        d = a * b;
        cout << fixed << setprecision(1)<<d<<endl;
        break;
    case '/': 
        if (b == 0) {
            cout << "Invalid" << endl;
        }
        else {
            d=a/b;
            cout << fixed << setprecision(1) << d << endl;
        }
        break;
    default:
        cout << "Phep toan khong hop le!" << endl;
    }
    return 0;
}

