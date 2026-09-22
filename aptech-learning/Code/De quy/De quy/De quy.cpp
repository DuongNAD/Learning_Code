#include<iostream>
using namespace std;

int giaithua(int n) {
	if (n <= 1)
		return 1;
	return n * giaithua(n - 1);
}
int main() {
	int n;
	cout << "Nhap n = ";
	cin >> n;
	int kq = giaithua(n);
	cout << "kq = " << kq << endl;
	return 0;
}