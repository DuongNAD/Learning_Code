#include<iostream>
#include<iomanip>
using namespace std;
void maytinh(double a,double b,char c) {
	switch (c) {
	case'+': cout << fixed << setprecision(1) << a + b << endl;
		break;
	case'-': cout<< fixed << setprecision(1) << a - b<<endl;
		break;
	case'*': cout<< fixed << setprecision(1) << a * b<<endl;
		break;
	case'/': 
		if (b == 0) {
			cout << "Phep tinh khong hop le" << endl;
		}
		else {
			cout << fixed << setprecision(1) << a / b << endl;
		}
		break;
	default:
		break;
	}
}
void ve(int n){
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= i; j++) {
			if (i == j || j == 1 || i == n) {
				cout << "*" << " ";
			}
			else {
				cout << " " << " ";
			}
		}
		cout << endl;
	}
}
int main() {
	double a, b;
	int n;
	char c;
	cout << "Nhap a = ";
	cin >> a;
	cout << "Nhap b = ";
	cin >> b;
	cout << "Nhap dau (+,-,*,/): ";
	cin >> c;
	cout << "Ket qua = ";
	maytinh(a, b, c);
	cout << "Nhap n(n>0) = ";
	cin >> n;
	ve(n);
	return 0;
}