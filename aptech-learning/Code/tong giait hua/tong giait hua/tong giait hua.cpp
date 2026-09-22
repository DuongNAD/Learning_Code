#include < iostream>
using namespace std;
int main() {
	int tong =0;
	for (int i = 1; i <= 10; i++) {
		int giaithua = 1;
		for (int j = 1; j <= i; j++) {
			giaithua = giaithua * j;
		}
		tong = tong + giaithua;
	}
	cout << tong;
	return 0;
}
