#include<iostream>
using namespace std;
int main() {
	// tinh tong cac so tu 1 den 5
	int a = 1;
	int tong = 0;
	do {
		tong = tong + a;
		a++;
	} while (a <= 5);
	cout << "tong = " << tong;
	return 0;
}