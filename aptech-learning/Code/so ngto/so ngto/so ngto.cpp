#include<iostream>
using namespace std;
int main() {
	while (true) {
		int a;
		cout << "Nhap a = ";
		cin >> a;
		if (a <= 0) {
			cout << "Vui long nhap lai a, a>0. \n ";
			continue;
		}
		bool ngto = true;
		for (int i = 2; i < a; i++) {
			if (a % i == 0) {
				ngto = false;
				break;
			}
		}
		if (ngto == true) {
			cout << a << " la so nguyen to.\n";
		}
		else {
			cout << a << " khong la so nguyen to.\n";
		}
		string traloi;
		cout << "Ban co muon tiep tuc khong?\n ";
		cout << "Bam phim n de dung\n";
	    cin >> traloi;
		if (traloi._Equal("n") || traloi._Equal("N")) {
			break;
		}
	}
	return 0;
}