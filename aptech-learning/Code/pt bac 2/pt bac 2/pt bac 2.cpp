#include<iostream>
#include<iomanip>
using namespace std;
void nghiemptbac2(double a, double b,double c) {
	double denta;
	denta = b * b - 4 * a * c;
	if (denta < 0) {
		cout << "Phuong trinh vo nghiem"<<endl;
	}
	else if (denta == 0) {
		cout << "Phuong trinh co nghiem kep x1 = x2 = " << (-b) / (2 * a)<<endl;
	}
	else if (denta > 0) {
		cout << "x1 = " << (-b + sqrt(denta)) / 2 * a<<endl;
		cout<<"x2 = "<< (-b - sqrt(denta)) / 2 * a<<endl;
	}
}
int main() {
	nghiemptbac2(1, 2, 3);
	nghiemptbac2(1, 2, 1);
	nghiemptbac2(1, 2, -3);
	int a, b, c;
	cout << "Nhap a = ";
	cin >> a;
	cout << "Nhap b = ";
	cin >> b; 
	cout << "Nhap c = ";
	cin >> c;
	nghiemptbac2(a, b, c);
}