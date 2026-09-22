#include<iostream>
#include<iomanip>
using namespace std;
void pheptinh(double a, double b, char c) {
	switch (c) {
	case '+': cout << fixed << setprecision(1) << a + b;
		break;
	case '-': cout << fixed << setprecision(1) << a - b;
		break;
	case'*': cout<< fixed << setprecision(1)<< a * b;
		break;
	case'/': cout << fixed << setprecision(1) << a / b;
		break;
	default:
		break;

	}
}
int main() {
	double a, b;
	char c;
	cout << "Nhap a = ";
	cin >> a;
	cout << "Nhap b = ";
	cin >>b;
	cout << "Nhap dau: ";
	cin >> c;
	cout << "Ket qua phep tinh = ";
	pheptinh(a, b, c);
	return 0;
}