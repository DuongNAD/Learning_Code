#include<iostream>
using namespace std;
int main() {
	int n;
	cout << "Nhap n (n duoc tu 1-99): ";
	cin >> n;
	while (n< 1 || n > 99) {
		cout << "Nhap lai n (n duoc tu 1-99): ";
		cin >> n;
	}
	cout <<"So " << n;
	return 0;
}