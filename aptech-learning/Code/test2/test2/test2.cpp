#include<iostream>]
using namespace std;
void vehinh(int n) {
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n; j++) {
			for (int m = 1; m <= n; m++) {
				cout << "*" << " ";
			}
			cout << endl;
		}
	}
}
int main() {
	int n;
	cout << "Nhap n = ";
	cin >> n;
	vehinh(n);
	return 0;
}