#include<iostream>
using namespace std;
int main() {
	int n,tong=0;
	cout << "Nhap so n = ";
	cin >> n;
	for (int i = 0; i <= n; i++) {
		if (i % 2 != 0) {
			if (i == 3) {
				continue;
			}
			else {
				tong = tong + i;
			}
		}
	}
	cout << tong ;
	return 0;
}