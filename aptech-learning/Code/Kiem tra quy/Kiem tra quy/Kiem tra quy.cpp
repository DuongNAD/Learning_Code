#include<iostream>
using namespace std;
int main() {
	int thang;
	cout << "Nhap thang: ";
	cin >> thang;
	if (thang>=1 && thang<=3) {
		cout << "Thang " << thang << " thuoc quy 1";
	}
	else if (thang >=4 &&thang<=6) {
		cout << "Thang " << thang << " thuoc quy 2";
	}
	else if (thang >=7 && thang<=9 ) {
		cout << "Thang " << thang << " thuoc quy 3";
	}
	else if (thang >= 10 && thang <= 2) {
		cout << "Thang " << thang << " thuoc quy 4";
	}
	else {
		cout << "Khong hop le";
	}
	return 0;
}