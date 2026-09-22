#include<iostream>
using namespace std;
int main () {
	int n,giaithua=1;
	cout << "Nhap so n= ";
	cin >> n;
	for (int i = 1; i <= n; i++) {
		giaithua = giaithua * i;
	}
	cout << "n! = " << giaithua;
}