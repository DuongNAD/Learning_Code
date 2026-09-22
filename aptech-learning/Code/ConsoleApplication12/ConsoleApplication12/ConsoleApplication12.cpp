#include<iostream>
using namespace std;
void vehinh(int n) {
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n; j++) {
			cout << "*" << " ";
		}
		cout << endl;
	}
}
void maytinh(double a, double b,char c) {
	switch (c) {
	case '+': cout << "a + b = " << a + b << endl;
		break;
	case '-': cout << "a - b = " << a - b<<endl;
		break;
	case '*': cout << "a * b = " << a * b<<endl;
		break;
	case '/': cout << "a / b = " << a / b<<endl;
		break;
	default:
		break;
	}
}
int main() {
	double a, b;
	char c;
	int n;
	cout << "Nhap a va b = ";
	cin >> a >> b;
	cout << "Nhap dau c (+, -, *, / ): ";
	cin >> c;
	maytinh(a,b,c);
	cout << "Nhap n = ";
	cin >> n;
	vehinh(n);
	return 0;
}