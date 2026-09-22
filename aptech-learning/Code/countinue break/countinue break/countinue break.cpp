#include<iostream>
using namespace std;
int main() {
	int tong = 0;
	for (int i = 0; i <= 5; i++) {
		if (i == 3|| i==4) {
			continue;
		}
		else {
			cout << "i= " << i << endl;
			tong = tong + i;
		}
	}
	cout << "Tong = " << tong;



	int n= 0;
	while (n < 100) {
		cout << "Gia tri cua n = " << n << endl;
		n++;
		if (n == 20) {
			break;
		}
	}
	cout << "Gia tri cuoi cung n= " << n;
	return 0;
}
