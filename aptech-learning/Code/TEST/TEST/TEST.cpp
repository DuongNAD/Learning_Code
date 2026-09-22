#include<iostream>
using namespace std;
void vehinh(int n) {
	for (int i = n; i >= 1; i++) {
		for (int j = 1; j <= i; j++) {
			if (i == j || i == n || j == 1) {
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
	int n;
	cout << "Nhap n = ";
	cin >> n;
	vehinh(n);
	return 0;
}