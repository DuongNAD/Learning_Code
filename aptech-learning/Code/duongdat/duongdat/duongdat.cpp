#include<iostream>
#include<iomanip>
using namespace std;
void maytinh(double a, double b, char c) {
	switch (c) {
	case'+': cout<< fixed << setprecision(1) << a + b << endl;
		break;
	case'-': cout<< fixed << setprecision(1) << a - b << endl;
		break;
	case'*': cout << fixed << setprecision(1) << a * b << endl;
		break;
	case'/': cout << fixed << setprecision(1) << a / b << endl;
		break;
	default:
		break;
	}
}

void vehinh(int n) {
	for (int i = n; i >= 1; i--) {
		for (int j = 1; j <= i; j++) {
				cout << "*" << " ";
		}
		cout << endl;
	}
}
int main() {
	double a, b;
	char c;
	int n;
	cout << "Nhap a =";
	cin >> a;
	cout << "Nhap b = ";
	cin >> b;
	cout << "Nhap c (+,-,*,/): ";
	cin >> c;
	cout << "Ket qua = ";
	maytinh(a, b, c);
	cout << "Nhap n = ";
	cin >> n;
	vehinh(n);
	return 0;
}