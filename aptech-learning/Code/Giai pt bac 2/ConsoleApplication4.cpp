#include<iostream>
#include<iomanip>
using namespace std;
int main() {
	int a, b, c,denta;
	cout << "Nhap a = ";
	cin >> a;
	cout << "Nhap b = ";
	cin >> b;
	cout << "Nhap c = ";
	cin >> c;
	denta = b * b - 4 * a * c;
	if (denta < 0) {
		cout << "Phuong trinh vo nghiem";
	}
    else if (denta ==0) {
		cout << "Phuong trinh co nghiem kep x1 = x2 = " << ( - b) / (2 * a)<<fixed<<setprecision(1);
	}
	else {
		cout << "x1 = " << ((-b) + sqrt(denta)) / (2 * a) <<fixed<< setprecision (1)<< endl;
		cout << "x2 = " << (( - b) - sqrt(denta)) / (2 * a)<<fixed<<setprecision(1);
	}
	return 0;
}