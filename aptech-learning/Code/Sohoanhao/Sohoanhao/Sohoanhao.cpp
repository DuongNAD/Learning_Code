#include<iostream>
using namespace std;
int main() {
	cout << "So hoan hoa tu 1 den 1000 là: ";
	for (int i = 1; i <= 1000; i++) {
		int sum = 0;
		for (int n = 1; n < i; n++) {
			if (i % n == 0) {
				sum = sum + n;
			}
		}
		if (sum == i) {
			cout << sum << endl;
		}
	}
	return 0;
}