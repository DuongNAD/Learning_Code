#include<iostream>
using namespace std;
int main() {
	int a, tongchan = 0;
	cout << "Nhap so a= ";
	cin >> a;
	if (a % 2 == 0) {
		for (int i = 0; i <= a; i++) {
			if (i % 2 == 0) {
				tongchan = tongchan + i;
			}
		}
		cout << "Tong cac so chan = " << tongchan;
	}
	else {
		cout << "Toi khong tinh so le, bye bye";
	}
	return 0;
}