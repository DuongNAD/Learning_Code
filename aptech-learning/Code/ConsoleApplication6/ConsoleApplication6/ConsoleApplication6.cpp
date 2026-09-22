#include<iostream>
using namespace std;
int main() {
	double a, b;
	char c;
	cout << "Nhap so a = ";
	cin >> a;
	cout << "Nhap dau ";
	cin >> c;
	cout << "Nhap so b = ";
	cin >> b;
		switch (c) {
	case '+': cout << a + b << endl;
		break;
	case '-':cout << a - b << endl;
		break;
	case '*':cout << a * b << endl;
		break;
	case '/':cout<<fixed<<setprecision(1)<< a / b << endl;
		break;
	}
	return 0;
}